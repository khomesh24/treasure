from . import views
from django.urls import path

urlpatterns=[
    path('', views.index,name='index'),
    path('post_url/', views.post_treasure,name='post_treasure'),
    path('<int:treasure_id>/',views.detail,name = 'detail'),
]