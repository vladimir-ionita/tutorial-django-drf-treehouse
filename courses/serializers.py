from rest_framework import serializers

from . import models


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'url'
        )
        model = models.Course
