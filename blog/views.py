from django.shortcuts import render
from blog.forms import ContactForm
from blog.models import AboutMe, Contact, MySiteLink
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, "pages/home.html")

def about(request):
    text = AboutMe.objects.all()
    return render(request, 'pages/about.html',{'texts': text})

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message sended successfully!!!')
            
    return render(request, "pages/contact.html", {'form': form})

def sites(request):
    return render(request, "pages/sites.html")

def mymessages(request):
    messages = Contact.objects.all()
    return render(request, "pages/messages.html", {'messages': messages})


