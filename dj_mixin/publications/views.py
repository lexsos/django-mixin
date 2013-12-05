from django.views.generic import (
    ListView,
    DetailView,
)


class PublishedMixin(object):

    def get_queryset(self):
        queryset = super(PublishedMixin, self).get_queryset()
        return queryset.published()


class SortMixin(object):

    def _get_sort_key(self):
        return self.request.GET.get('sort', 'default')

    def _get_sort_tuple(self):
        sort_key = self._get_sort_key()
        sort_orders = getattr(self, 'sort_orders', {})
        if not sort_key in sort_orders:
            return None
        return sort_orders[sort_key]

    def get_queryset(self):
        queryset = super(SortMixin, self).get_queryset()
        sort_tuple = self._get_sort_tuple()
        if sort_tuple is None:
            return queryset
        return queryset.order_by(*sort_tuple)

    def get_context_data(self, **kwargs):
        context = super(SortMixin, self).get_context_data(**kwargs)
        context['sort'] = self._get_sort_key()
        return context


class PublicationListView(PublishedMixin, SortMixin, ListView):
    """Returns only published records."""


class PublicationDetailView(PublishedMixin, DetailView):
    """Returns only published records."""
