from django.db import models

# Create your models here.
class BlogModel(models.Model):
    title = models.CharField(max_length=256 , blank=True , null=True)
    post = models.TextField(blank=True , null=True)
    created_at = models.DateTimeField(auto_now_add=True , blank=True , null=True)
    updated_at = models.DateTimeField(auto_now=True , blank=True , null=True)
    image = models.ImageField(upload_to='media/blog_image' , blank=True , null=True)
    author = models.CharField(max_length=256 , blank=True , null=True)
    mins_to_read = models.IntegerField(blank=True , null=True)
    title_fr = models.CharField(max_length=256 , blank=True , null=True)
    post_fr = models.TextField(blank=True , null=True)
    title_ru = models.CharField(max_length=256 , blank=True , null=True)
    post_ru = models.TextField(blank=True , null=True)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created_at',)


class ContactUs(models.Model):
    name = models.CharField(max_length=256 , blank=True , null=True)
    email = models.EmailField(max_length=256 , blank=True , null=True)
    message = models.TextField(blank=True , null=True)
    created_at = models.DateTimeField(auto_now_add=True , blank=True , null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created_at',)