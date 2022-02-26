import imp
from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.
def home(request):
    tenant = Tenant.objects.all()
    if request.method == 'POST':
        tenant_form = AddTenant(request.POST)
        if tenant_form.is_valid():
            tenant_form.save()
            
            # messages.add_message(request,'Tenant successfully saved.')
            return redirect('home')
    else:
        tenant_form = AddTenant(request.POST)
     
    return render(request,'homepage.html',{'tenant':tenant,'tenant_form':tenant_form})

def destroy(request,id):
    single = Tenant.objects.get(id=id)
    single.delete()
    print("6"*100)
    return redirect('/')



