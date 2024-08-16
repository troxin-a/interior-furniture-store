from django.http import JsonResponse
from django.views import View

from carts.mixins import CartMixin
from carts.models import Cart
from goods.models import Products


class CartAddView(CartMixin, View):

    def post(self, request):
        product_id = request.POST.get("product_id")
        product = Products.objects.get(id=product_id)

        cart = self.get_cart(request, product=product)

        if cart:
            cart.quantity += 1
            cart.save()
        else:
            user = None
            session_key = None
            if request.user.is_authenticated:
                user = request.user
            else:
                session_key = request.session.session_key

            Cart.objects.create(
                user=user, session_key=session_key, product=product, quantity=1
            )

        response_data = {
            "message": "Товар добавлен в корзину",
            "cart_items_html": self.render_cart(request),
        }

        return JsonResponse(response_data)


class CartChangeView(CartMixin, View):

    def post(self, request):
        cart_id = request.POST.get("cart_id")

        cart = self.get_cart(request, cart_id=cart_id)

        cart.quantity = request.POST.get("quantity")
        cart.save()

        quantity = cart.quantity

        response_data = {
            "message": "Количество изменено",
            "cart_items_html": self.render_cart(request),
            "quantity": quantity,
        }

        return JsonResponse(response_data)


class CartRemoveView(CartMixin, View):

    def post(self, request):
        cart_id = request.POST.get("cart_id")

        cart = self.get_cart(request, cart_id=cart_id)
        cart.delete()

        quantity = cart.quantity

        response_data = {
            "message": "Товар удален",
            "cart_items_html": self.render_cart(request),
            "quantity": quantity,
        }

        return JsonResponse(response_data)


class CartClearView(CartMixin, View):

    def post(self, request):
        cart = self.get_cart(request, full_cart=True)
        cart.delete()

        response_data = {
            "message": "Корзина очищена",
            "cart_items_html": self.render_cart(request),
        }

        return JsonResponse(response_data)
