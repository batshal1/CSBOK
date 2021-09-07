from csbok.models import Category
from django.urls import path

from . import views

app_name = 'csbok'

urlpatterns = [
    path('', views.all_topics, name='all_topics'),
    path('topic/<slug:slug>/', views.topic_detail, name='topic_detail'),
    path('category/<slug:category_slug>/',views.category_list, name='category_list')
]
