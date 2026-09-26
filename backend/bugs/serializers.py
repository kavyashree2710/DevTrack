from rest_framework import serializers
from .models import Bug


class BugSerializer(serializers.ModelSerializer):

    assigned_to_username = serializers.CharField(
        source="assigned_to.username",
        read_only=True
    )

    class Meta:
        model = Bug
        fields = [
            "id",
            "title",
            "description",
            "severity",
            "status",
            "assigned_to",
            "assigned_to_username",
            "root_cause",
            "resolution",
            "created_at",
            "updated_at",
        ]