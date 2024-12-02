from django.contrib import admin
from .models import NewsItem, SchoolHistory, SchoolValue, LeadershipStaff, Achievement, Facility, ManagementDetail, LeadershipSection, Feature, Service

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