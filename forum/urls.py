from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='forum'),
path('post/<int:pk>/', views.BlogDetailView.as_view(), name='forum_detail'),
path('post/new/', views.BlogCreateView.as_view(), name='post_new'),
]