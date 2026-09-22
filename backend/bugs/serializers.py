from rest_framework import serializers
from .models import Bug


class BugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bug
        fields = [
            "id",
            "title",
            "description",
            "severity",
            "status",
            "assigned_to",
            "root_cause",
            "resolution",
            "created_at",
            "updated_at",
        ]