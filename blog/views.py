from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import PostCreateForm
from .models import Post
# Create your views here.

class BlogListView(View):
    
    def get(self, request, *args, **kwargs):
        ctx: dict = {

        }
        return render(request, 'blog_list.html', ctx)


class BlogCreateView(View):
    def get(self, request, *args, **kwargs):
        form = PostCreateForm()
        ctx: dict = {
            'form' : form
        }
        return render(request, 'blog_create.html', ctx)


    def post(self, request, *args, **kwargs):

        if (request.method == 'POST'):
            form = PostCreateForm(request.POST)

            if (form.is_valid()):
                title = form.cleaned_data.get('title')
                content = form.cleaned_data.get('content')

                p, create = Post.objects.get_or_create(title=title, content=content)
                p.save()
                return redirect('blog:home')

        ctx: dict = {

        }
        return render(request, 'blog_create.html', ctx)