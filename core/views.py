from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from core.serializers import PdfFileUploadSerializer
from core.models import PdfSummary


# Create your views here.
class SummarView(generics.CreateAPIView):
    serializer_class = PdfFileUploadSerializer
    queryset = PdfSummary.objects.all()
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        instance = serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
