# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1484932884.260046
_enable_loop = True
_template_filename = 'themes/custom/templates/base.tmpl'
_template_uri = 'base.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_js', 'extra_head', 'content', 'sourcelink', 'belowtitle']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('notes', context._clean_inheritance_tokens(), templateuri='annotation_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'notes')] = ns

    ns = runtime.TemplateNamespace('base', context._clean_inheritance_tokens(), templateuri='base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'base')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        date_fanciness = _import_ns.get('date_fanciness', context.get('date_fanciness', UNDEFINED))
        body_end = _import_ns.get('body_end', context.get('body_end', UNDEFINED))
        annotations = _import_ns.get('annotations', context.get('annotations', UNDEFINED))
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        logo_url = _import_ns.get('logo_url', context.get('logo_url', UNDEFINED))
        def belowtitle():
            return render_belowtitle(context._locals(__M_locals))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        show_blog_title = _import_ns.get('show_blog_title', context.get('show_blog_title', UNDEFINED))
        js_date_format = _import_ns.get('js_date_format', context.get('js_date_format', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        show_sourcelink = _import_ns.get('show_sourcelink', context.get('show_sourcelink', UNDEFINED))
        notes = _mako_get_namespace(context, 'notes')
        search_form = _import_ns.get('search_form', context.get('search_form', UNDEFINED))
        set_locale = _import_ns.get('set_locale', context.get('set_locale', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        momentjs_locales = _import_ns.get('momentjs_locales', context.get('momentjs_locales', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        content_footer = _import_ns.get('content_footer', context.get('content_footer', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        base = _mako_get_namespace(context, 'base')
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer(str(set_locale(lang)))
        __M_writer('\n')
        __M_writer(str(base.html_headstart()))
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n')
        __M_writer(str(template_hooks['extra_head']()))
        __M_writer('\n</head>\n<body>\n<a href="#content" class="sr-only sr-only-focusable">')
        __M_writer(str(messages("Skip to main content")))
        __M_writer('</a>\n\n<div class="container" id="content" role="main">\n\n<div class="page-header">\n\t<img class="logo-header" src=" /images/logo.png">\n\t<h1>Reproducible Science <small>Promoting Open Science</small></h1>\n\n<!-- Menubar -->\n<nav class="navbar navbar-inverse">\n\t<div class="container-fluid">\n        <div class="navbar-header">\n\t<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-2">\n            <span class="sr-only">Toggle navigation</span>\n            <span class="icon-bar"></span>\n            <span class="icon-bar"></span>\n            <span class="icon-bar"></span>\n            </button>\n            <a class="navbar-brand" href="')
        __M_writer(str(abs_link(_link("root", None, lang))))
        __M_writer('">\n')
        if logo_url:
            __M_writer('                <img src="')
            __M_writer(str(logo_url))
            __M_writer('" alt="')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('" id="logo">\n')
        __M_writer('\n')
        if show_blog_title:
            __M_writer('                <span id="blog-title" style="padding: 19px 0px;">')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('</span>\n')
        __M_writer('            </a>\n        </div><!-- /.navbar-header -->\n       <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-2">\n            <ul class="nav navbar-nav">\n                ')
        __M_writer(str(base.html_navigation_links()))
        __M_writer('\n                ')
        __M_writer(str(template_hooks['menu']()))
        __M_writer('\n            </ul>\n')
        if search_form:
            __M_writer('                ')
            __M_writer(str(search_form))
            __M_writer('\n')
        __M_writer('\n            <ul class="nav navbar-nav navbar-right">\n\t\t<!--dropdown-->\n\t      <li class="dropdown">\n\t\t<a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Reproducibility Initiatives<span class="caret"></span></a>\n\t\t<ul class="dropdown-menu">\n\t\t\t<li><a href="https://reproduciblescience.org/nyu/">Reproducibility @ NYU</a></li>\n\t\t\t <li><a href="http://escience.washington.edu/about-us/working-groups/reproducibility-and-open-science/">Reproducibility @ UW</a></li>\n\t\t\t<li><a href="http://bids.berkeley.edu/working-groups/reproducibility-and-open-science">Reproducibility @ BIDS</a></li>\n\t\t</ul>\n\t\t</li>\n\t\t<!--end dropdown-->\n\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'belowtitle'):
            context['self'].belowtitle(**pageargs)
        

        __M_writer('\n')
        if show_sourcelink:
            __M_writer('                    ')
            if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
                context['self'].sourcelink(**pageargs)
            

            __M_writer('\n')
        __M_writer('                ')
        __M_writer(str(template_hooks['menu_alt']()))
        __M_writer('\n            </ul>\n        </div><!-- /.navbar-collapse -->\n    </div><!-- /.container -->\n</nav>\n</div>\n\n<!-- End of Menubar -->\n\n    <div class="body-content">\n        <!--Body content-->\n        <div class="row">\n            ')
        __M_writer(str(template_hooks['page_header']()))
        __M_writer('\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n        </div>\n        <!--End of body content-->\n\n        <footer id="footer">\n            ')
        __M_writer(str(content_footer))
        __M_writer('\n            ')
        __M_writer(str(template_hooks['page_footer']()))
        __M_writer('\n        </footer>\n    </div>\n</div>\n\n')
        __M_writer(str(base.late_load_js()))
        __M_writer('\n    <script>$(\'a.image-reference:not(.islink) img:not(.islink)\').parent().colorbox({rel:"gal",maxWidth:"100%",maxHeight:"100%",scalePhotos:true});</script>\n    <!-- fancy dates -->\n    <script>\n    moment.locale("')
        __M_writer(str(momentjs_locales[lang]))
        __M_writer('");\n    fancydates(')
        __M_writer(str(date_fanciness))
        __M_writer(', ')
        __M_writer(str(js_date_format))
        __M_writer(');\n    </script>\n    <!-- end fancy dates -->\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        __M_writer('\n')
        if annotations and post and not post.meta('noannotations'):
            __M_writer('        ')
            __M_writer(str(notes.code()))
            __M_writer('\n')
        elif not annotations and post and post.meta('annotations'):
            __M_writer('        ')
            __M_writer(str(notes.code()))
            __M_writer('\n')
        __M_writer(str(body_end))
        __M_writer("\n<script>\n  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){\n  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),\n  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)\n  })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');\n\n  ga('create', 'UA-86255717-1', 'auto');\n  ga('send', 'pageview');\n</script>\n")
        __M_writer(str(template_hooks['body_end']()))
        __M_writer('\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        def extra_js():
            return render_extra_js(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        def sourcelink():
            return render_sourcelink(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_belowtitle(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        def belowtitle():
            return render_belowtitle(context)
        base = _mako_get_namespace(context, 'base')
        __M_writer = context.writer()
        __M_writer('\n')
        if len(translations) > 1:
            __M_writer('                    <li>')
            __M_writer(str(base.html_translations()))
            __M_writer('</li>\n')
        __M_writer('                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"128": 81, "129": 86, "130": 86, "131": 87, "132": 87, "133": 92, "134": 92, "135": 96, "136": 96, "137": 97, "138": 97, "139": 97, "140": 97, "233": 61, "145": 100, "146": 101, "147": 102, "148": 102, "149": 102, "150": 103, "23": 3, "152": 104, "153": 104, "26": 2, "155": 106, "156": 116, "29": 0, "163": 100, "220": 60, "154": 106, "157": 116, "177": 6, "186": 6, "151": 104, "232": 60, "192": 81, "69": 2, "70": 3, "71": 4, "72": 4, "73": 5, "74": 5, "206": 66, "79": 8, "80": 9, "81": 9, "82": 12, "83": 12, "84": 30, "85": 30, "86": 31, "87": 32, "88": 32, "89": 32, "90": 32, "91": 32, "92": 34, "93": 35, "94": 36, "95": 36, "96": 36, "97": 38, "98": 42, "99": 42, "100": 43, "101": 43, "102": 45, "103": 46, "104": 46, "105": 46, "106": 48, "235": 62, "236": 62, "237": 64, "111": 64, "112": 65, "113": 66, "243": 237, "118": 66, "119": 68, "120": 68, "121": 68, "122": 80, "123": 80, "234": 62}, "filename": "themes/custom/templates/base.tmpl", "source_encoding": "utf-8", "uri": "base.tmpl"}
__M_END_METADATA
"""
