from django import template
import re

register = template.Library()

@register.filter
def youtube_embed(url):
    embed_url = re.sub(r'watch\?v=', 'embed/', url)
    return embed_url
