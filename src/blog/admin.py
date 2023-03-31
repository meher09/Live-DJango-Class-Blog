from django.contrib import admin
from .models import *
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'status')
    list_filter = ('category','status')



admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Post, PostAdmin)