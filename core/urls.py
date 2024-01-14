from django.urls import path
from core.views import SummarView

app_name = "core"

urlpatterns = [
    path("summary/", SummarView.as_view(), name="summary"),
]
