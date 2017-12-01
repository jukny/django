from django.conf.urls import url
from .views import CollectionsListView, CollectionListView, PhotoDetailView


urlpatterns = [
    url(r'^$', CollectionsListView.as_view(), name='collections'),
    url(r'^(?P<collection_name>[A-Za-z]+)/$', CollectionListView.as_view(), name='collection'),
    url(r'^(?P<collection_name>[A-Za-z]+)/(?P<pk>)/$', PhotoDetailView.as_view(), name='photo')
]