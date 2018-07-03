from django import forms

class Guest_Form(forms.Form):
    error_messages = {
        'required': 'Tolong isi input ini',
    }
    nama_attrs = {
        'type': 'text',
        'class': 'guest-form-input',
        'placeholder':'Masukan nama anda'
    }
    email_attrs = {
        'type': 'email',
        'class': 'guest-form-input',
        'placeholder':'Masukan email anda'
    }

    nama = forms.CharField(label='', required=True, max_length=50, widget=forms.TextInput(attrs=nama_attrs))
    email = forms.EmailField(label='', required=True, max_length=50, widget=forms.TextInput(attrs=email_attrs))
    
    CHOICES = ((1, 'YES!',), (2, 'No :(',))
    answer = forms.ChoiceField(label='Are you going?', required=True,widget=forms.RadioSelect, choices=CHOICES)