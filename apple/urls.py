from django.urls import path
from .views import Steve, Jobs

urlpatterns = [
    path('', Steve.as_view(), name='steve'),
    path('CEO/', Jobs.as_view(), name='jobs'),
    
]