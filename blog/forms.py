from django import forms

from .models import Post
#models.pyからPostクラスをインポート

class PostForm(forms.ModelForm):
#djangoデフォルトのformsからModelFormを使いますよって意味

    class Meta:
    #Djangoにフォームを作るときにどのフォームを使うのか伝える
        model = Post
    #モデルはポストモデルを使いますよ
        fields = ('title', 'text',)
    #入力するのはタイトルとテキストですよ
    #authorは自分
    #created_dateは自動的に追加される