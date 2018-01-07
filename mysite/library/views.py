from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import BookTable

def vote(request):
    all_books = BookTable.objects.all()
    return render(request,"library/index.html",{'all_books': all_books})
#this is our view page which will show library page
