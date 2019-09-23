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
    url(r'^book/form$', book_form, name='book_form'), #you can use url or path
    path('books/<int:book_id>/', book_details, name='book'),
     url(r'^books/(?P<book_id>[0-9]+)/form$', book_edit_form, name='book_edit_form'),

    url(r'^librarians$', list_librarians, name='librarians'),
    # path('librarians/<int:librarian_id>/', librarian_details, name='librarian'),


     url(r'^library/form$', library_form, name='library_form'),
     url(r'^libraries$', list_library, name='library'),
    path('libraries/<int:library_id>/', library_details, name='library'),
    url(r'^libraries/(?P<library_id>[0-9]+)/form$', library_edit_form, name='library_edit_form'),

    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'^logout/$', logout_user, name='logout')

]


# path('books', book_list, name=books')

