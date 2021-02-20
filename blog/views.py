from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .models import Post #ポストのモデルをインポートする
from .forms import PostForm
#ポストフォームクラスをインポート
from django.shortcuts import redirect
#

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})
    #request:クライアントからもらった情報が詰まっている

def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        #入力が終わった後の処理
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #著者が定義されていないのでフォームは保存するがPostモデルは保存しない
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
            #投稿の詳細へリダイレクト
    else:
        #空白の入力フォームを返す
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})