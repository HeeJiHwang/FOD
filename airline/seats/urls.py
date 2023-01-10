from django.urls import path, include
from . import views


urlpatterns = [
    path('seat/', views.seat),
    path('seatresult/', views.seatresult)
]