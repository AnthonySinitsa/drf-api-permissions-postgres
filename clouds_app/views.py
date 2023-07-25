from rest_framework import generics
from .serializer import CloudSerializer
from .models import Cloud
from .permissions import IsOwnerOrReadOnly

class CloudList(generics.ListCreateAPIView):
  permission_classes = (IsOwnerOrReadOnly)
  queryset = Cloud.objects.all()
  serializer_class = CloudSerializer
  
class CloudDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsOwnerOrReadOnly)
  queryset = Cloud.objects.all()
  serializer_class = CloudSerializer