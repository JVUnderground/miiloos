from graphs.models import ComedFiveMinFeed
from rest_framework import viewsets
from graphs.serializers import ComedFiveMinFeedSerializer
from django.views.generic import TemplateView

class ComedFiveMinFeedViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Comed Five Minute Feed to be visualized.
    """
    queryset = ComedFiveMinFeed.objects.all().order_by('-date')
    serializer_class = ComedFiveMinFeedSerializer

class Index(TemplateView):
    template_name = "graphs/index.html"

