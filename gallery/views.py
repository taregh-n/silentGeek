from django.shortcuts import render
from .models import GalleryCategory, GalleryPost
# Create your views here.


def gallery(request):
    gallery_posts = GalleryPost.objects.filter(active=True).reverse()
    gallery_cats = GalleryCategory.objects.all()

    params = {
        'gallery_posts': gallery_posts,
        'gallery_cats': gallery_cats,
    }
    return render(request, 'gallery/gallery.html', params)