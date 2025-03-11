from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello there")

def files(request):
    return HttpResponse("List of files")