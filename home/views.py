from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from .forms import ContactForm
from blog.models import Post
from chat.models import Chat
from gallery.models import GalleryPost

# Create your views here.
def home(request):
    new_posts = Post.objects.filter(active = True).reverse()[:9]
    new_chats = Chat.objects.filter(hidden=False).reverse()[:9]
    new_gposts = GalleryPost.objects.filter(active = True).reverse()[:9]
    params = {
        'new_posts': new_posts,
        'new_chats': new_chats,
        'new_gposts': new_gposts,

    }
    return render(request, 'home/home.html', params)


def contact(request):
    ref_url = request.META.get('HTTP_REFERER')
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            data = contact_form.cleaned_data
            name = data['name']
            subject = f'{name} | ' + data['subject']
            email = data['email']
            message = data['message']
            mail_content = f'<p style="direction: rtl; font-size: 16px; font-weight: bold;"> فرستنده: {email}<br>{message} </p>'

            msg = EmailMessage(
                subject,
                mail_content,
                f'SilentGeek <taregh.na@gmail.com>',
                ['taregh.n@gmail.com',],
            )
            msg.content_subtype = "html"
            msg.send()
            return redirect(ref_url)
    params = {
        'contact_form': contact_form,
    }
    return render(request, 'home/contact.html', params)


def search(request):
    if 'search' in request.GET:
        kw = request.GET.get('search')
        search_posts = Post.objects.filter(title__icontains = kw, active = True).reverse()
        search_chats = Chat.objects.filter(topic__icontains = kw, hidden = False).reverse()
        search_gposts = GalleryPost.objects.filter(title__icontains = kw, active = True).reverse()
        params = {
            'search_posts': search_posts,
            'search_chats': search_chats,
            'search_gposts': search_gposts,
        }
        return render(request, 'home/search.html', params)

    return render(request, 'home/search.html')


def error_404_page(request, exeption):
    return render(request, '404.html', status=404)

def error_500_page(request):
    return render(request, '500.html', status=500)