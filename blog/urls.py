from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # path('detail/<int:pk>', views.blog_view, name='post_url'),
    # path('detail/<str:title>', views.blog_view, name='post_url'),
    path('detail/<slug:slug>', views.blog_view, name='post_url'),
    path('list', views.post_list, name='post_list_url'),
    path('category/<int:pk>', views.category_detail, name='category_list_url'),
    path('search', views.search, name='search_url'),
    path('contact', views.contact, name='contact_page_url')
]
