from django.shortcuts import render,  redirect
from .models import Chat, ChatReply
from .forms import ReplyForm
from django.contrib import messages
# Create your views here.


def has_active():
    actives = Chat.objects.filter(active = True)
    if actives:
        return True
    return False

def has_deactive():
    deactives = Chat.objects.filter(active = False)
    if deactives:
        return True
    return False

def chat(request):
    reply_form = ReplyForm()
    active_chats = Chat.objects.filter(active = True)
    deactive_chats = Chat.objects.filter(active = False)
    params = {
        'actives': active_chats,
        'deactives': deactive_chats,
        'has_active': has_active(),
        'has_deactive': has_deactive(),
        'reply_form': reply_form,
    }
    return render(request, 'chat/chat.html', params)


def send_reply(request, chat_id):
    ref_url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        reply_form = ReplyForm(request.POST)
        if reply_form.is_valid():
            data = reply_form.cleaned_data
            new_reply = ChatReply.objects.create(
                user_id = request.user.id,
                chat_id= chat_id,
                name= data['name'],
                comment= data['comment'],
                email= data['email'],
                site= data['site'],
            )
            new_reply.save()
            messages.success(request, 'پاسخ شما ثبت شد', 'success')
        else:
            messages.warning(request, 'خطایی در ثبت پاسخ شما رخ داده است', 'danger')
    return redirect(ref_url)

# def replys(request, chat_id):
#     chat = get_object_or_404(Chat, id=chat_id)
#     replys = ChatReply.objects.filter(chat_id= chat_id)
#     params= {
#         'chat': chat,
#         'replys': replys,
#     }
#     return render(request, 'chat/chat_replys.html', params)