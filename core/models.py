from django.db import models


# Create your models here.
class PdfSummary(models.Model):
    summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
