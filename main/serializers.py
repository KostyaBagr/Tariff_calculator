"""
Serializers for views.
"""

from rest_framework import serializers


class TariffInputSerializer(serializers.Serializer):
    """Serializser for input data."""
    TariffUnit = serializers.CharField(max_length=100)
    TariffUnitPrice = serializers.IntegerField()
    Started_at = serializers.DateTimeField()
    LastPaymentTime = serializers.DateTimeField(required=False)
    Deposit = serializers.FloatField(required=False)

    def validate_TariffUnit(self, value):
        """Check tariffUnit instance."""
        if value.lower() not in ('минута', 'час', 'день', 'неделя'):
            raise serializers.ValidationError("Invalid tarrifUnit value")
        return value


class TariffOutputSerializser(serializers.Serializer):
    """Serializer for output data."""
    Duration = serializers.CharField(max_length=255)
    UnpaidDuration = serializers.CharField(max_length=255, required=False,
                                           allow_blank=True)
    Cost = serializers.IntegerField()
