from django.urls import path
from .views import index, top_sellers, me_post, advertisement_detail

urlpatterns = [
    path("", index, name='main-page'),
    path("top-sellers/", top_sellers, name='top-sellers'),
    path("advertisement-post/", me_post, name='me_post'),
    path("advertisement/<int:pk>", advertisement_detail, name='adv-detail')
]
