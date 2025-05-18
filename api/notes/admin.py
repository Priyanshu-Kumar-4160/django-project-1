from django.contrib import admin
from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')  # Columns to show in list view
    search_fields = ('title',)                   # Add a search bar
    list_filter = ('created_at',)                # Add a sidebar filter
    ordering = ('-created_at',)        
    readonly_fields = ('created_at',)

    fieldsets = (
        ('Note Details', {
            'fields': ('title', 'content')
        }),
        ('Meta Information', {
            'fields': ('created_at',),
        }),
    )
# Register your models here.
