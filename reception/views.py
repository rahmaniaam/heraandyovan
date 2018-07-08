from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Guest_Form
from .models import Guest

# Create your views here.
response = {}
def index(request):
    html = 'reception/another.html'
    guest = Guest.objects.all()
    response['guest'] = guest
    response['guest_form'] = Guest_Form
    return render(request, html, response)

def add_guest(request):
    form = Guest_Form(request.POST or None)
    if(request.method == 'POST' and form.is_valid()):
        response['nama'] = request.POST['nama']
        response['email'] = request.POST['email']
        print(request.POST['answer'])
        if request.POST['answer'] == '1':
            response['answer'] = 'YES'
        else:
            response['answer'] = 'NO'
        guest = Guest(nama=response['nama'],email=response['email'], answer=response['answer'])
        guest.save()
        return HttpResponseRedirect('/reception/')
    else:
        return HttpResponseRedirect('/reception/')