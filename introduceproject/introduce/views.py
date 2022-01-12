from django.shortcuts import get_object_or_404, render

from .models import Post, Test


def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'introduce/index.html', context={'post_list': post_list})
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'introduce/detail.html', context={'post': post})
    img = Test.objects.all()
    return render(request, 'introduce/index.html', {'img': img})

# Create your views here.
