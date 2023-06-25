from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # path('detail/<int:pk>', views.blog_view, name='post_url')
    # path('detail/<str:title>', views.blog_view, name='post_url')
    path('detail/<slug:slug>', views.blog_view, name='post_url')

]
