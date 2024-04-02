from django.db import models
from wagtail.models import Page

from wagtail.admin.panels import FieldPanel


class BlogIndexPage(Page):
    max_count = 1
    # subpage_types = ['blog.BlogPage'] # TODO
    parent_page_types = ['home.HomePage']

    summary = models.TextField(blank=True, max_length=500)
    subscribe_url = models.URLField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('summary'),
        FieldPanel('subscribe_url'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        # TODO:
        # context['posts'] = BlogPage.objects.live().public().order_by('-first_pubished_at')
        return context
