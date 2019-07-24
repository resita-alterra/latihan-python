from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('author/',views.author, name='author'),
    path('mentor/', views.mentor, name='mentor'),
    path('mentee/', views.mentee, name='mentee'),
    path('inputmentor/', views.inputmentor),
    path('inputmentee/', views.inputmentee),
    path('blog/', views.blog, name='blog'),
    path('inputblog', views.inputblog),
    path('blog/<int:id_blog>', views.masukblog, name='masukblog'),
]