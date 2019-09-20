from django.conf.urls import url, include
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from .views import *
from django.urls import path


app_name = "libraryapp"

urlpatterns = [
    url(r'^$', book_list, name='home'),
    url(r'^$', home, name='home'),
    url(r'^books$', book_list, name='books'),
    url(r'^librarians$', list_librarians, name='librarians'),

    url(r'^libraries$', list_library, name='library'),
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'^logout/$', logout_user, name='logout'),
    url(r'^book/form$', book_form, name='book_form'), #you can use url or path
    url(r'^library/form$', library_form, name='library_form'),
    path('books/<int:book_id>/', book_details, name='book'),
    path('libraries/<int:library_id>/', library_details, name='library'),
    path('librarians/<int:librarian_id>/', librarian_details, name='librarian'),
]

# path('books', book_list, name=books')

