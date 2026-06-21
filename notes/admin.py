from django.contrib import admin
from .models import Note



# Register your models here.
#admin.site.register(Note)

#customizing the admin interface for the Note model
from django.contrib import admin
from .models import Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at',)
    ordering = ('-created_at',)



# changing the admin site header and title
admin.site.site_header = "Notes App Administration"
admin.site.site_title = "Notes Admin"
admin.site.index_title = "Welcome to Notes Dashboard"