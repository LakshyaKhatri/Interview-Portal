from rest_framework import serializers
from dashboard.models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='get_type_display')
    technology = serializers.StringRelatedField()
    status = serializers.StringRelatedField()
    moved_by = serializers.SerializerMethodField()

    class Meta:
        model = Application
        fields = [
            'id', 'name', 'email', 'type',
            'technology', 'status',
            'applied_on', 'moved_by', 'updated_on',
        ]

    def get_moved_by(self, obj):
        if obj.moved_by:
            return obj.moved_by.get_full_name()
        return None
