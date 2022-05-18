from django.contrib import admin
from .models import *
# Register your models here.

class CommentInline(admin.TabularInline):
    readonly_fields = ('user', 'name', 'post', 'site', 'email', 'content', 'parent')
    exclude = ('image',)
    show_change_link = True
    model = Comment
    extra = 0
    max_num=0

class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    list_display = ('title', 'author','create', 'update', 'active')
    list_filter = ('author', 'category', 'tags','create', 'update', 'active')

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Post, PostAdmin)
admin.site.register(Category)