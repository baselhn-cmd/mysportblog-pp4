from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Permission
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm, PostForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog/index.html"
    paginate_by = 6


def post_detail(request, slug):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(request, messages.SUCCESS,
                                'Comment submitted and awaiting approval')

    comment_form = CommentForm()
    return render(request, "blog/post_detail.html", {
        "post": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
    })


def comment_edit(request, slug, comment_id):
    if request.method == "POST":
        post = get_object_or_404(Post, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                    'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    post = get_object_or_404(Post, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                                'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class AddPost(LoginRequiredMixin, generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'
    login_url = 'account_login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditPost(LoginRequiredMixin, generic.UpdateView):
    model = Post
    template_name = 'blog/edit_post.html'
    success_url = reverse_lazy('home')
    login_url = 'account_login'
    fields = (
        'title', 'slug', 'excerpt', 'content'
    )

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Post, slug=slug)


@login_required
def delete_post(request, slug, *args, **kwargs):
    post = get_object_or_404(Post, slug=slug)
    if not request.user.is_superuser and request.user != post.blogger:
        messages.error(request,
                        'Sorry, only admin or the post owner can do that.')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        post.delete()
        messages.success(request, 'Post deleted!')
        return redirect(reverse('home'))
    return render(request, 'blog/delete_post.html', {'post': post})


class PostLike(LoginRequiredMixin, View):
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=self.kwargs.get('slug'))
        if post.likes.all().filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


@login_required
@permission_required('blog.add_post', raise_exception=True)
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.blogger = request.user
            post.save()
            messages.add_message(request, messages.SUCCESS,
                                    'Post added successfully!')
            return HttpResponseRedirect(reverse('home'))
    else:
        form = PostForm()

    return render(request, 'blog/add_post.html', {'form': form})


def assign_add_post_permission(user):
    permission = Permission.objects.get(codename='add_post')
    user.user_permissions.add(permission)


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)
