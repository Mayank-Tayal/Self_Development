from django.contrib import admin
from .models import Book, Author, Address

# Register your models here.

class BookAdmin(admin.ModelAdmin):

    
    # readonly_fields = ("slug",) # make mentioned field read only 

    prepopulated_fields = {"slug":("title",)} 
    # prepopulate the field(key in dict) with the field(value of the key)
    """cannot use readonly_fields with prepopulated fields as it contradicts and 
    django wil throw error for it"""

    list_filter = ('author', 'rating')

    list_display = ('title', 'author')


admin.site.register(Book,BookAdmin) #you add class when you want to customize the interaction on admin for model
admin.site.register(Author)
admin.site.register(Address)