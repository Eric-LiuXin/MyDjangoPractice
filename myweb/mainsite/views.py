from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from .models import Post
from datetime import datetime
from django.template.loader import get_template

def homepage(request):
    posts = Post.objects.all()
    posts_list = ["No.{}:".format(str(count)) + str(post.title) for count,post in enumerate(posts)]
    template = get_template('index.html')
    now = datetime.now()
    html = template.render(locals())

    return HttpResponse(html)