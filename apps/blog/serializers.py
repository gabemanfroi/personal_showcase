from rest_framework import serializers

from apps.blog.models import Subject, Article, Blog


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['title', 'tag_color', 'id']


class ArticleSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True)

    class Meta:
        model = Article
        fields = ['subjects', 'title', 'content', 'image', 'created_at', 'id']


class BlogSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True)

    class Meta:
        model = Blog
        fields = ['articles']
