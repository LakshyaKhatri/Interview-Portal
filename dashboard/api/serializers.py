from rest_framework import serializers
from dashboard.models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='get_type_display')
    technology = serializers.StringRelatedField()
    current_status = serializers.StringRelatedField()

    class Meta:
        model = Application
        fields = [
            'id', 'name', 'email', 'type',
            'technology', 'current_status',
            'applied_on', 'moved_by', 'updated_on',
        ]
