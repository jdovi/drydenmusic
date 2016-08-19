from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sheet_list/', views.sheet_list, name='sheet_list'),
    url(r'^book_list/', views.book_list, name='book_list'),
    url(r'^email/', views.email, name='email'),
    url(r'^upload/', views.upload, name='upload'),
]
