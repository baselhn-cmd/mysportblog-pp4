from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('add_post/', views.AddPost.as_view(), name='add_post'),
    path('<slug:slug>/edit/', views.EditPost.as_view(), name='edit_post'),

    path('post/<slug:slug>/delete/', views.DeletePost.as_view(), name='delete_post'),
    path('<slug:slug>/', views.post_detail, name="post_detail"),
    path('<slug:slug>/edit_comment/<int:comment_id>/', views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>/', views.comment_delete, name='comment_delete'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),

]
