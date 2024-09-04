from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleUpdateView,
    ArticleDeleteView,
    ArticleCreateView,
    UserArticleList,
    article_like,
)

urlpatterns = [
    path("", ArticleListView.as_view(), name="article_list"),
    # path("", ArticleListView.as_view(), name="user_article_list"),
    path("my-articles/", UserArticleList.as_view(), name="user_articles"),
    path("<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
    path("<int:pk>/edit/", ArticleUpdateView.as_view(), name="article_edit"),
    path("<int:pk>/delete/", ArticleDeleteView.as_view(), name="article_delete"),
    path("create/", ArticleCreateView.as_view(), name="article_new"),
    path("article-like/<int:pk>", article_like, name="article_like"),
]
