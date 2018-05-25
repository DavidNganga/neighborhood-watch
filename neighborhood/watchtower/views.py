from django.shortcuts import render,redirect
from .forms import ProfileForm
from .models import User
# Create your views here.
def watch(request):
    return render(request, 'index.html')

def profile(request):
    current_user = request.user
    if request.method == 'POST':

        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():

            profile = form.save(commit=False)
            Profile.user = current_user
            profile.save()
            return redirect('watch')
    else:
        form = ProfileForm()
    return render(request, 'profile.html', {"form": form})

def search(request):
    if 'name' in request.GET and request.GET["name"]:
        search_term = request.GET.get("name")
        businesses = Business.search(search_term)
        message = f"{search_term}"
        return render(request,'search.html',{"message":message,"businesses":businesses})
    else:
        message="You haven't searched for any term"
        return render(request,'search.html',{"message":message})
