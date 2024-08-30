from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('add_post/', views.AddPost.as_view(), name='add_post'),
    
    # Update to use <slug:slug> for edit and delete post paths to maintain consistency
    path('post/<slug:slug>/edit/', views.EditPost.as_view(), name='edit_post'),
    path('post/<slug:slug>/delete/', views.DeletePost.as_view(), name='delete_post'),
    
    # Detail view for individual posts using slug
    path('<slug:slug>/', views.post_detail, name="post_detail"),
    
    # Edit and delete comment paths using slug for the post and id for the comment
    path('<slug:slug>/edit_comment/<int:comment_id>/', views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>/', views.comment_delete, name='comment_delete'),
    
    # Like post path using slug
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
]
