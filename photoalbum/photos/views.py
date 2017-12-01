from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Collection, Photo
# Create your views here.


class CollectionsListView(ListView):
    model = Collection
    ordering = 'collection_name'
    context_object_name = 'collections'
    template_name = 'photos/index.html'



class CollectionListView(ListView):
    model = Photo
    ordering = 'id'
    context_object_name = 'image_list'
    template_name = 'photos/collection.html'

    def get_queryset(self):
        collection = Collection.objects.get(collection_name=self.kwargs['collection_name'])
        image_list = Photo.objects.filter(collection=collection)
        return image_list

class PhotoDetailView(DetailView):
    model = Photo
