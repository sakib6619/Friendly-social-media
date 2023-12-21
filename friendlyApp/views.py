from django.shortcuts import render,redirect
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.
@login_required(login_url='signin')
def Home(request):
    posts = Post.objects.all()
    return render(request, 'homefeed.html',locals())
def signUp(request):
    if not request.user.is_authenticated: 
        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'User created successful...!!')
                return redirect('signin')
        else:
            form = SignUpForm()
        return render(request, 'signUp.html', locals())
    else:
        return redirect('Home')
    
def signIn(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('Home')
        else:        
            form = AuthenticationForm()
        return render(request, 'signin.html',locals())
    else:
        return redirect('Home')
@login_required(login_url='signin')
def userProfile(request):
    edit_profile =  Profile.objects.get(user=request.user)
    if request.method =="POST":
        if request.FILES.get('image','cover') == None:
            profile_image = edit_profile.image
            cover = edit_profile.coverImg
            first_name = request.POST.get('fname')
            last_name = request.POST.get('lname')
            bio = request.POST.get('bio')
            gender = request.POST.get('gender')
            relationship = request.POST.get('relationship')
            birthDate = request.POST.get('birthDate')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            
            edit_profile.image = profile_image
            edit_profile.coverImg = cover
            edit_profile.user.first_name = first_name
            edit_profile.user.last_name = last_name
            edit_profile.bio = bio
            edit_profile.gender = gender
            edit_profile.relationship = relationship
            edit_profile.birth_date = birthDate
            edit_profile.user.email = email
            edit_profile.phone = phone
            edit_profile.address = address
            edit_profile.save()
            return redirect('profile')
        else:
            profile_image = request.FILES.get('image')
            cover = request.FILES.get('cover')
            first_name = request.POST.get('fname')
            last_name = request.POST.get('lname')
            bio = request.POST.get('bio')
            gender = request.POST.get('gender')
            relationship = request.POST.get('relationship')
            birthDate = request.POST.get('birthDate')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            
            edit_profile.image = profile_image
            edit_profile.coverImg = cover
            edit_profile.user.first_name = first_name
            edit_profile.user.last_name = last_name
            edit_profile.bio = bio
            edit_profile.gender = gender
            edit_profile.relationship = relationship
            edit_profile.birth_date = birthDate
            edit_profile.user.email = email
            edit_profile.phone = phone
            edit_profile.address = address
            edit_profile.save()
            return redirect('profile')
    else:
        return render(request, 'user_pofile.html', locals())
@login_required(login_url='signin')
def friendRequest(request):
    return render(request, 'friend_request.html')
@login_required(login_url='signin')
def chatlist(request):
    return render(request, 'chatlist.html')
@login_required(login_url='signin')
def message(request):
    return render(request, 'Chatinbox.html')
def forgotPassword(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, 'Password changed successful..!')
                return redirect('profile')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, 'Forgot_password.html', locals())
    else:
        return redirect('signin')
@login_required(login_url='signin')
def user_logout(request):
    logout(request)
    return redirect('signin')
