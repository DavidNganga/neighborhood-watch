from django.shortcuts import render

# Create your views here.
def watch(request):
    return render(request, 'index.html')
