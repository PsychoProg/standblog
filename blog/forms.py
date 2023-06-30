from django import forms
from django.core.validators import ValidationError
from .models import Contact

#
# class ContactForm(forms.Form):
#     email = forms.EmailField(required=True, widget=forms.EmailInput(
#         attrs={'placeholder': 'your email'}))
#
#     title = forms.CharField(max_length=100, required=True, widget=forms.TextInput(
#         attrs={'placeholder': 'title'}))
#
#     message = forms.CharField(widget=forms.Textarea(
#         attrs={'placeholder': 'your message', 'rows': 6}))
#
#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         if '@gmail' not in email:
#             # raise ValidationError('enter your gmail !!!', code='not_gmail')
#             self.add_error('email', 'it is not a gmail !!!')
#         # note: set non_field_errors
#         return email


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            "email": forms.EmailInput(attrs={'placeholder': 'your email'}),
            "title": forms.TextInput(attrs={'placeholder': 'title'}),
            "message": forms.Textarea(attrs={'placeholder': 'enter your message', 'rows': 6})
        }
