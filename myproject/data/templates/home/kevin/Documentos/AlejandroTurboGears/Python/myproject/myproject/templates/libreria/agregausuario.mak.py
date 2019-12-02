# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1575154730.726344
_enable_loop = True
_template_filename = '/home/kevin/Documentos/AlejandroTurboGears/Python/myproject/myproject/templates/libreria/agregausuario.mak'
_template_uri = '/home/kevin/Documentos/AlejandroTurboGears/Python/myproject/myproject/templates/libreria/agregausuario.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _ = context.get('_', UNDEFINED)
        usuario_id = context.get('usuario_id', UNDEFINED)
        handler = context.get('handler', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<script type="text/javascript">\n    $(\'.datepicker\').datepicker({\n        dateFormat: \'yy-mm-dd\',\n    startDate: \'-3d\'\n    });\n</script>\n\n<html lang="en">\n<head></head>\n<body>\n<form id="addUsuasrio">\n    <input hidden type="text" id="user_id" value=\'')
        __M_writer(escape(usuario_id))
        __M_writer('\'>\n    <fieldset>\n        <table style="width:100%">\n            <tr>\n                <td style="width:30%">\n                    ')
        __M_writer(escape(_('Nombre')))
        __M_writer(':\n                </td>\n                <td>\n                    <input type="text" maxlength="40" id="user_name" style="width: 40%" value=\'')
        __M_writer(escape(handler.name))
        __M_writer('\'>\n                </td>\n            </tr>\n\n            <tr>\n                <td style="width:30%">\n                    <br>\n                    ')
        __M_writer(escape(_('Edad')))
        __M_writer(':\n                </td>\n                <td>\n                    <br>\n                    <input type="text" maxlength="40" id="user_edad" style="width: 40%" value=\'')
        __M_writer(escape(handler.age))
        __M_writer('\'>\n                </td>\n            </tr>\n\n              <tr>\n                <td style="width:30%">\n                    <br>\n                    ')
        __M_writer(escape(_('Telefono')))
        __M_writer(':\n                </td>\n                <td>\n                    <br>\n                    <input type="text" maxlength="40" id="user_tel" style="width: 40%" value=\'')
        __M_writer(escape(handler.phone))
        __M_writer('\'>\n                </td>\n            </tr>\n\n              <tr>\n                <td style="width:30%">\n                    <br>\n                    ')
        __M_writer(escape(_('Email')))
        __M_writer(':\n                </td>\n                <td>\n                    <br>\n                    <input type="text" maxlength="40" id="user_email" style="width: 40%" value=\'')
        __M_writer(escape(handler.email_address))
        __M_writer('\'>\n                </td>\n            </tr>\n\n            <tr style="height: 10px">\n                <td></td>\n            </tr>\n            <tr>\n                <td style="width:30%" >\n                    ')
        __M_writer(escape(_('Imagen')))
        __M_writer(':\n                </td>\n                <td>\n                    <input type="file" value=\'')
        __M_writer(escape(handler.image))
        __M_writer("'>\n                </td>\n            </tr>\n        </table>\n    </fieldset>\n</form>\n</body>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/kevin/Documentos/AlejandroTurboGears/Python/myproject/myproject/templates/libreria/agregausuario.mak", "uri": "/home/kevin/Documentos/AlejandroTurboGears/Python/myproject/myproject/templates/libreria/agregausuario.mak", "source_encoding": "utf-8", "line_map": {"17": 0, "25": 1, "26": 12, "27": 12, "28": 17, "29": 17, "30": 20, "31": 20, "32": 27, "33": 27, "34": 31, "35": 31, "36": 38, "37": 38, "38": 42, "39": 42, "40": 49, "41": 49, "42": 53, "43": 53, "44": 62, "45": 62, "46": 65, "47": 65, "53": 47}}
__M_END_METADATA
"""
