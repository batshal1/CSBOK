from django.contrib import admin

from .models import Category, Topic

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['title','category',]
    list_filter = ['category']
    prepopulated_fields = {'slug':('title',)}
