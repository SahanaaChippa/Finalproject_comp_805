import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import University, Review, SavedUniversity
from .forms import ReviewForm
from django.http import JsonResponse

def home(request):
    picture_path = r'usauniversity\usauniversity\static\images\image.jpg'  # Update this with the actual path to your picture
    return render(request, 'home.html', {r'usauniversity\usauniversity\static\images\image.jpg': picture_path})