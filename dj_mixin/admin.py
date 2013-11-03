from django.utils.translation import ugettext_lazy as _
from tinymce.widgets import AdminTinyMCE


class AdminTinymceMixin(object):

    rich_fields = []

    def get_rich_fields(self):
        return self.rich_fields

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in self.get_rich_fields():
            kwargs['widget'] = AdminTinyMCE()
        return super(AdminTinymceMixin, self).formfield_for_dbfield(db_field, **kwargs)


class EnabledMixin(object):

    def make_enabled(self, request, queryset):
        queryset.update(enabled=True)

    def make_disabled(self, request, queryset):
        queryset.update(enabled=False)

    def get_actions(self, request):
        actions = super(EnabledMixin, self).get_actions(request)
        if not 'make_enabled' in actions:
            action = (self.make_enabled,
                      'make_enabled',
                      _('Enable selected %(verbose_name_plural)s'))
            actions['make_enabled'] = action
        if not 'make_disabled' in actions:
            action = (self.make_disabled,
                      'make_disabled',
                      _('Disable selected %(verbose_name_plural)s'))
            actions['make_disabled'] = action
        return actions