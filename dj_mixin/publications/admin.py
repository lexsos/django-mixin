from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


class EnabledMixin(object):

    def make_enabled(self, request, queryset):
        queryset.update(enabled=True)

    def make_disabled(self, request, queryset):
        queryset.update(enabled=False)

    def get_actions(self, request):
        actions = super(EnabledMixin, self).get_actions(request)
        if not 'make_enabled' in actions:
            action = (EnabledMixin.make_enabled,
                      'make_enabled',
                      _('Enable selected %(verbose_name_plural)s'))
            actions['make_enabled'] = action
        if not 'make_disabled' in actions:
            action = (EnabledMixin.make_disabled,
                      'make_disabled',
                      _('Disable selected %(verbose_name_plural)s'))
            actions['make_disabled'] = action
        return actions


class WeightMixin(object):

    def zero_weight(self, request, queryset):
        queryset.update(weight=0)

    def get_actions(self, request):
        actions = super(WeightMixin, self).get_actions(request)
        if not 'zero_weight' in actions:
            action = (WeightMixin.zero_weight,
                      'zero_weight',
                      _('Set weight to 0 on selected %(verbose_name_plural)s'))
            actions['zero_weight'] = action
        return actions


class PublicationAdmin(EnabledMixin, WeightMixin, admin.ModelAdmin):

    list_filter = ('enabled', 'pub_date_start', 'weight')
    list_display = ('enabled', 'pub_date_start', 'pub_date_end', 'weight')
    list_per_page = 30
    date_hierarchy = 'pub_date_start'

    fieldsets = (
        (_('Publication parameters'), {
            'classes': ('wide',),
            'fields': ('enabled',
                       'pub_date_start',
                       'pub_date_end',
                       'weight')
        }),
    )
