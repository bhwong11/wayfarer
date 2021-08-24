from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('profile/', views.UserProfile.as_view(), name='profile'),
    path('profileupdate/', views.UpdateProfile.as_view(), name='update_profile'),
    path('profile/<int:pk>/', views.ProfileDetail.as_view(), name="profile_detail"),
    path('profile/<int:pk>/update/',
         views.ProfileUpdate.as_view(), name="profile_update"),
    path('accounts/signup/', views.Signup.as_view(), name='signup'),
    path('regerror/', views.HomeError.as_view(), name='reg_error'),
    path('posts/<int:pk>/', views.PostDetails.as_view(), name='post_details'),
    path('posts/create/', views.PostCreate.as_view(), name='post_create'),
    path('posts/<int:pk>/update/', views.PostUpdate.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),
    path('cities/<int:pk>/', views.CityDetail.as_view(), name='cities_detail'),
    path('cities/<slug:slug>/', views.CityDetailView.as_view(), name='city_detail'),
    path('comments/create/', views.CommentCreate.as_view(), name='comment_create'),
    path('comments/<int:pk>/update/',
         views.CommentUpdate.as_view(), name='comment_update'),
    path('comments/<int:pk>/delete/',
         views.CommentDelete.as_view(), name='comment_delete'),
    # put urls here
]
