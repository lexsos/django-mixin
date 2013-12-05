from django.db.models import Q
from django.db.models import query
from django.utils import timezone


class PublicationQuerySet(query.QuerySet):

    def expired(self):
        return self.filter(pub_date_end__lt=timezone.now())

    def future(self):
        return self.filter(pub_date_start__gt=timezone.now())

    def enabled(self):
        return self.filter(enabled=True)

    def disabled(self):
        return self.filter(enabled=False)

    def unpublished(self):
        return self.filter(~self._published_query())

    def published(self):
        return self.filter(self._published_query())

    def _published_query(self):
        now = timezone.now()
        q = Q(pub_date_end__gte=now) | Q(pub_date_end=None)
        q &= Q(pub_date_start__lte=now)
        q &= Q(enabled=True)
        return q
