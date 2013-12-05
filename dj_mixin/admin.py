from tinymce.widgets import AdminTinyMCE


class AdminTinymceMixin(object):

    rich_fields = []

    def get_rich_fields(self):
        return self.rich_fields

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in self.get_rich_fields():
            kwargs['widget'] = AdminTinyMCE()
        return super(AdminTinymceMixin, self).formfield_for_dbfield(db_field, **kwargs)
