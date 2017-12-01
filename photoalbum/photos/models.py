from django.db import models
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from urllib.request import urlopen
from json import loads
# Create your models here.


class CollectionManager(models.Manager):

    def create_collection(self, name):
        try:
            Collection.objects.get(collection_name = name)
        except ObjectDoesNotExist:
            try:
                url = settings.STATICFILES_DIRS[0] + 'list/' + name
                print(url)
                response = urlopen(url)
                photo_list = loads(response.read().decode())
            except IOError:
                raise ObjectDoesNotExist
            else:
                collection = self.create(collection_name=name)
                collection.save()
                if photo_list:
                    for p in photo_list:
                        photo = Photo()
                        photo.photo = p
                        photo.collection = collection
                        photo.caption = ''
                        photo.save()
                else:
                    raise ObjectDoesNotExist

class Collection(models.Model):
    collection_name = models.CharField(max_length=50)
    objects = CollectionManager()

    def __str__(self):
        return self.collection_name

    @property
    def thumbnail(self):
            thumb = Photo.objects.filter(collection=self)[0]
            return thumb


class Photo(models.Model):
    photo = models.CharField(max_length=50)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    caption = models.TextField(max_length=1000)

    def __str__(self):
        return self.photo