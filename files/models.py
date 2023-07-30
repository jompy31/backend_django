from django.db import models
from django.contrib.auth.models import User
import os

class File(models.Model):
    file = models.FileField(upload_to='files/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        # Eliminar el archivo del sistema de archivos
        if self.file:
            if os.path.isfile(self.file.path):
                os.remove(self.file.path)
        
        super().delete(*args, **kwargs)
