import imp
from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.
def home(request):
    my_todo = Tenants.objects.all()
    if request.method == 'POST':
        tenant_form = AddTenant(request.POST)
        if tenant_form.is_valid():
            print('tenant successfully saved')
            messages.add_message(request,'Tenant successfully saved.')
            return redirect('home')
    else:
        tenant_form = AddTenant(request.POST)
    return render(request,'homepage.html',{'my_todo':my_todo,'tenant_form':tenant_form})


