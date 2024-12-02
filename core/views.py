from django.shortcuts import render
from .models import NewsItem, SchoolHistory, SchoolValue, LeadershipStaff, Achievement, Facility, ManagementDetail, LeadershipSection, Feature, Service
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

def login(request):
    return render(request, 'login.html')