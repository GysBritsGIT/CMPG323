'''Photoapp URL patterns'''

from django.urls import path, include, re_path, reverse_lazy

from .views import (
    PhotoListView,
    PhotoTagListView,
    PhotoDetailView,
    PhotoCreateView,
    PhotoUpdateView,
    PhotoDeleteView,
    SearchResultsView,##
)

app_name = 'photo'

urlpatterns = [
    path('', PhotoListView.as_view(), name='list'),

    path('tag/<slug:tag>/', PhotoTagListView.as_view(), name='tag'),

    path('photo/<int:pk>/', PhotoDetailView.as_view(), name='detail'),

    path('photo/create/', PhotoCreateView.as_view(), name='create'),

    path('photo/<int:pk>/update/', PhotoUpdateView.as_view(), name='update'),

    path('photo/<int:pk>/delete/', PhotoDeleteView.as_view(), name='delete'),

    path('search_results/', SearchResultsView.as_view(), name='search_results'),##

    #url(r'^tags/', include('taggit_templatetags2.urls')),

]
