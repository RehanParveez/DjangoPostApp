from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login, logout
from django.views import View
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import views
from django.utils.text import slugify
from django.utils import timezone

from learner.models import Post
from learner.forms import PostForm, RegisterForm


         
class RegisterView(View):
    template_name = 'registration/register.html'
    
    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! You can login now")
            return redirect('login')
        return render(request, self.template_name, {'form': form})


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
        return get_object_or_404(Post, slug=self.kwargs.get("slug"))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.object.title
        return context
    
    
class PostCreateView(CreateView):
    model = Post
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
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        timestamp = timezone.now().strftime("%Y%m%d%H%M%S")
        form.instance.slug = slugify(form.instance.title) + "-" + timestamp
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('post_list')

    
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'learner/post_form.html'
    
    def get_object(self):
        return get_object_or_404(Post, slug=self.kwargs.get("slug"), author=self.request.user)
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Edit post"
        return context
    
    def form_valid(self, form):
        post = form.save(commit=False)
        
        if "title" in form.changed_data:
            timestamp = timezone.now().strftime("%Y%m%d%H%M%S")
            post.slug = slugify(post.title) + "-" + timestamp
        
        post.save()
        return redirect('post_list')

    def get_success_url(self):
        return reverse_lazy('post_list')

    
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'learner/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')
    
    def get_object(self):
        return get_object_or_404(Post, slug=self.kwargs.get("slug"), author=self.request.user)
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

    
    

