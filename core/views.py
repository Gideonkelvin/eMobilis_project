from django.shortcuts import render, redirect
from .models import (
    NewsItem, SchoolHistory, SchoolValue, LeadershipStaff, Achievement, 
    Facility, ManagementDetail, LeadershipSection, Feature, Service, CustomUser,
)
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from core.utils import send_registration_email
from .forms import RegistrationForm, LoginForm

@login_required(login_url='login')

def index(request):
    news_items = NewsItem.objects.all()  # Fetch all news items
    return render(request, 'index.html', {'news_items': news_items})

def about(request):
    history = SchoolHistory.objects.first()  # Assuming one history record
    values = SchoolValue.objects.all()
    leadership = LeadershipStaff.objects.all()
    achievements = Achievement.objects.all()
    facilities = Facility.objects.all()

    return render(request, 'about.html', {
        'history': history,
        'values': values,
        'leadership': leadership,
        'achievements': achievements,
        'facilities': facilities
    })

def management(request):
    management_detail = ManagementDetail.objects.first()  # Fetch the first entry
    return render(request, 'management.html', {'management_detail': management_detail})


def students_leadership(request):
    leadership_section = LeadershipSection.objects.first()
    features = Feature.objects.all()
    services = Service.objects.all()

    # Calculate delays for each service
    for idx, service in enumerate(services):
        service.aos_delay = idx + 1  # Add any logic you need for delay

    context = {
        'leadership_section': leadership_section,
        'features': features,
        'services': services,
    }

    return render(request, 'students_leadership.html', context)


def academics(request):
    return render(request, 'academics.html')



def user_registration(request):  # sourcery skip: extract-method
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # send registration email
            send_registration_email(user)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('/')
    return render(request, 'registration_form.html', {'form': form})

def login_user(request):
    if request.method != 'POST':
        return render (request, 'login.html')
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        user= CustomUser.objects.get(username=username)
        # user.set_password(password)
    except CustomUser.DoesNotExist:
        messages.error(request, 'username does not exist!')
        return render (request, 'login.html')
    user = authenticate(request, username=username, password=password)

    if user is None:
        messages.error(request, 'Incorrect password')
        return render (request, 'login.html')

    elif user.is_active:
        login(request, user)
        messages.success(request, 'Logged in succesfully')
    else:
        messages.error(request, 'Please activate your account')
        return render (request, 'login.html')
    return redirect('/')
    
def logout_user(request):
    logout(request)
    return redirect('login')