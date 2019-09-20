import sqlite3
from django.shortcuts import render
from libraryapp.models import Librarian
from libraryapp.models import Library
from ..connection import Connection
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


@login_required
def list_library(request):
    if request.method == 'GET':
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

            all_libraries = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                lib = Library()
                lib.id = row["id"]
                lib.title = row["title"]
                lib.address = row["address"]

                all_libraries.append(lib)

        template_name = 'libraries/list.html'

        context = {
            'all_libraries': all_libraries
        }

        return render(request, template_name, context)

    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

    #below, first argument is the SQL data, second argument is a tuple
            db_cursor.execute("""
            INSERT INTO libraryapp_library
            (
                title, address
            )
            VALUES (?, ?)
            """,
            (form_data['title'], form_data['address']))

        return redirect(reverse('libraryapp:library'))
    #we are going to stay in this route but it will be a GET request, we go fetch all teh stuff from the database, but now it will have the new book or new datat in it.

