from django.urls import path
from . import blog_views


app_name = 'blog'

urlpatterns = [
    path('', blog_views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', blog_views.detail, name='detail'),
]
