from django.contrib import admin

from .models import Article,Comment,Song,Medsos

# Register your models here.

admin.site.register(Comment)
admin.site.register(Song)
admin.site.register(Medsos)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ["title","author","created_date"]

    list_display_links = ["title","created_date"]

    search_fields = ["title"]

    list_filter = ["created_date"]
    class Meta:
        model = Article

