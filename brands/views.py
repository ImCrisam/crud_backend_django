from rest_framework import viewsets, permissions
from .models import Brand
from .serializers import BrandSerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all().order_by('-created_at')
    serializer_class = BrandSerializer
    permission_classes = [permissions.AllowAny]
