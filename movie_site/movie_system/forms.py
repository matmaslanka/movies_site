from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError  # it checks that email is unique

from .models import Review, Movies, Genre, Director


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("A user with this email already exists.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class ReviewForm(forms.ModelForm):
    RATING_CHOICES = [
        (1, '1 - Very bad!'),
        (2, '2 - Bad!'),
        (3, '3 - Nothing special'),
        (4, '4 - Good!'),
        (5, '5 - Amazing!')
    ]

    rating = forms.ChoiceField(choices=RATING_CHOICES, label="Your rate (from 1 to 5):")

    class Meta:
        model = Review
        fields = ["rating", "review_text"]
        labels = {
            "review_text": "Your review:"
        }


class AddMovieForm(forms.ModelForm):
    RATING_CHOICES = [
        (1, '1 - Very bad!'),
        (2, '2 - Bad!'),
        (3, '3 - Nothing special'),
        (4, '4 - Good!'),
        (5, '5 - Amazing!')
    ]

    rating = forms.ChoiceField(choices=RATING_CHOICES, label="Your rate (from 1 to 5):")

    class Meta:
        model = Movies
        exclude = ["slug"]
        labels = {
            "title": "Title",
            "release_date": "Release Date (e.g. 1999-12-31)",
            "duration": "Duration (e.g. 03:59:00 (please input :00 seconds))",
            "rating": "Your rate (from 1 to 5)",
            "poster_image": "Please add poster image",
            "trailer_URL": "Trailer URL",
            "synopsis": "Synopsis",
            "genre": "Genre",
            "director": "Director",
        }


class AddGenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        exclude = ["slug"]
        labels = {
            "name": "Name Of Genre",
        }


class AddDirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        exclude = ["slug"]
        labels = {
            "name": "Name (First Last)",
            "date_of_birth": "Date Of Birth",
            "biography": "Biography",
        }
