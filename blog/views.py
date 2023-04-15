from django.shortcuts import render
from .models import Post
from  django.contrib.auth.models import User
from  django.utils import timezone
from  django.http import HttpResponse
def post_list(request):
    return render(request, 'blog/post_list.html', {})
def post100(request):
    me = User.objects.get(username='sajawd')
    for i in range(100):
        now = timezone.now()
        title = f'title{i}'
        text = f'text{i}'
        Post.objects.create(author=me,title=title,text=text).publish()
    return HttpResponse('100 post created')

# Create your views here.
