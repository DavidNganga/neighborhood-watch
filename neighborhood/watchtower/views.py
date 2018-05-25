from django.shortcuts import render,redirect
from .forms import ProfileForm,PostForm
from .models import User,Neighborhood,Business,Parastatal,Post
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

        neighborhoods = Neighborhood.search(search_term)
        message = f"{search_term}"
        print(neighborhoods)
        return render(request,'search.html',{"message":message,"neighborhoods":neighborhoods})
    else:
        message="You haven't searched for any term"
        return render(request,'search.html',{"message":message})

def post(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            # Post.user = current_user
            post.save()
            return redirect('watch')
    else:
        form = PostForm()
    return render(request, 'post.html',{"form":form})
