# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1485205305.7045832
_enable_loop = True
_template_filename = 'themes/custom/templates/index.tmpl'
_template_uri = 'index.tmpl'
_source_encoding = 'utf-8'
_exports = ['content', 'extra_head', 'content_header']


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
        def content():
            return render_content(context._locals(__M_locals))
        def content_header():
            return render_content_header(context._locals(__M_locals))
        parent = context.get('parent', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        pagekind = context.get('pagekind', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        front_index_header = context.get('front_index_header', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        index_teasers = context.get('index_teasers', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        index_file = context.get('index_file', UNDEFINED)
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        front_index_header = context.get('front_index_header', UNDEFINED)
        def content_header():
            return render_content_header(context)
        date_format = context.get('date_format', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        helper = _mako_get_namespace(context, 'helper')
        index_teasers = context.get('index_teasers', UNDEFINED)
        pagekind = context.get('pagekind', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
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


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        permalink = context.get('permalink', UNDEFINED)
        def extra_head():
            return render_extra_head(context)
        posts = context.get('posts', UNDEFINED)
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
{"filename": "themes/custom/templates/index.tmpl", "line_map": {"23": 3, "26": 2, "32": 0, "56": 2, "57": 3, "58": 4, "63": 11, "68": 56, "74": 13, "92": 13, "97": 14, "98": 15, "99": 16, "100": 16, "101": 16, "102": 18, "103": 19, "104": 20, "105": 20, "106": 20, "107": 22, "108": 22, "109": 22, "110": 22, "111": 24, "112": 24, "113": 24, "114": 24, "115": 24, "116": 24, "117": 24, "118": 24, "119": 25, "120": 25, "121": 25, "122": 25, "123": 25, "124": 25, "125": 26, "126": 26, "127": 26, "128": 26, "129": 26, "130": 26, "131": 26, "132": 26, "133": 27, "134": 28, "135": 28, "136": 28, "137": 30, "138": 32, "139": 33, "140": 34, "141": 34, "142": 35, "143": 36, "144": 37, "145": 37, "146": 39, "147": 40, "148": 43, "149": 44, "150": 44, "151": 44, "152": 44, "153": 44, "154": 46, "155": 49, "156": 52, "157": 53, "158": 53, "159": 54, "160": 54, "161": 55, "162": 55, "168": 6, "178": 6, "179": 7, "180": 7, "181": 8, "182": 9, "183": 9, "184": 9, "190": 14, "201": 190}, "uri": "index.tmpl", "source_encoding": "utf-8"}
__M_END_METADATA
"""
