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
