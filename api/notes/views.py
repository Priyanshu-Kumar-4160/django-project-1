from django.shortcuts import render
from rest_framework import viewsets
from .models import Note, Category
from .models import *
from .serializers import NoteSerializer, CategorySerializer
# Create your views here.


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.select_related('category').all()  # Optimized ORM
    serializer_class = NoteSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


from .models import Note

# 1. Get all notes
all_notes = Note.objects.all()

# 2. Filter notes by title
important_notes = Note.objects.filter(title__icontains='important')

# 3. Get a single note by id (raises error if not found)
from django.shortcuts import get_object_or_404
note = get_object_or_404(Note, id=1)

# 4. Create a new note
new_note = Note.objects.create(title='My Title', content='My Content', category_id=1)

# 5. Update a note
note_to_update = Note.objects.get(id=1)
note_to_update.title = "Updated Title"
note_to_update.save()

# 6. Delete a note
note_to_delete = Note.objects.get(id=2)
note_to_delete.delete()