from graphs.models import ComedFiveMinFeed
from rest_framework import serializers


class ComedFiveMinFeedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ComedFiveMinFeed
        fields = '__all__'