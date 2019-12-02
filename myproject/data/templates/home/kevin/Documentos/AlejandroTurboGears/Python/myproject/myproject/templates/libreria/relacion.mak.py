# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1575304923.1404467
_enable_loop = True
_template_filename = '/home/kevin/Documentos/AlejandroTurboGears/Python/myproject/myproject/templates/libreria/relacion.mak'
_template_uri = '/home/kevin/Documentos/AlejandroTurboGears/Python/myproject/myproject/templates/libreria/relacion.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'local:templates.master', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        tg = context.get('tg', UNDEFINED)
        h = context.get('h', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<html lang="en">\n<head>\n<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>\n  <script src="//cdn.jsdelivr.net/free-jqgrid/4.8.0/js/i18n/grid.locale-es.js"></script>\n  <script src="//cdn.jsdelivr.net/free-jqgrid/4.8.0/js/jquery.jqgrid.min.js"></script>\n    <link rel="stylesheet" href="//cdn.jsdelivr.net/free-jqgrid/4.8.0/css/ui.jqgrid.css"></link>\n    <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css"></link>\n  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">\n  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>\n\n    <script src="')
        __M_writer(escape(tg.url('/lib/js/alert.js')))
        __M_writer('"></script>\n  <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>\n  <link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.16/themes/redmond/jquery-ui.css" type="text/css"/>\n    <meta charset="utf-8" />\n    <title>jqGrid Loading Data - Million Rows from a REST service</title>\n</head>\n<body>\n<br>\n\n\n<table style="width:100%;overflow:auto;">\n    <table id="jqGrid"></table>\n    <div id="jqGridPager"></div>\n    <div style="red" id="dialogForm01"  title="Agenda"></div>\n    </table>\n\n <script type="text/javascript">\n\n     function EliminaFila(rowId) {\n         var selRowId = jQuery(\'#jqGrid\').jqGrid(\'getGridParam\', \'selrow\');\n         var rowData = jQuery("#jqGrid").getRowData(selRowId);\n         var usuario_id = rowData[\'usuario_id\'];\n         var book_id = rowData[\'book_id\'];\n\n\n         if (!selRowId) {\n             alert("Seleccione una fila")\n         } else {\n             $(\'#dialogForm01\').html("¿Deseas eliminar este registro?");\n             var winHeight = Math.round(window.innerHeight * .345)\n             var winWidth = Math.round(window.innerWidth * .445)\n             var ContDialog = $("#dialogForm01").dialog({\n                 autoOpen: false,\n                 height: winHeight - 100,\n                 width: winWidth - 300,\n                 modal: true,\n                 title: "')
        __M_writer(escape(_('Eliminar')))
        __M_writer('",\n                 dialogClass: "noclose",\n                 closeOnEscape: false,\n                 buttons: {\n                     "')
        __M_writer(escape(_('Si')))
        __M_writer('": function () {\n                         $(\'#dialogForm01\').html("");\n\n                         <!-- Aquí inicia la funcion para enviar los datos del row al EndPoint-->\n                         var formData = new FormData();\n                         formData.append("usuario_id", usuario_id);\n                         formData.append("book_id", book_id);\n                         var request = new XMLHttpRequest();\n                         request.open("POST", \'')
        __M_writer(escape(h.url()))
        __M_writer('/libreria/DeletePrestamo\');\n                         request.send(formData);\n                         $(\'#jqGrid\').trigger(\'reloadGrid\');\n\n                         ContDialog.dialog("close");\n                     },\n                     "')
        __M_writer(escape(_('No')))
        __M_writer('": function () {\n                         $(\'#dialogForm01\').html("");\n                         ContDialog.dialog("close");\n                     }\n                 },\n                 close: function () {\n                 }\n             });\n             ContDialog.dialog("open");\n         }\n     }\n        $(document).ready(\n            function () {\n\n            $("#jqGrid").jqGrid({\n                url: "')
        __M_writer(escape(tg.url('/libreria/tablaBaseConec')))
        __M_writer('",\n                datatype: "json",\n                colNames: [\'Solicitante\', \'Entrevistador\'],\n                colModel: [\n                    { name: \'name\', index :\'name\', width: 250 },\n                    { name: \'book_name\', index :\'book_name\',width: 250 },\n                ],\n        viewrecords: true,\n                height: 250,\n                rowNum: 20,\n                pager: "#jqGridPager",\n                caption: "Agenda"\n            });\n            jQuery("#jqGrid").jqGrid(\'navGrid\',\'#jqGridPager\',{edit:false,add:false,del:false});\n            jQuery("#jqGrid").navButtonAdd(\'#jqGridPager\',\n                {\n                    buttonicon: "ui-icon-plus",\n                    title: "')
        __M_writer(escape(_('Agrgar una Fila')))
        __M_writer('",\n                    caption: "')
        __M_writer(escape(_(' ')))
        __M_writer('",\n                    position: "first",\n                    onClickButton: function(){\n                        displayPrestamo();\n                    }\n                })\n            jQuery("#jqGrid").navButtonAdd(\'#jqGridPager\',\n                {\n                    buttonicon: " ui-icon-trash",\n                    title: "Eliminar",\n                    caption: " ",\n                    position: "last",\n                    onClickButton: function(rowId){\n                        EliminaFila(rowId);\n                    }\n                });\n        });\n\n\nfunction  displayPrestamo() {\n    // Create Dialog\n                 var winHeight=Math.round(window.innerHeight*.75)\n                 var winWidth=Math.round(window.innerWidth*.86)\n                 var Dialog01 = $( "#dialogForm01" ).dialog({\n                        autoOpen: false,\n                        height: winHeight-330,\n                        width: winWidth-900,\n                        modal: true,\n\n                        close: function() {\n\n                            //form[ 0 ].reset();\n                            //allFields.removeClass( "ui-state-error" );\n                        },\n                        \n                 });\n                 $.ajax({\n                    type: "GET",\n                    url: "')
        __M_writer(escape(tg.url('/libreria/prestamosTemplate')))
        __M_writer('",\n                    contentType: "application/json; charset=utf-8",\n                    data: { \'param\':\'gaugeParameters\' },\n                    success: function(parameterdata) {\n                        //Insert HTML code\n                        $( "#dialogForm01" ).html(parameterdata.prestamostemplate);\n                        $( "#dialogForm01" ).show();\n                        Dialog01.dialog( "open" );\n                    },\n                    error: function() {\n                        alert("Error accessing server /libreria/prestamosTemplate")\n                    },\n                    complete: function() {\n                    }\n                 });\n\n        }\n   </script>\n\n\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/kevin/Documentos/AlejandroTurboGears/Python/myproject/myproject/templates/libreria/relacion.mak", "uri": "/home/kevin/Documentos/AlejandroTurboGears/Python/myproject/myproject/templates/libreria/relacion.mak", "source_encoding": "utf-8", "line_map": {"28": 0, "36": 1, "37": 12, "38": 12, "39": 48, "40": 48, "41": 52, "42": 52, "43": 60, "44": 60, "45": 66, "46": 66, "47": 81, "48": 81, "49": 98, "50": 98, "51": 99, "52": 99, "53": 137, "54": 137, "60": 54}}
__M_END_METADATA
"""
