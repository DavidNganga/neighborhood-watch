from django.shortcuts import render,redirect
from .forms import ProfileForm,NeighborhoodForm,EstablishmentForm
from .models import User,Neighborhood,Establishment,Parastatal
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def watch(request):
    neighborhoods = Neighborhood.objects.all()
    establishments =Establishment.objects.all()
    return render(request, 'index.html',{"neighborhoods":neighborhoods,"establishments":establishments})

def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
            return redirect('watch')
    else:
        form = ProfileForm()
    return render(request, 'profile.html', {"form": form})

def search(request):
    if 'name' in request.GET and request.GET["name"]:
        search_term = request.GET.get("name")

        establishments = Establishment.search(search_term)
        message = f"{search_term}"
        print(establishments)
        return render(request,'search.html',{"message":message,"establishments":establishments})
    else:
        message="You haven't searched for any term"
        return render(request,'search.html',{"message":message})

def post(request):
    current_user = request.user.id

    if request.method == 'POST':
        form = NeighborhoodForm(request.POST,request.FILES)
        if form.is_valid():
            neighborhood = form.save(commit=False)
            # Post.user = current_user
            neighborhood.save()
            return redirect('watch')
    else:
        form = NeighborhoodForm()
    return render(request, 'post.html',{"form":form})

def establishment(request):
    current_user = request.user
    if request.method == 'POST':
        form = EstablishmentForm(request.POST,request.FILES)
        if form.is_valid():
            establishment = form.save(commit=False)
            # Post.user = current_user
            establishment.save()
            return redirect('watch')
    else:
        form = EstablishmentForm()
    return render(request, 'establishment.html',{"form":form})

def viewpost(request, neighborhood_id):

    posts = Neighborhood.objects.filter(id = neighborhood_id)
    return render(request,'viewpost.html',{"posts":posts,id:neighborhood_id})

def viewestablishment(request):
    current_user=request.user
    # neighborhoods= Neighborhood.objects.all()
    establishments=Establishment.objects.all()
    return render(request,'viewestablishment.html',{"establishments":establishments})
