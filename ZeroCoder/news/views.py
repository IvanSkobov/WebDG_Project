from django.shortcuts import render, get_object_or_404, redirect
from .models import News_post
from .forms import NewsForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def home(request):
	news = News_post.objects.all()
	return render(request, 'news/news.html', {'news': news})

def news_detail(request, news_id):
	news = get_object_or_404(News_post, id=news_id)
	return render(request, 'news/news_detail.html', {'news': news})

def create_news(request):
	edit_id = request.GET.get('edit')
	delete_id = request.GET.get('delete')
	if delete_id:
		News_post.objects.filter(id=delete_id).delete()
		return HttpResponseRedirect(reverse('create_news'))

	if edit_id:
		instance = get_object_or_404(News_post, id=edit_id)
	else:
		instance = None

	if request.method == 'POST':
		if edit_id:
			form = NewsForm(request.POST, instance=instance)
		else:
			form = NewsForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('create_news'))
	else:
		form = NewsForm(instance=instance)

	news = News_post.objects.all().order_by('-pub_date')
	return render(request, 'news/create_news.html', {'form': form, 'news': news, 'edit_id': edit_id})