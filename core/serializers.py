from rest_framework import serializers
from core.models import PdfSummary
from core.utils import generate_summary, get_file_content


class PdfFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PdfSummary
        fields = [
            "id",
            "summary",
            "created_at",
        ]
        read_only_fields = ["created_at"]


class PdfFileUploadSerializer(serializers.Serializer):
    pdf_file = serializers.FileField(write_only=True)
    reduction_percentage = serializers.IntegerField(write_only=True)

    def create(self, validated_data):
        fille = validated_data["pdf_file"]
        reduction_percentage = validated_data["reduction_percentage"] / 100
        text_content = get_file_content(fille)
        summary = generate_summary(text_content, reduction_percentage)

        data = {
            "summary": summary,
        }

        summary_serializer = PdfFileSerializer(data=data)
        summary_serializer.is_valid(raise_exception=True)
        instance = summary_serializer.save()

        return instance

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["summary"] = instance.summary
        return data
