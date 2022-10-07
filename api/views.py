from .serializers import *
from rest_framework.decorators import api_view
from .models import *
from rest_framework.response import Response
from django.db.models import Q


@api_view(['GET'])
def get_blog(request):
    blog = BlogModel.objects.all()
    serializer = BlogSerializer(blog , many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_blog_fr(request):
    blog = BlogModel.objects.all()
    serializer = BlogSerializerFR(blog , many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_blog_ru(request):
    blog = BlogModel.objects.all()
    serializer = BlogSerializerRU(blog , many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_post(request , id):
    if request.method == 'GET':
        post = BlogModel.objects.get(id=id)
        serializer = BlogSerializer(post)
        return Response(serializer.data)

@api_view(['GET'])
def get_post_fr(request , id):
    if request.method == 'GET':
        post = BlogModel.objects.get(id=id)
        serializer = BlogSerializerFR(post)
        return Response(serializer.data)

@api_view(['GET'])
def get_post_ru(request , id):
    if request.method == 'GET':
        post = BlogModel.objects.get(id=id)
        serializer = BlogSerializerRU(post)
        return Response(serializer.data)

@api_view(['GET'])
def get_latest_post(request):
    if request.method == 'GET':
        post = BlogModel.objects.latest('id')
        serializer = BlogSerializer(post)
        return Response(serializer.data)

@api_view(['GET'])
def get_latest_post_fr(request):
    if request.method == 'GET':
        post = BlogModel.objects.latest('id')
        serializer = BlogSerializerFR(post)
        return Response(serializer.data)

@api_view(['GET'])
def get_latest_post_ru(request):
    if request.method == 'GET':
        post = BlogModel.objects.latest('id')
        serializer = BlogSerializerRU(post)
        return Response(serializer.data)

@api_view(['GET'])
def get_latest_posts_top(request):
    if request.method == 'GET':
        posts = BlogModel.objects.all().order_by('-id')[:5]
        serializer = BlogSerializer(posts , many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_latest_posts_top_fr(request):
    if request.method == 'GET':
        posts = BlogModel.objects.all().order_by('-id')[:5]
        serializer = BlogSerializerFR(posts , many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_latest_posts_top_ru(request):
    if request.method == 'GET':
        posts = BlogModel.objects.all().order_by('-id')[:5]
        serializer = BlogSerializerRU(posts , many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_latest_posts_bottom(request):
    if request.method == 'GET':
        posts = BlogModel.objects.all().order_by('-id')[5:8]
        serializer = BlogSerializer(posts , many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_latest_posts_bottom_fr(request):
    if request.method == 'GET':
        posts = BlogModel.objects.all().order_by('-id')[5:8]
        serializer = BlogSerializerFR(posts , many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_latest_posts_bottom_ru(request):
    if request.method == 'GET':
        posts = BlogModel.objects.all().order_by('-id')[5:8]
        serializer = BlogSerializerRU(posts , many=True)
        return Response(serializer.data)


@api_view(['GET'])
def random_posts(request):
    if request.method == 'GET':
        post = BlogModel.objects.order_by('?')[:4]
        serializer = BlogSerializer(post , many=True)
        return Response(serializer.data)

@api_view(['GET'])
def random_posts_fr(request):
    if request.method == 'GET':
        post = BlogModel.objects.order_by('?')[:4]
        serializer = BlogSerializerFR(post , many=True)
        return Response(serializer.data)

@api_view(['GET'])
def random_posts_ru(request):
    if request.method == 'GET':
        post = BlogModel.objects.order_by('?')[:4]
        serializer = BlogSerializerRU(post , many=True)
        return Response(serializer.data)

@api_view(['GET'])
def random_post(request):
    if request.method == 'GET':
        post = BlogModel.objects.order_by('?').first()
        serializer = BlogSerializer(post)
        return Response(serializer.data)

@api_view(['GET'])
def random_post_fr(request):
    if request.method == 'GET':
        post = BlogModel.objects.order_by('?').first()
        serializer = BlogSerializerFR(post)
        return Response(serializer.data)

@api_view(['GET'])
def random_post_ru(request):
    if request.method == 'GET':
        post = BlogModel.objects.order_by('?').first()
        serializer = BlogSerializerRU(post)
        return Response(serializer.data)
        
@api_view(['POST'])
def contact_us(request):
    if request.method == 'POST':
        serializer = ContactUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    