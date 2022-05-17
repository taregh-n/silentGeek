from django import forms
from .models import ChatReply

class ReplyForm(forms.ModelForm):
    class Meta:    
        model = ChatReply
        fields = ['name', 'comment', 'email', 'site',]
