from django.shortcuts import render, get_object_or_404

from .models import Category, Topic

def categories(request):
    return{
        'categories':Category.objects.all()
    }

def all_topics(request):
    topics = Topic.objects.all()
    return render(request, 'csbok/home.html', {'topics':topics})

def topic_detail(request, slug):
    topic = get_object_or_404(Topic, slug=slug)
    return render(request, 'csbok/topics/detail.html', {'topic' : topic})

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    topics = Topic.objects.filter(category=category)
    return render(request,'csbok/topics/category.html', {'category' : category, 'topics' : topics})