from django.shortcuts import render

# Create your views here.
def specific_jinja(request):
    D={'name':'Shiri','Age':22,'behavior':'Good girl'}
    return render(request,'specific_jinja.html',context=D)