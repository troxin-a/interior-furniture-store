from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db import transaction
from django.forms import ValidationError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from carts.models import Cart
from orders.models import Order, OrderItem
from orders.forms import CreateOrderForm


class OrderCreateView(LoginRequiredMixin, FormView):
    form_class = CreateOrderForm
    template_name = "users/cart.html"
    success_url = reverse_lazy('user:profile')
    extra_context = {'title': 'Оформление заказа'}

    def get_initial(self):
        initial = super().get_initial()
        initial['first_name'] = self.request.user.first_name,
        initial['last_name'] = self.request.user.last_name,
        return initial

    def form_valid(self, form):
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = self.request.user
                    cart_items = Cart.objects.filter(user=user)

                    if cart_items.exists():
                        # Создать заказ
                        order = Order.objects.create(
                            user=user,
                            phone_number=form.cleaned_data['phone_number'],
                            delivery_address=form.cleaned_data['delivery_address'],
                        )
                        # Создать заказанные товары
                        for cart_item in cart_items:
                            product=cart_item.product
                            name=cart_item.product.name
                            price=cart_item.product.get_sell_price()
                            quantity=cart_item.quantity


                            if product.quantity < quantity:
                                raise ValidationError(f'Недостаточное количество товара {name} на складе\
                                                        В наличии - {product.quantity}')

                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                name=name,
                                price=price,
                                quantity=quantity,
                            )
                            product.quantity -= quantity
                            product.save()

                        # Очистить корзину пользователя после создания заказа
                        cart_items.delete()

                        messages.success(self.request, 'Заказ оформлен!')
                        return redirect('user:profile')
            except ValidationError as e:
                messages.success(self.request, e.message)
                return redirect('orders:create_order')

    def form_invalid(self, form):
        for errors in form.errors.values():
            for error in errors:
                messages.error(self.request, error)
        # messages.error(self.request, "Заполните все обязательные поля")
        return redirect('orders:create_order')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        return context_data







# @login_required
# def create_order(request):
#     if request.method == 'POST':
#         form = CreateOrderForm(data=request.POST)
#         if form.is_valid():
#             try:
#                 with transaction.atomic():
#                     user = request.user
#                     cart_items = Cart.objects.filter(user=user)

#                     if cart_items.exists():
#                         # Создать заказ
#                         order = Order.objects.create(
#                             user=user,
#                             phone_number=form.cleaned_data['phone_number'],
#                             delivery_address=form.cleaned_data['delivery_address'],
#                         )
#                         # Создать заказанные товары
#                         for cart_item in cart_items:
#                             product=cart_item.product
#                             name=cart_item.product.name
#                             price=cart_item.product.get_sell_price()
#                             quantity=cart_item.quantity


#                             if product.quantity < quantity:
#                                 raise ValidationError(f'Недостаточное количество товара {name} на складе\
#                                                        В наличии - {product.quantity}')

#                             OrderItem.objects.create(
#                                 order=order,
#                                 product=product,
#                                 name=name,
#                                 price=price,
#                                 quantity=quantity,
#                             )
#                             product.quantity -= quantity
#                             product.save()

#                         # Очистить корзину пользователя после создания заказа
#                         cart_items.delete()

#                         messages.success(request, 'Заказ оформлен!')
#                         return redirect('user:profile')
#             except ValidationError as e:
#                 messages.success(request, str(e))
#                 return redirect('user:cart')
#     else:
#         initial = {
#             'first_name': request.user.first_name,
#             'last_name': request.user.last_name,
#             }

#         form = CreateOrderForm(initial=initial)

#     context = {
#         'title': 'Оформление заказа',
#         'form': form,
#     }
#     return render(request, 'users/cart.html', context=context)
