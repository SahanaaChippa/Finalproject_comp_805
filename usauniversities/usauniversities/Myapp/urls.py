from django.conf import settings
from django.urls import path  # Import the view function
from . import views
from django.conf.urls.static import static
from .views import home

urlpatterns = [
    # Other URL patterns...
    path('', home, name='home'),
    path('university/', views.universities_list, name='universitie_list'),
    path('universities/<int:university_id>/reviews/', views.university_detail, name='university_reviews'),
    path('review/<int:review_id>/update/', views.review_update, name='review_update'),

]