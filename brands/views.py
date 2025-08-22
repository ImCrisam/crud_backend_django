from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Brand
from .serializers import BrandSerializer
from .permissions import HeaderNumberPermission
class BrandViewSet(viewsets.ModelViewSet):
    """CRUD for Brand. Read is open; write operations require a numeric
    X-CLIENT-ID header matching settings.FAKE_CLIENT_ID (default '42').
    """
    queryset = Brand.objects.all().order_by('-created_at')
    serializer_class = BrandSerializer
    permission_classes = [HeaderNumberPermission]

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