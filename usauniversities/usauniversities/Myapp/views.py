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

def universities_list(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        # Fetch universities data from the external API
        url = 'http://universities.hipolabs.com/search?country=United+States'
        response = requests.get(url)
        universities_data = response.json()

        # Iterate over the universities data and save them
        for university_data in universities_data:
            name = university_data.get('name', '')
            country = university_data.get('country', '')
            website = university_data.get('web_pages', [''])[0]

            # Check if a university with the same name already exists
            existing_university = University.objects.filter(name=name).exists()

            if not existing_university:
                # Create a University instance and save it if it doesn't exist
                University.objects.create(name=name, country=country, website=website)

        # Fetch all saved universities
        universities = University.objects.all()
        saved_universities = SavedUniversity.objects.filter(user=request.user)
        saved_university_ids = saved_universities.values_list('university_id', flat=True)

        # Prepare data to send back to the client
        universities_list = []
        for university in universities:
            universities_list.append({
                'id': university.id,
                'name': university.name,
                'country': university.country,
                'website': university.website
            })

        response_data = {
            'universities': universities_list,
            'saved_university_ids': list(saved_university_ids)
        }

        return JsonResponse(response_data)

    # Render the template for non-AJAX requests
    universities = University.objects.all()
    saved_universities = SavedUniversity.objects.filter(user=request.user)
    saved_university_ids = saved_universities.values_list('university_id', flat=True)
    return render(request, 'myt/university_list.html', {'universities': universities, 'saved_universities': saved_universities, 'saved_university_ids': saved_university_ids})

@login_required
def university_detail(request, university_id):
    university = get_object_or_404(University, pk=university_id)
    reviews = Review.objects.filter(university=university)
    review_form = ReviewForm()

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.university = university
            review.save()
            return redirect('university_reviews', university_id=university_id)

    return render(request, 'myt/university_reviews.html', {'university': university, 'reviews': reviews, 'review_form': review_form})

@login_required
def review_update(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    form = ReviewForm(instance=review)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('university_reviews', university_id=review.university.pk)

    return render(request, 'myt/review.html', {'form': form})

@login_required
def delete_review(request):
    if request.method == 'POST':
        review_id = request.POST.get('review_id')
        review = get_object_or_404(Review, pk=review_id)

        # Check if the review belongs to the current user
        if review.user == request.user:
            review.delete()
