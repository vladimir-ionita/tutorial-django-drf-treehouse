from rest_framework import serializers

from . import models


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'course',
            'name',
            'review',
            'rating',
            'created_at'
        )
        model = models.Review


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'url'
        )
        model = models.Course
