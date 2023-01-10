from django.urls import path
from . import views

urlpatterns = [
    path('joinForm/',views.joinForm),
    path('checkJoin/',views.checkJoin),
    # path('logout/',views.logout),
]