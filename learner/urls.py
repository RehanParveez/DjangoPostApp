from django.urls import path
from learner.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('postdetail/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('postcreate/', PostCreateView.as_view(), name='post_create'),
    path('postupdate/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('postdelete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
]

