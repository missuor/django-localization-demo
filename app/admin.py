# coding=utf-8
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
import models


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name_and_category', 'author')

    def name_and_category(self, obj):
        ctx = {
            'name': obj.name,
            'category': dict(models.BOOK_CATEGORY).get(obj.category)
        }
        return '%(name)s(%(category)s)' % ctx
    name_and_category.short_description = _('book name')
