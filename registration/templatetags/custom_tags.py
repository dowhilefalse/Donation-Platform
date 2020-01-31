import json

from django import template
from rest_framework.reverse import reverse


register = template.Library()

class CurrentUser2Json(template.Node):
    def render(self, context):
        user = context.request.user
        url = reverse('api:user-list', request=context.request)
        return json.dumps({
            'id': user.id,
            'username': user.username,
            'phone': getattr(user, 'phone', None),
            'url': url,
        }, ensure_ascii=True, indent=4)

@register.tag(name='current_user_json')
def current_user_json(parser, token):
    """当前用户转json"""
    try:
        # tag_name, *args = token.split_contents()
        return CurrentUser2Json()
    except ValueError:
        raise template.TemplateSyntaxError(
            "%r tag error" % token.contents.split()[0]
        )