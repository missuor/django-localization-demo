# coding=utf-8
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

BOOK_CATEGORY = (
    ('novel', _('novel')),
    ('paper', _('paper'))
)


@python_2_unicode_compatible
class Book(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('author'))
    name = models.CharField(_('book name'), max_length=30)
    category = models.CharField(_('book category'), max_length=30, choices=BOOK_CATEGORY)

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Book")

    def __str__(self):
        ctx = {
            'author': self.author,
            'name': self.name,
            'category': self.category
        }
        return '%(name)s(%(category)s) %(author)s ' % ctx
