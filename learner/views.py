from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth import views
from learner.models import Post
from learner.forms import PostForm
# Login/Logout Practice Using Sessions

class PostListView(ListView):
    model = Post
    template_name = 'learner/post_list.html'
    context_object_name = 'posts'
    
    
    def get_queryset(self):
        return Post.objects.all().order_by('-created_at')
        # return Post.objects.filter(status='published').order_by('-created_at')
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'All Posts'
        return context
    
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'learner/post_detail.html'
    context_object_name = 'post'
    
    def get_object(self):
        slug = self.kwargs.get("slug")
        return get_object_or_404(Post, slug=slug)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.object.title
        return context
    
    
class PostCreateView(CreateView):
    models = Post
    form_class = PostForm
    template_name = 'learner/post_form.html'
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Create new posts"
        return context
    
    
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'learner/post_form.html'
    
    def get_object(self):
        slug = self.kwargs.get("slug")
        return get_object_or_404(Post, slug=slug, author=self.request.user)
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Edit post"
        return context
    
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'learner/post_confirm_delete.html'
    success_url = reverse_lazy()
    
    def get_object(self):
        slug = self.kwargs.get("slug")
        return get_object_or_404(Post, slug=slug, author=self.request.user)
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)
    
    
    

