from django.contrib import admin
from .models import File

class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'user', 'created_at')  # Campos a mostrar en la lista de objetos
    list_filter = ('user', 'created_at')  # Campos para filtrar los objetos
    search_fields = ('file', 'user__username')  # Campos para búsqueda
    date_hierarchy = 'created_at'  # Jerarquía de fechas para navegación rápida

admin.site.register(File, FileAdmin)
