from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import truncatechars
from django.urls import reverse

class Category(models.Model):
    name = models.CharField( max_length=256, db_index=True)
    slug = models.SlugField( max_length=256, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('csbok:category_list', args=[self.slug])
    
    def __str__(self):
        return self.name
    
class Topic(models.Model):
    category = models.ForeignKey(Category, related_name='topic',on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topic_creator')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='B.Bhattarai')
    body = models.TextField(blank=False)
    media = models.ImageField(upload_to='image/')
    references = models.TextField(blank=False)
    slug = models.SlugField( max_length=256, unique=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    @property
    def short_body(self):
        return truncatechars(self.body, 50)

    class Meta:
        verbose_name_plural = 'Topics'
        ordering = ('-updated',)
    
    def get_absolute_url(self):
        return reverse('csbok:topic_detail', args=[self.slug])

    def __str__(self):
        return self.title