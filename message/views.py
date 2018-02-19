from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Surat_Form
from .models import Surat

# Create your views here.
response = {}
def index(request):
    response['author'] = "Rahmania Astrid Mochtar" #TODO Implement yourname
    surat = Surat.objects.all()
    response['surat'] = surat
    html = 'message/message.html'
    response['surat_form'] = Surat_Form
    return render(request, html, response)

def add_surat(request):
    form = Surat_Form(request.POST or None)
    if(request.method == 'POST' and form.is_valid()):
        response['dari'] = request.POST['dari']
        response['untuk'] = request.POST['untuk']
        response['pesan'] = request.POST['pesan']
        surat = Surat(dari=response['dari'],untuk=response['untuk'],pesan=response['pesan'])
        surat.save()
        return HttpResponseRedirect('/message/')
    else:
        return HttpResponseRedirect('/message/')

def delete_surat(request, id_num):
    surat = Surat.objects.get(pk=id_num)
    surat.delete()
    return HttpResponseRedirect('/message/')
