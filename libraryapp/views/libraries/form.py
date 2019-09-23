import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from libraryapp.models import Book
from libraryapp.models import Library
# from libraryapp.models import model_factory
from ..connection import Connection
from .details import get_library



# def get_library(library_id):
#     with sqlite3.connect(Connection.db_path) as conn:
#         conn.row_factory = sqlite3.Row
#         db_cursor = conn.cursor()

#         db_cursor.execute("""
#         select
#             l.id,
#             l.title,
#             l.address
#         from libraryapp_library l
#         WHERE l.id = ?
#          """, (library_id,))

#         return db_cursor.fetchall()


# @login_required
# def library_form(request, library_id):

#     if request.method == 'GET':
#         library = get_library(library_id)

#         template = 'libraries/form.html'

#         context = {
#         'library': library}

#         return render(request, template, context)


def get_libraries():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            l.id,
            l.title,
            l.address
        from libraryapp_library l
        """)

        return db_cursor.fetchall()

@login_required
def library_form(request):
    if request.method == 'GET':
        libraries = get_libraries()
        template = 'libraries/form.html'
        context = {
            'all_libraries': libraries
        }

        return render(request, template, context)

@login_required
def library_edit_form(request, library_id):

    if request.method == 'GET':
        library = get_library(library_id)
        libraries = get_libraries()

        template = 'libraries/form.html'
        context = {
            'library': library,
            'all_libraries': libraries
        }

        return render(request, template, context)
