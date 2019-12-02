# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1575289454.9651344
_enable_loop = True
_template_filename = '/home/kevin/Documentos/AlejandroTurboGears/Python/myproject/myproject/templates/libreria/entrevistador.mak'
_template_uri = '/home/kevin/Documentos/AlejandroTurboGears/Python/myproject/myproject/templates/libreria/entrevistador.mak'
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
        __M_writer = context.writer()
        __M_writer('\n<html lang="en">\n<head>\n<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>\n  <script src="//cdn.jsdelivr.net/free-jqgrid/4.8.0/js/i18n/grid.locale-es.js"></script>\n  <script src="//cdn.jsdelivr.net/free-jqgrid/4.8.0/js/jquery.jqgrid.min.js"></script>\n    <link rel="stylesheet" href="//cdn.jsdelivr.net/free-jqgrid/4.8.0/css/ui.jqgrid.css"></link>\n    <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css"></link>\n  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">\n  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>\n\n    <script src="')
        __M_writer(escape(tg.url('/lib/js/alert.js')))
        __M_writer('"></script>\n  <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>\n  <link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.16/themes/redmond/jquery-ui.css" type="text/css"/>\n    <meta charset="utf-8" />\n    <title>jqGrid Loading Data - Million Rows from a REST service</title>\n</head>\n<body>\n<br>\n\n\n\n<table style="width:100%;overflow:auto;">\n    <table id="jqGridTableBook" class="scroll" cellpadding="0" cellspacing="0"></table>\n    <div id="listPagerTablesBook" class="scroll" style="text-align:center;"></div>\n    <div id="listPsetcolsBook" class="scroll" style="text-align:center;"></div>\n    </table>\n<script type="text/javascript">\n        $(document).ready(\n        function () {\n            var grid_name_book= \'#jqGridTableBook\';\n            var grid_pager_book= \'#listPagerTablesBook\';\n            var update_url_book=\'/libreria/updateBook\';\n            var load_url_book=\'/libreria/loadBook/\';\n            var header_container_book=\'Entrevistadores\';\n            var addParams_book = {left: 0,width: window.innerWidth-400,top: 20,height: 250,url: update_url_book, closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}\n            var editParams_book = {left: 0,width: window.innerWidth-400,top: 20,height: 250,url: update_url_book,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,modal: true,\n                    width: "500",\n                    editfunc: function (rowid) {\n                    alert(\'The "Edit" button was clicked with rowid=\' + rowid);\n                    }\n                };\n            var deleteParams_book = {left: 0,width: window.innerWidth-500,top: 20,height: 130,url: update_url_book,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}\n            var viewParams_book = {left: 0,width: window.innerWidth-700,top: 20,height: 130,url: update_url_book,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}\n            var searchParams_book = {top: 20,height: 130,width: "500",closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,url: update_url_book,modal: true, };\n            var grid_book = jQuery(grid_name_book);\n            grid_book.jqGrid({\n                url: load_url_book,\n                datatype: \'json\',\n                mtype: \'GET\',\n                colNames: [\'ID\',\'Nombre\',\'Dia agendado\',\'Departamento\'],\n                colModel: [\n                   \n                    {name: \'book_id\',index: \'id\', width: 5,align: \'left\',key:true,hidden: true, editable: true,edittype: \'text\',editrules: {required: false}},\n                     {name: \'book_name\',index: \'book_name\', width: 25, align: \'right\', hidden: false, editable: true, edittype: \'text\',editrules: {required: false}},\n                     {name: \'dia_agendado\',index: \'dia_agendado\', formatter: \'date\', width: 10,sortable: false,align: \'right\',editable: true, editoptions: {size: 20,maxlengh: 10,\n                                            dataInit: function (element) {\n                                                $(element).datepicker({\n                                                    dateFormat: \'yy-mm-dd\',\n                                                    constrainInput: false,\n                                                    showOn: \'button\',\n                                                    buttonText: \'Seleciona el dia\'\n                                                });\n                                            }\n                            },\n                            formatoptions: {\n                                newformat: "Y-m-d"\n                            },\n\n                    },\n                    {name: \'departamento\',index: \'departamento\', width: 30, align: \'right\',hidden: false,editable: true, edittype: \'text\',editrules: {required: false}},\n                    \n\n                ],\n                pager: jQuery(grid_pager_book),\n                rowNum: 10,\n                rowList: [10, 50, 100],\n                sortname: \'book_id\',\n                sortorder: "desc",\n                autowidth: true,\n                shrinkToFit: true,\n                viewrecords: true,\n                height: 150,\n                caption: header_container_book,\n                ondblClickRow: function(rowId) {\n\n                }\n            });\n            grid_book.jqGrid(\'navGrid\',grid_pager_book,{edit:true,add:true,del:true, search:true},\n                            editParams_book,\n                            addParams_book,\n                            deleteParams_book,\n                            searchParams_book,\n                            viewParams_book);\n        });\n        $.extend($.jgrid.nav,{alerttop:1});\n    </script>\n\n\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/kevin/Documentos/AlejandroTurboGears/Python/myproject/myproject/templates/libreria/entrevistador.mak", "uri": "/home/kevin/Documentos/AlejandroTurboGears/Python/myproject/myproject/templates/libreria/entrevistador.mak", "source_encoding": "utf-8", "line_map": {"28": 0, "34": 1, "35": 12, "36": 12, "42": 36}}
__M_END_METADATA
"""
