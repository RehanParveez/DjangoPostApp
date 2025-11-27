from django.urls import path
from learner.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, RegisterView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('postregister/', RegisterView.as_view(), name='register'),
    path('postdetail/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('postcreate/', PostCreateView.as_view(), name='post_create'),
    path('postupdate/<slug:slug>/', PostUpdateView.as_view(), name='post_update'),
    path('postdelete/<slug:slug>/', PostDeleteView.as_view(), name='post_delete'),
]

