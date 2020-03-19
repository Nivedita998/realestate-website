from django.contrib import admin
from .models import Post ,Contact,ContactAgent,Author,Blogpost_details
# Register your models here.
admin.site.register(Post)
admin.site.register(Contact)
admin.site.register(ContactAgent)
admin.site.register(Author)
admin.site.register(Blogpost_details)
