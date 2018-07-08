from django import forms

class Guest_Form(forms.Form):
    error_messages = {
        'required': 'Tolong isi input ini',
    }
    nama_attrs = {
        'type': 'text',
        'class': 'guest-form-input',
        'placeholder':'Name'
    }
    email_attrs = {
        'type': 'email',
        'class': 'guest-form-input',
        'placeholder':'Email'
    }

    nama = forms.CharField(label='', required=True, max_length=50, widget=forms.TextInput(attrs=nama_attrs))
    email = forms.EmailField(label='', required=True, max_length=50, widget=forms.TextInput(attrs=email_attrs))
    
    CHOICES = ((1, 'Will definitely be there!',), (2, 'Sorry, I can\'t make it',))
    answer = forms.ChoiceField(label='', required=True,widget=forms.RadioSelect, choices=CHOICES)