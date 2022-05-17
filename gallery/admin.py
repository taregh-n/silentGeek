from django.contrib import admin
from .models import *
import admin_thumbnails

@admin_thumbnails.thumbnail('image')
class ImagesInline(admin.TabularInline):
    model = GalleryImage
    extra = 0

class GalleryPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'create', 'update', 'active')
    list_filter = ('category', 'active', 'create')
    # exclude = ('like', 'dislike')
    inlines = [ImagesInline]


admin.site.register(GalleryPost, GalleryPostAdmin)
admin.site.register(GalleryCategory)