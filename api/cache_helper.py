import os
import warnings

from django.core.cache import cache
from diskcache.fanout import FanoutCache


cache_page_fixed = 'views.decorators.cache.cache_page'
cache_header_fixed = 'views.decorators.cache.cache_header'
is_support = isinstance(cache._cache, FanoutCache)

def not_support_warn(func_name):
    message = 'function {0}() only is support diskcache.DjangoCache as cache backend'.format(func_name)
    warnings.warn(message, FutureWarning)

def keys_by_prefix(prefix):
    version = cache.make_key('')
    version_len = len(version)
    for fixed in [cache_page_fixed, cache_header_fixed]:
        info = '{0}{1}.{2}'.format(version, fixed, prefix)
        if is_support:
            for key in cache._cache:
                if key.startswith(info):
                    yield key[version_len:]
        else:
            not_support_warn('keys_by_prefix')

def clear_by_prefix(prefix):
    if is_support:
        for key in keys_by_prefix(prefix):
            cache.delete(key)
    else:
        not_support_warn('clear_by_prefix')

def keys_iter():
    if is_support:
        for key in cache._cache:
            yield key
    else:
        not_support_warn('all_keys')

def keys_count():
    if is_support:
        return len(cache._cache)
    else:
        not_support_warn('all_keys')
