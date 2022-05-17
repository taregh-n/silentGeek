from django import forms



class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    subject = forms.CharField(max_length=50)
    email = forms.EmailField()
    message = forms.CharField(max_length=500)