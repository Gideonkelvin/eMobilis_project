from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import NewsItem, SchoolHistory, SchoolValue, LeadershipStaff, Achievement, Facility, ManagementDetail, LeadershipSection, Feature, Service, CustomUser

# Register your models here.
admin.site.register(NewsItem)
admin.site.register(SchoolHistory)
admin.site.register(SchoolValue)
admin.site.register(LeadershipStaff)
admin.site.register(Achievement)
admin.site.register(Facility)
admin.site.register(ManagementDetail)
admin.site.register(LeadershipSection)
admin.site.register(Feature)
admin.site.register(Service)
admin.site.register(CustomUser)
