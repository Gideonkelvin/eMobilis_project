from django.contrib.auth.models import AbstractUser
from django.db import models

class NewsItem(models.Model):
    title = models.CharField(max_length=255)  # Title of the news post
    description = models.TextField()  # Short description of the news
    images = models.ImageField(upload_to='news_images/')  # Image associated with the news
    author = models.CharField(max_length=255)  # Author's name
    date = models.DateTimeField(auto_now_add=True)  # Date the news item was created

    def __str__(self):
        return self.title

class SchoolHistory(models.Model):
    title = models.CharField(max_length=200)
    year_established = models.IntegerField()
    description = models.TextField()
    milestones = models.TextField()
    image = models.ImageField(upload_to='history/')

    def __str__(self):
        return self.title

class SchoolValue(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

class LeadershipStaff(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='staff/')

    def __str__(self):
        return self.name

class Achievement(models.Model):
    description = models.TextField()

    def __str__(self):
        return self.description[:50]  # First 50 characters

class Facility(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, help_text="Enter the FontAwesome icon class name (e.g., 'fas fa-flask').")
    description = models.TextField()

    def __str__(self):
        return self.name

class ManagementDetail(models.Model):
    title = models.CharField(max_length=255, default="Management")
    description = models.TextField()
    image = models.ImageField(upload_to='management_images/')
    catalog_pdf = models.FileField(upload_to='catalogs/', blank=True, null=True)
    catalog_doc = models.FileField(upload_to='catalogs/', blank=True, null=True)
    phone = models.CharField(max_length=15, default="+1 5589 55488 55")
    email = models.EmailField(default="contact@example.com")

    def __str__(self):
        return self.title


class LeadershipSection(models.Model):
    title = models.CharField(max_length=255, help_text="Title of the leadership section")
    description_1 = models.TextField(help_text="First description for the leadership section")
    description_2 = models.TextField(help_text="Second description for the leadership section")
    read_more_link = models.URLField(blank=True, null=True, help_text="Optional link for the 'Read More' button")

    def __str__(self):
        return self.title


class Feature(models.Model):
    tab_id = models.SlugField(unique=True, help_text="Unique ID for the tab (used in HTML)")
    icon_class = models.CharField(max_length=255, help_text="CSS class for the tab icon")
    tab_title = models.CharField(max_length=255, help_text="Title of the tab")
    heading = models.CharField(max_length=255, help_text="Heading for the feature content")
    italic_description = models.TextField(blank=True, help_text="Italicized description for the feature")
    description = models.TextField(help_text="Main description for the feature")
    image = models.ImageField(upload_to='features/', blank=True, null=True, help_text="Optional image for the feature")

    def __str__(self):
        return self.tab_title

    def get_points_list(self):
        """
        Placeholder method to demonstrate dynamic points. Replace with actual logic if needed.
        """
        return ["Point 1", "Point 2", "Point 3"]


class Service(models.Model):
    icon_class = models.CharField(max_length=255, help_text="CSS class for the service icon")
    icon_color = models.CharField(max_length=7, default="#000000", help_text="Color for the service icon (hex code)")
    title = models.CharField(max_length=255, help_text="Title of the service")
    description = models.TextField(help_text="Description of the service")
    details_url = models.URLField(help_text="URL for more details about the service")

    def __str__(self):
        return self.title
    

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=14, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='users/', default='profile.png')


