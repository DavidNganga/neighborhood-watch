from django.shortcuts import render,redirect
from .forms import ProfileForm,NeighborhoodForm,BusinessForm
from .models import User,Neighborhood,Business,Parastatal
# Create your views here.
def watch(request):
    neighborhoods = Neighborhood.objects.all()
    businesses = Business.objects.all()
    return render(request, 'index.html',{"neighborhoods":neighborhoods,"businesses":businesses})

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
        
        neighborhoods = Neighborhood.search(search_term)
        message = f"{search_term}"
        print(neighborhoods)
        return render(request,'search.html',{"message":message,"neighborhoods":neighborhoods})
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

def business(request):
    current_user = request.user
    if request.method == 'POST':
        form = BusinessForm(request.POST,request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            # Post.user = current_user
            business.save()
            return redirect('watch')
    else:
        form = BusinessForm()
    return render(request, 'business.html',{"form":form})

def viewpost(request, neighborhood_id):

    posts = Neighborhood.objects.filter(id = neighborhood_id)
    return render(request,'viewpost.html',{"posts":posts,id:neighborhood_id})

def viewbusiness(request):
    current_user=request.user
    # neighborhoods= Neighborhood.objects.all()
    businesses=Business.objects.all()
    return render(request,'viewbusiness.html',{"businesses":businesses})






