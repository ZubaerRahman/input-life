from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'myblog'

urlpatterns = [
    path('', views.sign_up),
    path('index/', views.index, name='index'),
    path('register/', views.sign_up, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='myblog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='myblog/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('Diary/', views.diary, name='diary'),
    path('Diary/Write', views.add_diary, name='write'),
    url(r'^Diary/Edit/(?P<id>[0-9]+)/$', views.edit_diary, name='edit'),

]
