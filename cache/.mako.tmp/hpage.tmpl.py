# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1583337271.081124
_enable_loop = True
_template_filename = 'themes/custom/templates/hpage.tmpl'
_template_uri = 'hpage.tmpl'
_source_encoding = 'utf-8'
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('pheader', context._clean_inheritance_tokens(), templateuri='post_header.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'pheader')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('math', context._clean_inheritance_tokens(), templateuri='math_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'math')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'post.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        math = _mako_get_namespace(context, 'math')
        post = context.get('post', UNDEFINED)
        pheader = _mako_get_namespace(context, 'pheader')
        messages = context.get('messages', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        comments = _mako_get_namespace(context, 'comments')
        enable_comments = context.get('enable_comments', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
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
        math = _mako_get_namespace(context, 'math')
        post = context.get('post', UNDEFINED)
        pheader = _mako_get_namespace(context, 'pheader')
        messages = context.get('messages', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        def content():
            return render_content(context)
        comments = _mako_get_namespace(context, 'comments')
        enable_comments = context.get('enable_comments', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('  \n    <div class="container">\n        <div class="row">\n            <!-- barra lateral donde voy a poner algo para relleno o links harcodeado en el template -->\n            <div class="col-sm-4">\n                <h5>\n                Próximos eventos\n                </h5>\n            \n                <div>\n                <p class="lead"> El que avisa no traiciona\n                </p>\n                </div>\n                <div><iframe src="https://calendar.google.com/calendar/embed?height=500&amp;wkst=2&amp;bgcolor=%23ffffff&amp;ctz=America%2FArgentina%2FBuenos_Aires&amp;src=N3E5NXNmOXQ0YzE2ZW02dmxwYnF2ODF0MjhAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ&amp;color=%23402175&amp;showDate=0&amp;showTz=0&amp;showCalendars=0&amp;showPrint=0&amp;showNav=1&amp;showTitle=0&amp;mode=AGENDA&amp;title=Calendario%20Acad%C3%A9mico" style="border-width:0" width="300" height="400" frameborder="0" scrolling="no"></iframe>\n                </div>\n            </div>\n            <div class="col-sm-8">\n                <article class="post-')
        __M_writer(str(post.meta('type')))
        __M_writer(' storypage" itemscope="itemscope" itemtype="http://schema.org/Article">\n                   <header>\n                        ')
        __M_writer(str(pheader.html_title()))
        __M_writer('\n                        ')
        __M_writer(str(pheader.html_translations(post)))
        __M_writer('\n                    </header>\n                    <div class="e-content entry-content" itemprop="articleBody text">\n                    ')
        __M_writer(str(post.text()))
        __M_writer('\n                    </div>\n')
        if site_has_comments and enable_comments and not post.meta('nocomments'):
            __M_writer('                        <section class="comments">\n                        <h2>')
            __M_writer(str(messages("Comments")))
            __M_writer('</h2>\n                        ')
            __M_writer(str(comments.comment_form(post.permalink(absolute=True), post.title(), post.base_path)))
            __M_writer('\n                        </section>\n')
        __M_writer('                    ')
        __M_writer(str(math.math_scripts_ifpost(post)))
        __M_writer('\n                </article>\n            </div>\n        </div>\n    </div> \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/custom/templates/hpage.tmpl", "uri": "hpage.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 4, "32": 5, "38": 0, "52": 2, "53": 3, "54": 4, "55": 5, "56": 6, "61": 44, "67": 8, "80": 8, "81": 25, "82": 25, "83": 27, "84": 27, "85": 28, "86": 28, "87": 31, "88": 31, "89": 33, "90": 34, "91": 35, "92": 35, "93": 36, "94": 36, "95": 39, "96": 39, "97": 39, "103": 97}}
__M_END_METADATA
"""
