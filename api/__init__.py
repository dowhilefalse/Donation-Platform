'''
rest_framework reverse 补丁
'''
from rest_framework import relations


original_reverse = relations.reverse
def hack_reverse(alias, **kwargs):
    namespace = kwargs['request'].resolver_match.namespace
    if bool(namespace):
        name = "%s:%s" % (namespace, alias)
        return original_reverse(name, **kwargs)
    else:
        return original_reverse(alias, **kwargs)
relations.reverse = hack_reverse