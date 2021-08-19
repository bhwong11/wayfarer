from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('profile/',views.Profile.as_view(),name='profile'),
    path('profile/<int:pk>/', views.ProfileDetail.as_view(), name="profile_detail")
	# put urls here
]
