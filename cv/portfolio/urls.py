from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('portfolio_detail', portfolio_detail),
    path('blog_detail/<int:id>', blog_detail),  
]
