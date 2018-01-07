from django.contrib import admin

from .models import BookTable,libUsers

admin.site.register(BookTable)
admin.site.register(libUsers)
# this is aadmin page
# one is for book table
# other is for lib USERs
