from django import forms


class Contact(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'your email', 'rows': 6}), required=True)

    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'your message'}))


