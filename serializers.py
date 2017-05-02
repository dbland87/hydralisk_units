from units.models import Unit

from rest_framework import serializers


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ('id', 'name', 'bag')
