# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1484932884.740732
_enable_loop = True
_template_filename = 'themes/custom/templates/index.tmpl'
_template_uri = 'index.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content', 'content_header']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='index_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        comments = _mako_get_namespace(context, 'comments')
        index_teasers = context.get('index_teasers', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        posts = context.get('posts', UNDEFINED)
        front_index_header = context.get('front_index_header', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        pagekind = context.get('pagekind', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        index_file = context.get('index_file', UNDEFINED)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        lang = context.get('lang', UNDEFINED)
        def content_header():
            return render_content_header(context._locals(__M_locals))
        _link = context.get('_link', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        posts = context.get('posts', UNDEFINED)
        def extra_head():
            return render_extra_head(context)
        permalink = context.get('permalink', UNDEFINED)
        index_file = context.get('index_file', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n')
        if posts and (permalink == '/' or permalink == '/' + index_file):
            __M_writer('        <link rel="prefetch" href="')
            __M_writer(str(posts[0].permalink()))
            __M_writer('" type="text/html">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        comments = _mako_get_namespace(context, 'comments')
        front_index_header = context.get('front_index_header', UNDEFINED)
        index_teasers = context.get('index_teasers', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        pagekind = context.get('pagekind', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        def content():
            return render_content(context)
        _link = context.get('_link', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        def content_header():
            return render_content_header(context)
        posts = context.get('posts', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_header'):
            context['self'].content_header(**pageargs)
        

        __M_writer('\n')
        if 'main_index' in pagekind:
            __M_writer('    ')
            __M_writer(str(front_index_header))
            __M_writer('\n')
        __M_writer('<div class="postindex">\n')
        for post in posts:
            __M_writer('    <article class="h-entry post-')
            __M_writer(str(post.meta('type')))
            __M_writer('">\n    <header>\n        <h1 class="p-name entry-title"><a href="')
            __M_writer(str(post.meta('link')))
            __M_writer('" class="u-url">')
            __M_writer(filters.html_escape(str(post.title())))
            __M_writer('</a></h1>\n        <div class="metadata">\n            <p class="dateline"><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" rel="bookmark"><time class="published dt-published" datetime="')
            __M_writer(str(post.formatted_date('webiso')))
            __M_writer('" title="')
            __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
            __M_writer('">')
            __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
            __M_writer('</time></a></p>  \n\t    <p><a href="mailto:?subject=I saw this and thought of you!&body=')
            __M_writer(str(post.title()))
            __M_writer('; ')
            __M_writer(str(post.meta('link')))
            __M_writer('" onclick="ga(\'send\', \'social\', \'email\', \'share\', ')
            __M_writer(str(post.meta('link')))
            __M_writer('); return true;">Email this article</a></p>\n\t    <p><a href="https://twitter.com/share?url=')
            __M_writer(str(post.permalink()))
            __M_writer(');text=')
            __M_writer(str(post.title()))
            __M_writer(', ')
            __M_writer(str(post.meta('link')))
            __M_writer('" onclick="ga(\'send\', \'social\', \'Twitter\', \'tweet\', ')
            __M_writer(str(post.permalink()))
            __M_writer('); return true;" target="_blank">Tweet this article</a></p> \n')
            if not post.meta('nocomments') and site_has_comments:
                __M_writer('                <p class="commentline">')
                __M_writer(str(comments.comment_link(post.permalink(), post._base_path)))
                __M_writer('\n')
            __M_writer('        </div>\n    </header>\n')
            if index_teasers:
                __M_writer('    <div class="p-summary entry-summary">\n    ')
                __M_writer(str(post.text(teaser_only=True)))
                __M_writer('\n')
            else:
                __M_writer('    <div class="e-content entry-content">\n    ')
                __M_writer(str(post.text(teaser_only=False)))
                __M_writer('\n')
            if post.tags:
                __M_writer('\t<div id="index-tags"\n        <ul class="tags">\n\t\tTagged:\n')
                for tag in post.tags:
                    __M_writer('                <li class="tag"><a href="')
                    __M_writer(str(_link('tag', tag, lang)))
                    __M_writer('">')
                    __M_writer(str(tag))
                    __M_writer('</a></li>          \n')
                __M_writer('        </ul>\n\t</div>\n')
            __M_writer('    </div>\n    </article>\n')
        __M_writer('</div>\n')
        __M_writer(str(helper.html_pager()))
        __M_writer('\n')
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\n')
        __M_writer(str(helper.mathjax_script(posts)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_header():
            return render_content_header(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"23": 3, "26": 2, "32": 0, "56": 2, "57": 3, "58": 4, "63": 11, "68": 56, "74": 6, "84": 6, "85": 7, "86": 7, "87": 8, "88": 9, "89": 9, "90": 9, "96": 13, "114": 13, "119": 14, "120": 15, "121": 16, "122": 16, "123": 16, "124": 18, "125": 19, "126": 20, "127": 20, "128": 20, "129": 22, "130": 22, "131": 22, "132": 22, "133": 24, "134": 24, "135": 24, "136": 24, "137": 24, "138": 24, "139": 24, "140": 24, "141": 25, "142": 25, "143": 25, "144": 25, "145": 25, "146": 25, "147": 26, "148": 26, "149": 26, "150": 26, "151": 26, "152": 26, "153": 26, "154": 26, "155": 27, "156": 28, "157": 28, "158": 28, "159": 30, "160": 32, "161": 33, "162": 34, "163": 34, "164": 35, "165": 36, "166": 37, "167": 37, "168": 39, "169": 40, "170": 43, "171": 44, "172": 44, "173": 44, "174": 44, "175": 44, "176": 46, "177": 49, "178": 52, "179": 53, "180": 53, "181": 54, "182": 54, "183": 55, "184": 55, "190": 14, "201": 190}, "filename": "themes/custom/templates/index.tmpl", "source_encoding": "utf-8", "uri": "index.tmpl"}
__M_END_METADATA
"""
