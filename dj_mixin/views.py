from django.http import Http404


class EnabledMixin(object):

    def get_queryset(self):
        queryset = super(EnabledMixin, self).get_queryset()
        return queryset.filter(enabled=True)


class SortMixin(object):

    def _get_sort_key(self):
        return self.request.GET.get('sort', 'default')

    def _get_sort(self):
        sort = self._get_sort_key()
        if not sort in self.sort_orders:
            return None
        return self.sort_orders[sort]

    def get_queryset(self):
        queryset = super(SortMixin, self).get_queryset()
        sort = self._get_sort()
        if not sort:
            raise Http404
        return queryset.order_by(*sort)

    def get_context_data(self, **kwargs):
        context = super(SortMixin, self).get_context_data(**kwargs)
        context['sort'] = self._get_sort_key()
        return context
