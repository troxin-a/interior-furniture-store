from django.contrib.postgres.search import (
    SearchQuery,
    SearchRank,
    SearchVector,
    SearchHeadline,
)
from django.http import Http404


from goods.models import Products


def get_queryset_or_404(klass):
    """
    Нужна функция, которая возвращает именно queryset, а не list
    """
    queryset = klass
    if queryset:
        return queryset
    raise Http404("Нет такой категории")


def q_search(query):
    if query.isdigit() and len(query) <= 6:
        return Products.objects.filter(id=int(query))

    vector = SearchVector("name", "description")
    query = SearchQuery(query)

    result = (
        Products.objects.annotate(rank=SearchRank(vector, query))
        .filter(rank__gt=0)
        .order_by("-rank")
    )

    result = result.annotate(
        headline=SearchHeadline(
            "name",
            query,
            start_sel='<span style="background-color: yellow;">',
            stop_sel="</span>",
        ),
    )
    result = result.annotate(
        bodyline=SearchHeadline(
            "description",
            query,
            start_sel='<span style="background-color: yellow;">',
            stop_sel="</span>",
        ),
    )

    return result
