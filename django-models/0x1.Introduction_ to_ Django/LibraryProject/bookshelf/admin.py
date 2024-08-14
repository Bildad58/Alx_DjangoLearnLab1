
from django.contrib import admin
from .models import Book

admin.site.register(Book)

# form class admin 
class BookAdmin(admin.ModelAdmin):
# create list display
    list_display = ('title', 'author', 'publication_year')

#create list filter 
    list_filter = ('author', 'publication_year')
# create search field 
    search_fields = ('title', 'author')

# register  Book and Bookadmon
admin.site.register(Book, BookAdmin)

# Register your models here.
# Register your models here.
