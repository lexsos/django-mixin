from django.views.generic import (
    ListView,
    DetailView,
)


class PublishedMixin(object):

    def get_queryset(self):
        queryset = super(PublishedMixin, self).get_queryset()
        return queryset.published()


class PublicationListView(PublishedMixin, ListView):
    """Returns only published records."""


class PublicationDetailView(PublishedMixin, DetailView):
    """Returns only published records."""