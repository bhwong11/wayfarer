from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('profile/', views.UserProfile.as_view(), name='profile'),
    path('profile/<int:pk>/', views.ProfileDetail.as_view(), name="profile_detail"),
    path('profile/<int:pk>/update/',
         views.ProfileUpdate.as_view(), name="profile_update"),
    path('accounts/signup/', views.Signup.as_view(), name='signup'),
    path('regerror/', views.HomeError.as_view(), name='reg_error'),
    path('posts/<int:pk>/', views.PostDetails.as_view(), name='post_details')
    # put urls here
]
