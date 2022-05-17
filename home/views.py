from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from .forms import ContactForm
from blog.models import Post
from chat.models import Chat
from gallery.models import GalleryPost

# Create your views here.
def home(request):
    last_posts = Post.objects.all()[:9]
    last_chats = Chat.objects.all()[:9]
    last_gposts = GalleryPost.objects.all()[:9]
    params = {
        'last_posts': last_posts,
        'last_chats': last_chats,
        'last_gposts': last_gposts,

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


def error_404_page(request, exeption):
    return render(request, '404.html', status=404)

def error_500_page(request):
    return render(request, '500.html', status=500)