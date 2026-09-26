from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Bug
from .serializers import BugSerializer


class BugViewSet(viewsets.ModelViewSet):
    queryset = Bug.objects.all().order_by("-created_at")
    serializer_class = BugSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Bug.objects.all().order_by("-created_at")

        status = self.request.query_params.get("status")

        if status:
            queryset = queryset.filter(status=status)

        return queryset