from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import os

# Custom manager for the CustomUser model
class CustomUserManager(BaseUserManager):
    """
    Custom manager for CustomUser model to handle user creation.
    """
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, email, password, **extra_fields)

# Custom User model extending AbstractUser
class CustomUser(AbstractUser):
    """
    Custom user model extending AbstractUser with additional fields.
    """
    profile_picture = models.ImageField(
        upload_to='profile_pictures/',  # Folder where profile pictures are stored
        blank=True,  # Allow blank
        null=True,   # Allow null value
        default='profile_pictures/default.png'  # Default image if none is provided
    )
    bio = models.TextField(blank=True, null=True)  # Optional biography field

    # Custom manager for handling user creation
    objects = CustomUserManager()

    def __str__(self):
        return self.username

    @property
    def profile_picture_url(self):
        """
        Returns the profile picture URL or a default placeholder if not provided.
        """
        if self.profile_picture:
            return self.profile_picture.url
        return '/media/profile_pictures/default.png'  # Default path if no image is set

# Sunday School Lesson model
class SundaySchoolLesson(models.Model):
    """
    Model for storing Sunday School lessons.
    """
    title = models.CharField(max_length=255)  # Title of the lesson
    description = models.TextField()  # Description of the lesson
    date = models.DateField()  # Date of the lesson

    # Optionally link to an image for the lesson
    image = models.ImageField(upload_to='sunday_school_images/', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']  # Order lessons by date, most recent first
