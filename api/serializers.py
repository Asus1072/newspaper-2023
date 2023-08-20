from django.contrib.auth.models import User, Group
from rest_framework import serializers
from newspaper.models import Comment, Contact, Newsletter, Tag, Category, Post

# ORM => oBJECT rELATIONSHIP mAOOING
# Post.objects.all => Select * FORM posts Queryset[<Post 1>, <Post 2>, <Post 3>
# #Post.object.created(...)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups', 'first_name','is_active','is_superuser',]


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
                'id',
                'title',
                'content',
                'featured_image',
                'views_count',
                'status',
                'published_at',
                'author',
                'tag',
                'category',
        ]
        extra_kwargs = {
            "author": {"read_only": True},
            "views_count": {"read_only": True},
            "published_at": {"read_only": True},
            }
        def validate(self, data):
            data['author'] = self.context["request"].user
            return data


from rest_framework import serializers

class PostPublishSerializer(serializers.Serializer):
    post = serializers.IntegerField()


class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields ="__all__"


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields ="__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Comment
        fields ="__all__"