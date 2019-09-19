from django.conf.urls import url
from .views import *

app_name = "libraryapp"

urlpatterns = [
    url(r'^$', book_list, name='home'),
    url(r'^books$', book_list, name='books'),
    url(r'^librarians$', list_librarians, name='librarians'),
    url(r'^$', home, name='home'),
     url(r'^libraries$', list_library, name='library'),
]


