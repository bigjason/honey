import logging

from django.template.context import BaseContext

logger = logging.getLogger(__name__)

def context_to_dict(context):
    """Convert a django Context object into a standard python dict."""
    result = {}
    if isinstance(context, BaseContext):
        for d in context:
            result.update(d)
    elif isinstance(context, dict):
        result.update(context)
    return result
