from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy
# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = Post 
    template_name = 'article-detail.html'

class AddPostView(CreateView):
    model = Post 
    form_class = PostForm
    template_name = 'add_post.html'

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = {'title'}

class DeletePostView(DeleteView):
    model = Post 
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('home')

class UpdateCommentView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'update_comment.html'
    # def form_valid(self, form):
    #     form.instance.post_id = self.kwargs['pk']
    #     return super().form_valid(form)
    success_url = reverse_lazy('home')

class RemoveCommentView(DeleteView):
    model = Comment
    template_name = 'delete_comment.html'
    success_url = reverse_lazy('home')
