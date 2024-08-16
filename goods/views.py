from django.db.models.base import Model as Model
from django.views.generic import DetailView, ListView

from goods.utils import get_queryset_or_404, q_search
from goods.models import Products


class ProductsListView(ListView):
    model = Products
    template_name = "goods/catalog.html"
    paginate_by = 6
    category_slug = None

    def get(self, request, category_slug=None):
        self.category_slug = category_slug
        self.queryset = Products.objects.all()

        order_by = request.GET.get("order_by")
        on_sale = request.GET.get("on_sale")
        query = request.GET.get("q")

        if category_slug == "all":
            self.queryset = self.queryset
        elif query:
            self.queryset = q_search(query)
        else:
            self.queryset = get_queryset_or_404(
                Products.objects.filter(category__slug=category_slug)
            )

        if on_sale:
            self.queryset = self.queryset.filter(discount__gt=0)
        if order_by and order_by != "default":
            self.queryset = self.queryset.order_by(order_by)
        return super().get(request)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["title"] = "Каталог"
        context_data["slug_url"] = self.category_slug
        return context_data


class ProductsDetailView(DetailView):
    model = Products
    template_name = "goods/product.html"
    slug_url_kwarg = "product_slug"
