
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from .managers import PublicationManager


class Publication(models.Model):
    """Abstract model fot publication like objects."""

    enabled = models.BooleanField(
        verbose_name=_('enabled'),
        default=True,
        db_index=True,
        help_text=_('show/hide record.'),
    )
    pub_date_start = models.DateTimeField(
        verbose_name=_('start date for publication'),
        default=timezone.now,
        db_index=True,
        help_text=_('Rocord will be visible form this date.'),
    )
    pub_date_end = models.DateTimeField(
        verbose_name=_('end date for publication'),
        null=True,
        blank=True,
        db_index=True,
        help_text=_('Rocord will be invisible form this date.'),
    )
    weight = models.PositiveIntegerField(
        verbose_name=_('weight of publication'),
        db_index=True,
        default=0,
        help_text=_('Rocord will be first with greate weight.'),
    )

    objects = PublicationManager()

    class Meta:
        abstract = True
        ordering = ['-weight', '-pub_date_start']
