from django.db import models
from wagtail.models import Page

from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

class BlogIndexPage(Page):
    max_count = 1
    subpage_types = ['blog.BlogPage']
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


class BlogPage(Page):
    parent_page_types = ['blog.BlogIndexPage']

    reading_time_in_minutes = models.IntegerField()
    body = StreamField([
        ('content', blocks.RichTextBlock(
            features=['bold', 'italic', 'link', 'ol', 'ul', 'hr'],
            template='blocks/richtext.html'
        )),
        ('image', ImageChooserBlock(
            template='blocks/image.html',
        )),
        ('quote', blocks.BlockQuoteBlock(
            template='blocks/quote.html',
        )),
        ('twitter_block', blocks.StructBlock([
            ('text', blocks.CharBlock()),
            ('author', blocks.CharBlock()),
        ], template='blocks/twitter_block.html'))
    ])

    content_panels = Page.content_panels + [
        FieldPanel('reading_time_in_minutes'),
        FieldPanel('body'),
    ]
