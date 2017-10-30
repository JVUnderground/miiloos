from graphs.models import ComedFiveMinFeed
from rest_framework import viewsets
from graphs.serializers import ComedFiveMinFeedSerializer


class ComedFiveMinFeedViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Comed Five Minute Feed to be visualized.
    """
    queryset = ComedFiveMinFeed.objects.all().order_by('-date')
    serializer_class = ComedFiveMinFeedSerializer