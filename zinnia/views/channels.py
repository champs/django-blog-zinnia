"""Views for Zinnia channels"""
from django.views.generic.list import ListView

from zinnia.models import Entry


class EntryChannel(ListView):
    """View for displaying a custom selection of entries
    based on a search pattern, useful for SEO/SMO pages"""
    query = ''

    def get_queryset(self):
        """Override the get_queryset method to do the search"""
        return Entry.published.search(self.query)
