from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Query

def home(request):
    context = {
        'queries': Query.objects.all()
    }

    return render(request, 'blog/home.html', context)

class QueryListView(ListView):
    model = Query
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'queries'
    ordering = ['-date_posted']

    for query in Query.objects.all():
        date_c = query.created
        date_e = query.expiry
        #if(query.frequency == 'hrs'):
            

class QueryDetailView(DetailView):
    model = Query

class QueryCreateView(LoginRequiredMixin, CreateView):
    model = Query
    fields = ['Application', 'Notification', 'created', 'expiry', 'frequency', 'nos']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class QueryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Query
    fields = ['Application', 'Notification', 'created', 'expiry', 'frequency', 'nos']

    def form_valid(self, form):
        form.instance.creator = self.request.user

        return super().form_valid(form)

    def test_func(self):
        query = self.get_object()
        if self.request.user == query.creator:
            return True
        return False

class QueryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Query
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.creator:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
