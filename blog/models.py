from django.db import models
from wagtail.models import Page, Orderable

from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.models import register_snippet

from modelcluster.fields import ParentalKey

@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(choices=[
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('yellow', 'Yellow'),
        ('grey', 'Grey'),
    ], help_text='Background color', default='grey', max_length=6)

    @property
    def text_color(self):
        if self.color == 'grey':
            return 'blue-dark'
        elif self.color == 'yellow':
            return 'yellow-dark'
        return self.color


    class Meta:
        verbose_name_plural = 'blog categories'

    def __str__(self):
        return self.name


class BlogPageCategories(Orderable):
    page = ParentalKey('blog.BlogPage', related_name='categories')
    category = models.ForeignKey(
        'blog.BlogCategory',
        on_delete=models.CASCADE,
    )

    panels = [
        FieldPanel('category'),
    ]


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
        InlinePanel('categories', label='Categories'),
        FieldPanel('reading_time_in_minutes'),
        FieldPanel('body'),
    ]
