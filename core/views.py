from django.views.generic import View
from django.shortcuts import redirect, render


def index_view(request):
    return redirect('/home')


class HomeView(View):
    def get(self, request, *args, **kwargs):
        ctx: dict = {}

        return render(request, 'index.html', ctx)