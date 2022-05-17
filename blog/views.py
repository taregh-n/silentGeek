from django.shortcuts import redirect, render, get_object_or_404
from .models import Post, Comment
from django.core.paginator import Paginator
from .forms import CommentForm
# Create your views here.

def blog(request):
    all_posts = Post.objects.all()
    paginator = Paginator(all_posts, 8)
    page_num = request.GET.get('page')
    page_posts = paginator.get_page(page_num)
    page_range = paginator.page_range
    params = {
        'page': page_posts,
        'page_range': page_range,
        'page_num': page_num,
    }
    return render(request, 'blog/blog.html', params)


def post_details(request, post_id):
    comment_form = CommentForm()
    post = get_object_or_404(Post, id=post_id)
    params = {
        'post': post,
        'comment_form': comment_form,
    }
    return render(request, 'blog/details.html', params)


def post_comment(request, post_id):
    ref_url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        comment_form = CommentForm(request.POST, request.FILES)
        if comment_form.is_valid():
            data = comment_form.cleaned_data
            parent_id = request.POST.get('parent_id')
            new_comment = Comment.objects.create(
                post_id = post_id,
                name = data['name'],
                # image = data['image'],
                site = data['site'],
                email = data['email'],
                content = data['content'],
            )
            if request.user:
                new_comment.user_id = request.user.id
            if parent_id:
                new_comment.parent_id = int(parent_id)
            new_comment.save()
    return redirect(ref_url)

# def reply_to_comment(request, post_id, comment_id):
#     ref_url = request.META.get('HTTP_REFERER')
#     # comment = Comment.objects.get(id = comment_id)
#     if request.method == 'POST':
#         comment_form = CommentForm(request.POST, request.FILES)
#         if comment_form.is_valid():
#             data = comment_form.cleaned_data
#             new_comment = Comment.objects.create(
#                 post_id = post_id,
#                 user_id = request.user.id,
#                 name = data['name'],
#                 content = data['content'],
#                 parent_id = comment_id,
#             )
#             new_comment.save()
#     return redirect(ref_url)
