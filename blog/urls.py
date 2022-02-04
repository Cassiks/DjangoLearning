from django.urls import path
from blog.views import index , Contact

urlpatterns = [
    path('', index),
    path('index', index),
    path('home', index),
    path('iletişim', Contact),
]