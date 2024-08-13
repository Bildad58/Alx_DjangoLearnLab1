from .models import Author, Library, Librarian 

# query for all bookks by specific author
book = Author.object.get( author='')

Library = Library.objects.all()

librarian = Librarian.objects.get