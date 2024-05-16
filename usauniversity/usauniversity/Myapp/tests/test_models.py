from django.test import TestCase
from django.contrib.auth import get_user_model
from Myapp.models import University, Review, SavedUniversity

# Get the user model
User = get_user_model()

class UniversityModelTest(TestCase):
    def setUp(self):
        self.university = University.objects.create(
            name="Test University",
            country="United States",
            website="http://www.testuniversity.com"
        )

    def test_university_creation(self):
        self.assertEqual(self.university.name, "Test University")
        self.assertEqual(self.university.country, "United States")
        self.assertEqual(self.university.website, "http://www.testuniversity.com")

class ReviewModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.university = University.objects.create(
            name="Test University",
            country="United States",
            website="http://www.testuniversity.com"
        )
        self.review = Review.objects.create(
            user=self.user,
            university=self.university,
            content="Great university!",
            rating=5
        )

    def test_review_creation(self):
        self.assertEqual(self.review.user.username, "testuser")
        self.assertEqual(self.review.university.name, "Test University")
        self.assertEqual(self.review.content, "Great university!")
        self.assertEqual(self.review.rating, 5)

class SavedUniversityModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.university = University.objects.create(
            name="Test University",
            country="United States",
            website="http://www.testuniversity.com"
        )
        self.saved_university = SavedUniversity.objects.create(
            user=self.user,
            university=self.university
        )

    def test_saved_university_creation(self):
        self.assertEqual(self.saved_university.user.username, "testuser")
        self.assertEqual(self.saved_university.university.name, "Test University")
