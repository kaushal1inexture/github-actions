from datetime import datetime
from rest_framework import serializers
from crud_app.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


    def validate_name(self, value):
        if Category.objects.filter(name=value, is_deleted=False):
            raise serializers.ValidationError(f"Category with '{value}' name already exists.")
        return value

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        datetime_obj = datetime.fromisoformat(representation['created_at'])
        datetime_modified_obj = datetime.fromisoformat(representation['modified_at'])
        representation['created_at'] = datetime_obj.strftime('%Y-%m-%d %H:%M')
        representation['modified_at'] = datetime_modified_obj.strftime('%Y-%m-%d %H:%M')
        return representation
