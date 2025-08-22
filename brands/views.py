from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, permissions

from .models import Brand
from .serializers import BrandSerializer

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all().order_by('-created_at')
    serializer_class = BrandSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=True, methods=['post'], url_path='toggle-active')
    def toggle_active(self, request, pk=None):
        brand = self.get_object()
        # Cambia el estado activo/inactivo
        brand.is_active = not brand.is_active
        brand.save()
        return Response({
            'id': brand.id,
            'name': brand.name,
            'is_active': brand.is_active
        }, status=status.HTTP_200_OK)