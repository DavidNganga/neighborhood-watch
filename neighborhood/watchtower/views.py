from django.shortcuts import render,redirect
from .forms import ProfileForm,PostForm,EstablishmentForm,CreateNeighborhoodForm
from .models import User,Neighborhood,Establishment,Parastatal,Profile,Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
@login_required(login_url='/accounts/login')
def watch(request):
    '''
    function to call methods in the home page
    '''
    current_user=request.user
    profiles = Profile.objects.all()
    # neighborhoods = Neighborhood.objects.all()
    posts = Post.objects.all()
    establishments =Establishment.objects.all()
    return render(request, 'index.html',{"establishments":establishments,"posts":posts,"profiles":profiles})
@login_required
def profile(request):
    '''
    function that saves users profile
    '''
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
    '''
    function that searching for all businesses
    '''
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
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('watch')
    else:
        form = PostForm()
    return render(request, 'post.html',{"form":form})

def establishment(request):
    current_user = request.user
    if request.method == 'POST':
        form = EstablishmentForm(request.POST,request.FILES)
        if form.is_valid():
            establishment = form.save(commit=False)
            establishment.save()
            return redirect('watch')
    else:
        form = EstablishmentForm()
    return render(request, 'establishment.html',{"form":form})

def viewpost(request):
    '''
    function for viewing posts created
    '''
    post = Post.objects.get()
    return render(request,'viewpost.html',{"post":post})

def viewestablishment(request):
    '''
    function for viewing establishments posted in the neighborhoods
    '''
    current_user=request.user
    establishments=Establishment.objects.all()
    return render(request,'viewestablishment.html',{"establishments":establishments})

def viewprofile(request, profile_id):
    '''
    view function for displaying a user's profile page
    '''
    current_user = request.user
    current_user.id=request.user.id
    Profile.user = current_user
    pics = Profile.objects.filter(id = profile_id)

    return render(request, 'viewprofile.html',{"pics":pics, id:profile_id})

def profiledetails(request,profile_id):
    image = Profile.objects.all()
    return render(request,'profiledetails.html',{"image":image,id:profile_id})

def create_neighbourhood(request):
    '''
    function for user to create neighbourhood
    '''

    current_user=request.user
    if request.method=='POST':
        form=CreateNeighborhoodForm(request.POST)
        if form.is_valid():
            neighbourhood=form.save(commit=False)
            neighbourhood.user = current_user
            neighbourhood.save()

            return redirect('watch')
    else:
        form=CreateNeighborhoodForm()
    return render(request, 'neighborhoodprofile.html', {"form":form})
