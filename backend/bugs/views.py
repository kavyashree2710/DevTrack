from rest_framework import viewsets
from .models import Bug
from .serializers import BugSerializer


class BugViewSet(viewsets.ModelViewSet):
    queryset = Bug.objects.all().order_by("-created_at")
    serializer_class = BugSerializer