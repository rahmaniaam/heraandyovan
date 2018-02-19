from django import forms

class Surat_Form(forms.Form):
    error_messages = {
        'required': 'Tolong isi input ini',
    }
    dari_attrs = {
        'type': 'text',
        'class': 'surat-form-input',
        'placeholder':'Masukan nama pengirim'
    }
    untuk_attrs = {
        'type': 'text',
        'class': 'surat-form-input',
        'placeholder':'Masukan nama penerima'
    }
    pesan_attrs = {
        'type': 'text',
        'cols': 50,
        'rows': 4,
        'class': 'surat-form-textarea',
        'placeholder':'Masukan pesanmu'
    }

    dari = forms.CharField(label='', required=True, max_length=30, widget=forms.TextInput(attrs=dari_attrs))
    untuk = forms.CharField(label='', required=True, max_length=30, widget=forms.TextInput(attrs=untuk_attrs))
    pesan = forms.CharField(label='', required=True, widget=forms.Textarea(attrs=pesan_attrs))


