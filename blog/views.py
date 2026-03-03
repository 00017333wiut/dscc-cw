from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Post, Category, Tag


def post_list(request):
    posts = Post.objects.filter(published=True)
    categories = Category.objects.all()
    return render(request, "blog/post_list.html", {
        "posts": posts,
        "categories": categories
    })


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, published=True)
    return render(request, "blog/post_detail.html", {"post": post})


def category_posts(request, pk):
    category = get_object_or_404(Category, pk=pk)
    posts = category.posts.filter(published=True)
    return render(
        request,
        "blog/category_posts.html",
        {"category": category, "posts": posts}
    )
def category_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            category = Category.objects.create(name=name)
            return JsonResponse({'id': category.pk, 'name': category.name})
    return JsonResponse({'error': 'Invalid request'}, status=400)

# CRUD
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content", "category", "tags", "published"]
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("post_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content", "category", "tags", "published"]
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("post_list")

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("post_list")

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

