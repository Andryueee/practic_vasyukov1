from django.urls import path
from . import views
from django.urls import re_path


urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^books/$', views.BookListView.as_view(), name='books'),
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    re_path(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    re_path(r'borrowed/', views.LoanedBooksAllListView.as_view(), name='all-borrowed'),
    re_path('authors/', views.AuthorListView.as_view(), name='authors'),
    re_path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    re_path(r'^book/(?P<pk>[-\w]+)/renew/$', views.renew_book_librarian, name='renew-book-librarian'),
    re_path(r'^author/create/$', views.AuthorCreate.as_view(), name='author_create'),
    re_path(r'^author/(?P<pk>\d+)/update/$', views.AuthorUpdate.as_view(), name='author_update'),
    re_path(r'^author/(?P<pk>\d+)/delete/$', views.AuthorDelete.as_view(), name='author_delete'),
    re_path('book/create/', views.BookCreate.as_view(), name='book-create'),
    re_path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book-update'),
    re_path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book-delete'),

]
