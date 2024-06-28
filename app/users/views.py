from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.db.models import Count, Max, Sum
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from carts.models import Cart
from users.forms import UserEditForm, UserLoginForm, UserRegistrationForm


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            session_key = request.session.session_key

            if user:
                auth.login(request, user)
                messages.success(request, f"Вы успешно вошли в аккаунт {username}")

                if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user)

                    # Объединение одинаковых товаров в одну корзину
                    user_carts = Cart.objects.filter(user=user)
                    repeat_products = user_carts.values('product_id').annotate(cnt=Count('id')).filter(cnt__gt=1)
                    for product in repeat_products:        
                        prod = user_carts.filter(product_id=product['product_id'])
                        id = prod.values('product_id').annotate(id=Max('id'))[0]['id']
                        summ = prod.values('product_id').annotate(summ=Sum('quantity'))[0]['summ']

                        user_carts.filter(id=id).update(quantity=summ)
                        user_carts.exclude(id=id).filter(product_id=product['product_id']).delete()

                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('user:logout'):
                    return HttpResponseRedirect(request.POST.get('next'))

                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()


    context = {
        'title': 'Авторизация',
        'form': form,
    }

    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()

            session_key = request.session.session_key

            user = form.instance
            auth.login(request, user)

            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)
            messages.success(request, f"Вы успешно зарегистрировались и вошли в аккаунт {user.username}")
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'Регистрация',
        'form': form,
    }

    return render(request, 'users/registration.html', context)


@login_required
def profile(request):
    if request.method == "POST":
        form = UserEditForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Профиль успешно обновлен")
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = UserEditForm(instance=request.user)

    context = {
        'title': 'Профиль пользователя',
        'form': form,
    }

    return render(request, 'users/profile.html', context)


def cart(request):
    context = {
        'title': 'Корзина',
    }

    return render(request, 'users/cart.html', context)


@login_required
def logout(request):
    messages.success(request, "Выполнен выход из аккаунта")
    auth.logout(request)    
    return redirect(reverse('main:index'))
