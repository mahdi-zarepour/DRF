from django.urls import path
from . import views 


app_name = 'blog'
urlpatterns = [
    path('', views.AllArticle.as_view(), name='all_articles'),
    path('create/', views.ArticleCreate.as_view(), name='article_create'),
    path('delete/<int:pk>', views.ArticleDelete.as_view(), name='article_delete'),
    path('update/<int:pk>', views.ArticleUpdate.as_view(), name='article_update'),
    path('<int:pk>/<slug:slug>/', views.ArticleDetail.as_view(), name='article_detail'),

    # API
    path('api/response_api/', views.response_api),
    path('api/test_serializer/', views.test_serializer),
    path('api/articles/', views.AllArticleApi.as_view()),
    path('api/article/<int:article_id>/', views.ArticleApi.as_view()),
]