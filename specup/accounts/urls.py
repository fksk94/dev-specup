from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path('index/', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
    path('password/', views.user_password, name='user_password'),
    path('profile/<name>/', views.profile, name='profile'),
    path('profile/<int:pk>/follow/', views.follow, name='follow'),
]