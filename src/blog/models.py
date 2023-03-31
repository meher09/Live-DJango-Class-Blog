from django.db import models
from django.utils.text import slugify
from taggit.managers import TaggableManager



# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(max_length=255)
    
    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True,blank=True,null=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT,blank=True,null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    


class Post(models.Model):
    STATUS = (
        ('draft', 'Draft'),
        ('publish', 'Published')
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True,null=True, unique=True)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()
    status = models.CharField(max_length=10, choices=STATUS, default='draft')
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['created']
        verbose_name_plural = "My Posts"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    