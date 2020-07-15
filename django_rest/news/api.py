from rest_framework.parsers import FormParser, MultiPartParser

from .models import News
from rest_framework import viewsets, permissions
from .serializers import NewsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('-created_at')
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = NewsSerializer
    parser_classes = (FormParser, MultiPartParser)
