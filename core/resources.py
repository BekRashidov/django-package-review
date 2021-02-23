from tastypie.resources import ModelResource
from .models import Post


class PostResource(ModelResource):
    class Meta:
        queryset = Post.objects.all()
        resource_name = 'post'


post_resources = PostResource()
