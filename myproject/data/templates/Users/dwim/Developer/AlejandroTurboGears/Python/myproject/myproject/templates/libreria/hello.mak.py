# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1574887287.8440828
_enable_loop = True
_template_filename = '/Users/dwim/Developer/AlejandroTurboGears/Python/myproject/myproject/templates/libreria/hello.mak'
_template_uri = '/Users/dwim/Developer/AlejandroTurboGears/Python/myproject/myproject/templates/libreria/hello.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        image = context.get('image', UNDEFINED)
        book = context.get('book', UNDEFINED)
        usuario = context.get('usuario', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<HTML>\n    <HEAD>\n    <TITLE>Datos</TITLE>\n    </HEAD>\n    <BODY BGCOLOR="FFFFFF">\n        <CENTER>\n            <form>\n\n\n        <table>\n\t\t<caption>Datos de usuario</caption>\n\n        <tr>\n            <td colspan="2">\n                <img src="data:image/png;base64,')
        __M_writer(escape(image))
        __M_writer('" width="140" height="100" />\n            </td>\n        </tr>\n\t\t<tr>\n\t\t\t<td>Id de Usuario:</td>\n\t\t\t<td>')
        __M_writer(escape(usuario.usuario_id))
        __M_writer('</td>\n\t\t</tr>\n\t\t<tr>\n\t\t\t<td>Nombre de usuario:</td>\n\t\t\t<td>')
        __M_writer(escape(usuario.name))
        __M_writer('</td>\n\t\t</tr>\n        <tr>\n            <td>Libros de usuario:</td>\n')
        for it in book:
            __M_writer('                         <tr><td>')
            __M_writer(escape(it['book_name']))
            __M_writer(' </td></tr>\n')
        __M_writer('        </tr>\n\t\t</table>\n            </form>\n\n        </CENTER>\n        <HR>\n    </BODY>\n</HTML>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/dwim/Developer/AlejandroTurboGears/Python/myproject/myproject/templates/libreria/hello.mak", "uri": "/Users/dwim/Developer/AlejandroTurboGears/Python/myproject/myproject/templates/libreria/hello.mak", "source_encoding": "utf-8", "line_map": {"17": 0, "25": 1, "26": 15, "27": 15, "28": 20, "29": 20, "30": 24, "31": 24, "32": 28, "33": 29, "34": 29, "35": 29, "36": 31, "42": 36}}
__M_END_METADATA
"""
