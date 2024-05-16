from django.contrib import admin
from .models import University
from .models import Review

# Register the University model with the admin site
@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'website') 

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['content', 'user', 'university', 'rating']  # Add 'content' to display in the admin list view

admin.site.register(Review, ReviewAdmin)