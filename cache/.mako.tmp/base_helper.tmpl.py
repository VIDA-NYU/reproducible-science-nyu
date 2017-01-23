# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1485205305.5815063
_enable_loop = True
_template_filename = 'themes/custom/templates/base_helper.tmpl'
_template_uri = 'base_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_feedlinks', 'html_stylesheets', 'html_headstart', 'html_translations', 'late_load_js', 'html_navigation_links']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('notes', context._clean_inheritance_tokens(), templateuri='annotation_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'notes')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        generate_atom = _import_ns.get('generate_atom', context.get('generate_atom', UNDEFINED))
        rss_link = _import_ns.get('rss_link', context.get('rss_link', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        generate_rss = _import_ns.get('generate_rss', context.get('generate_rss', UNDEFINED))
        sorted = _import_ns.get('sorted', context.get('sorted', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        if rss_link:
            __M_writer('        ')
            __M_writer(str(rss_link))
            __M_writer('\n')
        elif generate_rss:
            if len(translations) > 1:
                for language in sorted(translations):
                    __M_writer('                <link rel="alternate" type="application/rss+xml" title="RSS (')
                    __M_writer(str(language))
                    __M_writer(')" href="')
                    __M_writer(str(_link('rss', None, language)))
                    __M_writer('">\n')
            else:
                __M_writer('            <link rel="alternate" type="application/rss+xml" title="RSS" href="')
                __M_writer(str(_link('rss', None)))
                __M_writer('">\n')
        if generate_atom:
            if len(translations) > 1:
                for language in sorted(translations):
                    __M_writer('                <link rel="alternate" type="application/atom+xml" title="Atom (')
                    __M_writer(str(language))
                    __M_writer(')" href="')
                    __M_writer(str(_link('index_atom', None, language)))
                    __M_writer('">\n')
            else:
                __M_writer('            <link rel="alternate" type="application/atom+xml" title="Atom" href="')
                __M_writer(str(_link('index_atom', None)))
                __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        has_custom_css = _import_ns.get('has_custom_css', context.get('has_custom_css', UNDEFINED))
        needs_ipython_css = _import_ns.get('needs_ipython_css', context.get('needs_ipython_css', UNDEFINED))
        use_bundles = _import_ns.get('use_bundles', context.get('use_bundles', UNDEFINED))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        annotations = _import_ns.get('annotations', context.get('annotations', UNDEFINED))
        use_cdn = _import_ns.get('use_cdn', context.get('use_cdn', UNDEFINED))
        notes = _mako_get_namespace(context, 'notes')
        __M_writer = context.writer()
        __M_writer('\n')
        if use_bundles:
            if use_cdn:
                __M_writer('            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">\n            <link href="/assets/css/all.css" rel="stylesheet" type="text/css">\n')
            else:
                __M_writer('            <link href="/assets/css/all-nocdn.css" rel="stylesheet" type="text/css">\n')
        else:
            if use_cdn:
                __M_writer('            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">\n')
            else:
                __M_writer('            <link href="/assets/css/bootstrap.min.css" rel="stylesheet" type="text/css">\n')
            __M_writer('        <link href="/assets/css/rst.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/code.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/colorbox.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/theme.css" rel="stylesheet" type="text/css">\n')
            if has_custom_css:
                __M_writer('            <link href="/assets/css/custom.css" rel="stylesheet" type="text/css">\n')
        if needs_ipython_css:
            __M_writer('        <link href="/assets/css/ipython.min.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/nikola_ipython.css" rel="stylesheet" type="text/css">\n')
        if annotations and post and not post.meta('noannotations'):
            __M_writer('        ')
            __M_writer(str(notes.css()))
            __M_writer('\n')
        elif not annotations and post and post.meta('annotations'):
            __M_writer('        ')
            __M_writer(str(notes.css()))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        nextlink = _import_ns.get('nextlink', context.get('nextlink', UNDEFINED))
        comment_system_id = _import_ns.get('comment_system_id', context.get('comment_system_id', UNDEFINED))
        comment_system = _import_ns.get('comment_system', context.get('comment_system', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        is_rtl = _import_ns.get('is_rtl', context.get('is_rtl', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        def html_stylesheets():
            return render_html_stylesheets(context)
        theme_color = _import_ns.get('theme_color', context.get('theme_color', UNDEFINED))
        def html_feedlinks():
            return render_html_feedlinks(context)
        url_replacer = _import_ns.get('url_replacer', context.get('url_replacer', UNDEFINED))
        use_base_tag = _import_ns.get('use_base_tag', context.get('use_base_tag', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        favicons = _import_ns.get('favicons', context.get('favicons', UNDEFINED))
        use_cdn = _import_ns.get('use_cdn', context.get('use_cdn', UNDEFINED))
        use_open_graph = _import_ns.get('use_open_graph', context.get('use_open_graph', UNDEFINED))
        prevlink = _import_ns.get('prevlink', context.get('prevlink', UNDEFINED))
        twitter_card = _import_ns.get('twitter_card', context.get('twitter_card', UNDEFINED))
        extra_head_data = _import_ns.get('extra_head_data', context.get('extra_head_data', UNDEFINED))
        description = _import_ns.get('description', context.get('description', UNDEFINED))
        mathjax_config = _import_ns.get('mathjax_config', context.get('mathjax_config', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n<!DOCTYPE html>\n<html\n')
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']) or (comment_system == 'facebook'):
            __M_writer("prefix='")
            if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
                __M_writer('og: http://ogp.me/ns# ')
            if use_open_graph:
                __M_writer('article: http://ogp.me/ns/article# ')
            if comment_system == 'facebook':
                __M_writer('fb: http://ogp.me/ns/fb# ')
            __M_writer("'")
        if is_rtl:
            __M_writer('dir="rtl" ')
        __M_writer('lang="')
        __M_writer(str(lang))
        __M_writer('">\n    <head>\n    <meta charset="utf-8">\n')
        if use_base_tag:
            __M_writer('    <base href="')
            __M_writer(str(abs_link(permalink)))
            __M_writer('">\n')
        if description:
            __M_writer('    <meta name="description" content="')
            __M_writer(filters.html_escape(str(description)))
            __M_writer('">\n')
        __M_writer('    <meta name="viewport" content="width=device-width, initial-scale=1">\n')
        if title == blog_title:
            __M_writer('        <title>')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('</title>\n')
        else:
            __M_writer('        <title>')
            __M_writer(filters.html_escape(str(title)))
            __M_writer(' | ')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('</title>\n')
        __M_writer('\n    ')
        __M_writer(str(html_stylesheets()))
        __M_writer('\n    <meta content="')
        __M_writer(str(theme_color))
        __M_writer('" name="theme-color">\n    ')
        __M_writer(str(html_feedlinks()))
        __M_writer('\n    <link rel="canonical" href="')
        __M_writer(str(abs_link(permalink)))
        __M_writer('">\n\n')
        if favicons:
            for name, file, size in favicons:
                __M_writer('            <link rel="')
                __M_writer(str(name))
                __M_writer('" href="')
                __M_writer(str(file))
                __M_writer('" sizes="')
                __M_writer(str(size))
                __M_writer('"/>\n')
        __M_writer('\n')
        if comment_system == 'facebook':
            __M_writer('        <meta property="fb:app_id" content="')
            __M_writer(str(comment_system_id))
            __M_writer('">\n')
        __M_writer('\n')
        if prevlink:
            __M_writer('        <link rel="prev" href="')
            __M_writer(str(prevlink))
            __M_writer('" type="text/html">\n')
        if nextlink:
            __M_writer('        <link rel="next" href="')
            __M_writer(str(nextlink))
            __M_writer('" type="text/html">\n')
        __M_writer('\n    ')
        __M_writer(str(mathjax_config))
        __M_writer('\n')
        if use_cdn:
            __M_writer('        <!--[if lt IE 9]><script src="https://html5shim.googlecode.com/svn/trunk/html5.js"></script><![endif]-->\n')
        else:
            __M_writer('        <!--[if lt IE 9]><script src="')
            __M_writer(str(url_replacer(permalink, '/assets/js/html5.js', lang)))
            __M_writer('"></script><![endif]-->\n')
        __M_writer('\n    ')
        __M_writer(str(extra_head_data))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        sorted = _import_ns.get('sorted', context.get('sorted', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        for langname in sorted(translations):
            if langname != lang:
                __M_writer('            <li><a href="')
                __M_writer(str(abs_link(_link("root", None, langname))))
                __M_writer('" rel="alternate" hreflang="')
                __M_writer(str(langname))
                __M_writer('">')
                __M_writer(str(messages("LANGUAGE", langname)))
                __M_writer('</a></li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        colorbox_locales = _import_ns.get('colorbox_locales', context.get('colorbox_locales', UNDEFINED))
        use_cdn = _import_ns.get('use_cdn', context.get('use_cdn', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        social_buttons_code = _import_ns.get('social_buttons_code', context.get('social_buttons_code', UNDEFINED))
        use_bundles = _import_ns.get('use_bundles', context.get('use_bundles', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        if use_bundles:
            if use_cdn:
                __M_writer('            <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.3/jquery.min.js"></script>\n            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>\n\n            <script src="/assets/js/all.js"></script>\n')
            else:
                __M_writer('            <script src="/assets/js/all-nocdn.js"></script>\n')
        else:
            if use_cdn:
                __M_writer('            <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.3/jquery.min.js"></script>\n            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>\n')
            else:
                __M_writer('            <script src="/assets/js/jquery.min.js"></script>\n            <script src="/assets/js/bootstrap.min.js"></script>\n            <script src="/assets/js/moment-with-locales.min.js"></script>\n            <script src="/assets/js/fancydates.js"></script>\n')
            __M_writer('        <script src="/assets/js/jquery.colorbox-min.js"></script>\n')
        if colorbox_locales[lang]:
            __M_writer('        <script src="/assets/js/colorbox-i18n/jquery.colorbox-')
            __M_writer(str(colorbox_locales[lang]))
            __M_writer('.js"></script>\n')
        __M_writer('    ')
        __M_writer(str(social_buttons_code))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        tuple = _import_ns.get('tuple', context.get('tuple', UNDEFINED))
        isinstance = _import_ns.get('isinstance', context.get('isinstance', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        navigation_links = _import_ns.get('navigation_links', context.get('navigation_links', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        rel_link = _import_ns.get('rel_link', context.get('rel_link', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        for url, text in navigation_links[lang]:
            if isinstance(url, tuple):
                __M_writer('            <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">')
                __M_writer(str(text))
                __M_writer(' <b class="caret"></b></a>\n            <ul class="dropdown-menu">\n')
                for suburl, text in url:
                    if rel_link(permalink, suburl) == "#":
                        __M_writer('                    <li class="active"><a href="')
                        __M_writer(str(permalink))
                        __M_writer('">')
                        __M_writer(str(text))
                        __M_writer(' <span class="sr-only">')
                        __M_writer(str(messages("(active)", lang)))
                        __M_writer('</span></a>\n')
                    else:
                        __M_writer('                    <li><a href="')
                        __M_writer(str(suburl))
                        __M_writer('">')
                        __M_writer(str(text))
                        __M_writer('</a>\n')
                __M_writer('            </ul>\n')
            else:
                if rel_link(permalink, url) == "#":
                    __M_writer('                <li class="active"><a href="')
                    __M_writer(str(permalink))
                    __M_writer('">')
                    __M_writer(str(text))
                    __M_writer(' <span class="sr-only">')
                    __M_writer(str(messages("(active)", lang)))
                    __M_writer('</span></a>\n')
                else:
                    __M_writer('                <li><a href="')
                    __M_writer(str(url))
                    __M_writer('">')
                    __M_writer(str(text))
                    __M_writer('</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/custom/templates/base_helper.tmpl", "line_map": {"23": 3, "26": 0, "33": 2, "34": 3, "35": 72, "36": 100, "37": 134, "38": 157, "39": 180, "40": 188, "46": 159, "59": 159, "60": 160, "61": 161, "62": 161, "63": 161, "64": 162, "65": 163, "66": 164, "67": 165, "68": 165, "69": 165, "70": 165, "71": 165, "72": 167, "73": 168, "74": 168, "75": 168, "76": 171, "77": 172, "78": 173, "79": 174, "80": 174, "81": 174, "82": 174, "83": 174, "84": 176, "85": 177, "86": 177, "87": 177, "93": 103, "106": 103, "107": 104, "108": 105, "109": 106, "110": 108, "111": 109, "112": 111, "113": 112, "114": 113, "115": 114, "116": 115, "117": 117, "118": 121, "119": 122, "120": 125, "121": 126, "122": 129, "123": 130, "124": 130, "125": 130, "126": 131, "127": 132, "128": 132, "129": 132, "135": 4, "165": 4, "166": 8, "167": 9, "168": 10, "169": 11, "170": 13, "171": 14, "172": 16, "173": 17, "174": 19, "175": 22, "176": 23, "177": 26, "178": 26, "179": 26, "180": 29, "181": 30, "182": 30, "183": 30, "184": 32, "185": 33, "186": 33, "187": 33, "188": 35, "189": 36, "190": 37, "191": 37, "192": 37, "193": 38, "194": 39, "195": 39, "196": 39, "197": 39, "198": 39, "199": 41, "200": 42, "201": 42, "202": 43, "203": 43, "204": 44, "205": 44, "206": 45, "207": 45, "208": 47, "209": 48, "210": 49, "211": 49, "212": 49, "213": 49, "214": 49, "215": 49, "216": 49, "217": 52, "218": 53, "219": 54, "220": 54, "221": 54, "222": 56, "223": 57, "224": 58, "225": 58, "226": 58, "227": 60, "228": 61, "229": 61, "230": 61, "231": 63, "232": 64, "233": 64, "234": 65, "235": 66, "236": 67, "237": 68, "238": 68, "239": 68, "240": 70, "241": 71, "242": 71, "248": 182, "260": 182, "261": 183, "262": 184, "263": 185, "264": 185, "265": 185, "266": 185, "267": 185, "268": 185, "269": 185, "275": 74, "286": 74, "287": 75, "288": 76, "289": 77, "290": 81, "291": 82, "292": 84, "293": 85, "294": 86, "295": 88, "296": 89, "297": 94, "298": 96, "299": 97, "300": 97, "301": 97, "302": 99, "303": 99, "304": 99, "310": 136, "323": 136, "324": 137, "325": 138, "326": 139, "327": 139, "328": 139, "329": 141, "330": 142, "331": 143, "332": 143, "333": 143, "334": 143, "335": 143, "336": 143, "337": 143, "338": 144, "339": 145, "340": 145, "341": 145, "342": 145, "343": 145, "344": 148, "345": 149, "346": 150, "347": 151, "348": 151, "349": 151, "350": 151, "351": 151, "352": 151, "353": 151, "354": 152, "355": 153, "356": 153, "357": 153, "358": 153, "359": 153, "365": 359}, "uri": "base_helper.tmpl", "source_encoding": "utf-8"}
__M_END_METADATA
"""
