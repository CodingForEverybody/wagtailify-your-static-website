from django.db import models

from wagtail.contrib.settings.models import BaseGenericSetting, register_setting
from wagtail.admin.panels import FieldPanel

@register_setting
class FooterLinks(BaseGenericSetting):
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    panels = [
        FieldPanel("github"),
        FieldPanel("linkedin"),
    ]
