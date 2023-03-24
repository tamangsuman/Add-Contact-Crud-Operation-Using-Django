from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        if Contact.objects.filter(email=email).exists() or Contact.objects.filter(phone=phone).exists():
            # handle duplicate entry error here
            messages.error(request, "email or phone already exists")
        else:
            contact=Contact(name=name,email=email,phone=phone)
            contact.save()
            messages.success(request, "Your details has been added")

    alldata=Contact.objects.all()
    context={
        'alldata':alldata
    }

    return render(request,'index.html',context)
def UpdateData(request,pk):
    contact_list = []
    contact = Contact.objects.get(id=pk)
    if request.method == 'POST':
        contact.name = request.POST['name']
        contact.email = request.POST['email']
        contact.phone = request.POST['phone']
        contact.save()
        return HttpResponseRedirect('/')
    contact_list.append({
        "name":contact.name,
        "email": contact.email,
        "phone": contact.phone
    })

    context = {'contact': contact_list}
    return render(request, 'update.html', context)

def DeleteData(request,pk):
    contact = Contact.objects.get(id=pk)
    contact.delete()
    return HttpResponseRedirect('/')
