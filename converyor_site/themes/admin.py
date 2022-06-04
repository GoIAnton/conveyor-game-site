from django.contrib import admin

from .models import Theme, Comment


class ThemeAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
    )
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


admin.site.register(Theme, ThemeAdmin)
admin.site.register(Comment)