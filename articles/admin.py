from django.contrib import admin

from .models import Article, Comment

from utilities.text_utilities import crop_text


class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'body']


class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 1


class ArticleAdmin(admin.ModelAdmin):

    @admin.display(description='body')
    def body_crop(self, obj):
        return crop_text(obj.body, 100)

    list_display = ['title', 'body_crop', 'author', 'published']
    inlines = [CommentInLine]

    actions = ['publish', 'unpublish']

    @admin.action(description='Опубликовать')
    def publish(modeladmin, request, queryset):  
        queryset.update(published=True)

    @admin.action(description='Снять с публикации')
    def unpublish(modeladmin, request, queryset):  
        queryset.update(published=False)

# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)