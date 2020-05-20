from django import template
from django.utils.safestring import mark_safe
from garb.config import get_config
from django.contrib.admin.views.main import ALL_VAR, PAGE_VAR
from html import escape
from builtins import range

register = template.Library()
DOT = '.'

@register.simple_tag
def paginator_number(cl, i):
    """
    Generates an individual page index link in a paginated list.
    """
    if i == DOT:
        return mark_safe('<li class="disabled"><a href="#" onclick="return false;">...</a></li>')
    elif i == cl.page_num:
        return mark_safe( '<li class="active"><a %s %s href="">%d</a></li> ' % (
                (i == cl.paginator.num_pages - 1 and ' class="end"' or ''),
                (i == 0 and ' class="start"' or ''),
                i + 1))
    else:
        return mark_safe('<li><a href="%s" %s %s>%d</a></li> ' % ( 
            escape(cl.get_query_string({PAGE_VAR: i})), 
            (i == cl.paginator.num_pages - 1 and ' class="end"' or ''),
            (i == 0 and ' class="start"' or ''),
            i + 1))

@register.simple_tag
def paginator_info(cl):
    paginator = cl.paginator

    # If we show all rows of list (without pagination)
    if cl.show_all and cl.can_show_all:
        entries_from = 1 if paginator.count > 0 else 0
        entries_to = paginator.count
    else:
        entries_from = (
            (paginator.per_page * cl.page_num) + 1) if paginator.count > 0 else 0
        entries_to = entries_from - 1 + paginator.per_page
        if paginator.count < entries_to:
            entries_to = paginator.count
    return '%s - %s' % (entries_from, entries_to)


@register.inclusion_tag('admin/pagination.html')
def pagination(cl):
    """
    Generate the series of links to the pages in a paginated list.
    """
    paginator, page_num = cl.paginator, cl.page_num

    pagination_required = (not cl.show_all or not cl.can_show_all) and cl.multi_page
    if not pagination_required:
        page_range = []
    else:
        ON_EACH_SIDE = 1
        ON_ENDS = 1

        # If there are 10 or fewer pages, display links to every page.
        # Otherwise, do some fancy
        if paginator.num_pages <= 8:
            page_range = range(paginator.num_pages)
        else:
            # Insert "smart" pagination links, so that there are always ON_ENDS
            # links at either end of the list of pages, and there are always
            # ON_EACH_SIDE links at either end of the "current page" link.
            page_range = []
            if page_num > (ON_EACH_SIDE + ON_ENDS):
                page_range += [ *range(0, ON_ENDS), DOT, *range(page_num - ON_EACH_SIDE, page_num + 1),]
            else:
                page_range.extend(range(0, page_num + 1))
            if page_num < (paginator.num_pages - ON_EACH_SIDE - ON_ENDS - 1):
                page_range += [ *range(page_num + 1, page_num + ON_EACH_SIDE + 1), DOT,  *range(paginator.num_pages - ON_ENDS, paginator.num_pages) ]
            else:
                page_range.extend(range(page_num + 1, paginator.num_pages))

    need_show_all_link = cl.can_show_all and not cl.show_all and cl.multi_page
    return {
        'cl': cl,
        'pagination_required': pagination_required,
        'show_all_url': need_show_all_link and cl.get_query_string({ALL_VAR: ''}),
        'page_range': page_range,
        'ALL_VAR': ALL_VAR,
        '1': 1,
    }
