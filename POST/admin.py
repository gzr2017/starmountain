from django.contrib import admin
from .models import Article, Message


class ArticleAdmin(admin.ModelAdmin):
    search_fields = ('title', 'body')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Message)
