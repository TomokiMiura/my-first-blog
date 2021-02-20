from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # /以降がないURLなら投稿リストを表示する
    path('post/<int:pk>/', views.post_detail, name='post_detail'), 
    #pkはプライマリーキー。post/数字なら投稿の詳細を表示する
]