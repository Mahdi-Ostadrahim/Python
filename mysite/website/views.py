from email import message
from django.shortcuts import render
from blog.models import Post
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from website.models import Contact
from website.forms import NameForm, ContactForm, NewsletterForm
from django.contrib import messages
def index_view(request):
    return render(request, 'website/index.html')
def about_view(request):
    return render(request, 'website/about.html')
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            formb = form.save(commit=False)
            formb.name = "unknown"
            formb.save()
            messages.add_message(request,messages.SUCCESS,'your ticket submitted successfully')
        else:
            messages.add_message(request,messages.ERROR,'your ticket didn\'t submit')
    form = ContactForm()
    return render(request, 'website/contact.html',{'form':form})
def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
def test_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('done')
        else:
            return HttpResponse('not valid')
    form = ContactForm()
    return render(request,'test.html',{'form':form})