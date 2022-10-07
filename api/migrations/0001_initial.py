# Generated by Django 4.0 on 2022-08-16 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=256, null=True)),
                ('post', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/blog_image')),
                ('author', models.CharField(blank=True, max_length=256, null=True)),
                ('mins_to_read', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
