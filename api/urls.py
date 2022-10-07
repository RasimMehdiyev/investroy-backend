from django.urls import path
from .views import *


urlpatterns = [
    path('en/posts/', get_blog),
    path('fr/posts/', get_blog_fr),
    path('ru/posts/', get_blog_ru),
    path('en/post/<int:id>/', get_post),
    path('fr/post/<int:id>/', get_post_fr),
    path('ru/post/<int:id>/', get_post_ru),
    path('en/latest_post/', get_latest_post),
    path('fr/latest_post/', get_latest_post_fr),
    path('ru/latest_post/', get_latest_post_ru),
    path('en/latest_posts_bottom/', get_latest_posts_bottom),
    path('fr/latest_posts_bottom/', get_latest_posts_bottom_fr),
    path('ru/latest_posts_bottom/', get_latest_posts_bottom_ru),
    path('en/latest_posts_top/', get_latest_posts_top),
    path('fr/latest_posts_top/', get_latest_posts_top_fr),
    path('ru/latest_posts_top/', get_latest_posts_top_ru),
    path('en/random_posts/', random_posts),
    path('fr/random_posts/', random_posts_fr),
    path('ru/random_posts/', random_posts_ru),
    path('en/random_post/', random_post),
    path('fr/random_post/', random_post_fr),
    path('ru/random_post/', random_post_ru),
    path('contact_us/', contact_us),
]