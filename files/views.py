from rest_framework import generics
from files.models import File
from files.serializers import FileSerializer

class FileListCreate(generics.ListCreateAPIView):
    serializer_class = FileSerializer
    queryset = File.objects.all()

    def perform_create(self, serializer):
        file = self.request.data.get('file')
        name = self.request.data.get('name')
        if file and name:
            serializer.save(user=self.request.user, file=file, name=name)
        else:
            serializer.save(user=self.request.user)


class FileRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

class FileDestroy(generics.DestroyAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer