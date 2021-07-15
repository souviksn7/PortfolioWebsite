from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    # return HttpResponse("this is my home pagem (/home)")
    context= {'name': 'Harry', 'course': 'Django'}
    return render(request, 'home.html', context)

def about(request):
    # return HttpResponse("this is my home pagem (/about)")
    return render(request, 'about.html')

def projects(request):
    # return HttpResponse("this is my home pagem (/project)")
    return render(request, 'projects.html')

def contact(request):
    if request.method=="POST":
        print("This is post")
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        desc=request.POST['desc']
        #print(name, email, phone, desc)
        ins = Contact(name=name, email=email, phone=phone, desc=desc)
        ins.save()
        print("the data has been written to the db")

    # return HttpResponse("this is my home pagem (/contact)")
    return render(request, 'contact.html')