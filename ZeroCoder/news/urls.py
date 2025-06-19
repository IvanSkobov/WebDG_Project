from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='news_home'),
	path('<int:news_id>', views.news_detail, name='news-detail'),
	path('create_news/', views.create_news, name='create_news'),
	# path('news_edit/<int:news_id>', views.news_edit, name='news_edit'),  # Добавьте функцию news_edit в views.py, если потребуется
	# path('news_delete/<int:news_id>', views.news_delete, name='news_delete'),  # Добавьте функцию news_delete в views.py, если потребуется
]