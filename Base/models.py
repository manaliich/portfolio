from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='profile/', blank=True, null=True)
    email = models.EmailField()
    location = models.CharField(max_length=100)
    resume = models.FileField(upload_to='resume/', blank=True, null=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=50)
    level = models.CharField(max_length=50)  

    def __str__(self):
        return self.name


class Experience(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.position} at {self.company}"


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title


class SocialLink(models.Model):
    platform = models.CharField(max_length=50)  
    url = models.URLField()

    def __str__(self):
        return self.platform
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
class Blogs(models.Model):
    category = models.CharField(max_length=100)  # e.g. "Tools for Thought"
    title = models.CharField(max_length=300)     # e.g. "How can we develop transformative tools for thought?"
    link = models.URLField()                     # e.g. "https://medium.com/..."

    def __str__(self):
        return f"{self.category} - {self.title}"

# models.py
from django.db import models
from django.utils.text import slugify

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    summary = models.TextField()
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
