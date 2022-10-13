from email import message
from django import forms
from website.models import Contact,Newsletter
class NameForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)

class ContactForm(forms.ModelForm):
    subject = forms.CharField(required=False)
    class Meta:
        model = Contact
        fields = '__all__'
        def clean_form(self):
            data = self.cleaned_data['name']
            return data

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'