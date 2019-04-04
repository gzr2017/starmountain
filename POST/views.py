from django.shortcuts import render, get_object_or_404
from .models import Message, Article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import date
from haystack.views import SearchView


class MySearchView(SearchView):
    tag_list = Article.tags.all()
    message_list = Message.objects.order_by('-publish_time')[:3]

    def extra_context(self):  # 重载extra_context来添加额外的context内容
        context = super(MySearchView, self).extra_context()
        context['tag_list'] = self.tag_list
        context['message_list'] = self.message_list
        return context


def index(request):
    article_list_raw = Article.objects.order_by('-publish_time')
    paginator = Paginator(article_list_raw, 5)
    page = request.GET.get('page')
    article_list = paginator.get_page(page)
    tag_list = Article.tags.all()
    message_list = Message.objects.order_by('-publish_time')[:3]
    context = {
        'article_list': article_list,
        'tag_list': tag_list,
        'message_list': message_list
    }
    return render(request, 'index.html', context)

# 文章详情视图


def article_detail(request, id):
    article = Article.objects.get(id=str(id))
    tag_list = Article.tags.all()
    message_list = Message.objects.order_by('-publish_time')[:3]
    context = {
        'article': article,
        'tag_list': tag_list,
        'message_list': message_list
    }
    return render(request, 'article_detail.html', context)


# 标签查询
def article_tag(request, tag_name):
    article_list_raw = Article.objects.filter(
        tags__name=tag_name).order_by('-publish_time')
    paginator = Paginator(article_list_raw, 5)
    page = request.GET.get('page')
    article_list = paginator.get_page(page)
    tag_list = Article.tags.all()
    message_list = Message.objects.order_by('-publish_time')[:3]
    context = {
        'article_list': article_list,
        'tag_list': tag_list,
        'message_list': message_list,
        'tag_name': tag_name
    }
    return render(request, 'index.html', context)


def message(request):
    tag_list = Article.tags.all()
    messagelistraw = Message.objects.order_by('-publish_time')
    paginator = Paginator(messagelistraw, 7)
    page = request.GET.get('page')
    message_list = Message.objects.order_by('-publish_time')[:3]
    messagelist = paginator.get_page(page)
    context = {
        'messagelist': messagelist,
        'tag_list': tag_list,
        'message_list': message_list
    }
    return render(request, 'message.html', context)
