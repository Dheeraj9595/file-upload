"""File_Upload_Class URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from upload.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),  # 127.0.0.1:8000/  - Base Url

    path('upload/', upload, name='upload'),
    path('book-list/', book_list, name='book_list'),
    # path('book-list-new/', book_list_new, name='book_list_new'),

    path('books/upload-book/', upload_book, name='upload_book'),
    path('delete-book/<int:pk>/', delete_book, name='delete_book'),

    path('delete-all-books/', delete_all_book, name='delete_all_book'),
    path('books/edit/<int:pk>/', edit, name='edit_book'),
    path('read/', csv_read, name='read'),

    
    # class based
    path('class/books/', BookListView.as_view(), name='class_book_list'),
    path('class/books/upload/', UploadBookView.as_view(), name='class_book_upload'),
    path('class/books/delete/<int:pk>/', DeleteBookView.as_view(), name='class_delete_book')

]

# for i in urlpatterns:
#     print(i)

from django.conf import settings
from django.conf.urls.static import static


if settings.DEBUG:  # development server only
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # If u want to see the stored file on server.


# 127.0.0.1:8000/media/file_name