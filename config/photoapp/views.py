'''Photo app generic views'''

import django
from django.http import request
from django.shortcuts import get_object_or_404

from django.core.exceptions import PermissionDenied

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.urls import reverse_lazy

from config.settings import DATABASES, TAGGIT_CASE_INSENSITIVE

from .models import Photo

from .models import filter_by_title

from django.db.models import Q

from django.db.models import QuerySet

from rest_framework import filters

from django.shortcuts import render, redirect

class PhotoListView(ListView):
    
    model = Photo     

    template_name = 'photoapp/list.html'

    context_object_name = 'photos'


class PhotoTagListView(PhotoListView):
    
    template_name = 'photoapp/taglist.html'
    
    # Custom function
    def get_tag(self):
        return self.kwargs.get('tag')

    def get_queryset(self):
        return self.model.objects.filter(tags__slug=self.get_tag())
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag"] = self.get_tag()
        return context
     

class PhotoDetailView(DetailView):

    model = Photo

    template_name = 'photoapp/detail.html'

    context_object_name = 'photo'


class PhotoCreateView(LoginRequiredMixin, CreateView):

    model = Photo
    
    fields = ['title','geolocation', 'description', 'image', 'tags']

    template_name = 'photoapp/create.html'
    
    success_url = reverse_lazy('photo:list')

    def form_valid(self, form):

        form.instance.submitter = self.request.user
        
        return super().form_valid(form)

class UserIsSubmitter(UserPassesTestMixin):

    # Custom method
    def get_photo(self):
        return get_object_or_404(Photo, pk=self.kwargs.get('pk'))
    
    def test_func(self):
        
        if self.request.user.is_authenticated:
            return self.request.user == self.get_photo().submitter
        else:
            raise PermissionDenied('Access denied')

class PhotoUpdateView(UserIsSubmitter, UpdateView):
    
    template_name = 'photoapp/update.html'

    model = Photo

    fields = ['title','geolocation', 'description', 'tags']
    
    success_url = reverse_lazy('photo:list')

class PhotoDeleteView(UserIsSubmitter, DeleteView):
    
    template_name = 'photoapp/delete.html'

    model = Photo

    success_url = reverse_lazy('photo:list')

#########

class SearchResultsView(PhotoListView):
    
    template_name = 'photoapp/search_results.html'

    model = Photo

    success_url = reverse_lazy('photo:search_result')
    
    def SearchResultsView(request):
        if 'q' in request.GET and request.GET['q']:
            query = request.GET.get('q', '')
            object_list = Photo.objects.filter(Q(tags__slug__icontains = query))
            #object_list = Photo.filter_by_title(Photo.title)
            message = f"{query}"
            print(object_list)
            return render(request, 'search_results', {"message": message, "photo": object_list})
        else:
            message = "Please enter tag number"
            return render(request, 'search_results', {"message": message})
