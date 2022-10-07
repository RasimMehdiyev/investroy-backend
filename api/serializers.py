from timeit import default_timer
from rest_framework import serializers
from .models import *

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = ['id','title','post','created_at','updated_at','image','author','mins_to_read']

class BlogSerializerFR(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = ['id','title_fr' , 'post_fr' , 'image' , 'created_at' ,'updated_at', 'author' , 'mins_to_read']

class BlogSerializerRU(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = ['id','title_ru' , 'post_ru' , 'image' , 'created_at' ,'updated_at', 'author' , 'mins_to_read']

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'