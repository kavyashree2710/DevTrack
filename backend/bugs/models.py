from django.db import models
from django.contrib.auth.models import User


class Bug(models.Model):

    SEVERITY_CHOICES = [
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
        ("Critical", "Critical"),
    ]

    STATUS_CHOICES = [
        ("Open", "Open"),
        ("In Progress", "In Progress"),
        ("Resolved", "Resolved"),
        ("Closed", "Closed"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()

    severity = models.CharField(
        max_length=20,
        choices=SEVERITY_CHOICES,
        default="Medium"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Open"
    )

    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_bugs"
    )

    root_cause = models.TextField(
        blank=True,
        null=True
    )

    resolution = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title