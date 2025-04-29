from django.contrib import admin

# Register your models here.
from .models import Profile, Skill, Experience,Book, Project, SocialLink , Blogs

admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Project)
admin.site.register(SocialLink)
admin.site.register(Blogs)
admin.site.register(Book)