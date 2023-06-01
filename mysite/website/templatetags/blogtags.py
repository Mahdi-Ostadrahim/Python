from django import template
from blog.models import Post, Category
register = template.Library()

@register.inclusion_tag('website/latest-posts.html')
def latest_posts(arg=3):
    posts = Post.objects.filter(status=1).order_by('published_date')[:arg]
    return {'posts': posts}