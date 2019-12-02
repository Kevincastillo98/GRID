<%inherit file="local:templates.master"/>
<html lang="en">
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
  <script src="//cdn.jsdelivr.net/free-jqgrid/4.8.0/js/i18n/grid.locale-es.js"></script>
  <script src="//cdn.jsdelivr.net/free-jqgrid/4.8.0/js/jquery.jqgrid.min.js"></script>
    <link rel="stylesheet" href="//cdn.jsdelivr.net/free-jqgrid/4.8.0/css/ui.jqgrid.css"></link>
    <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css"></link>
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

    <script src="${tg.url('/lib/js/alert.js')}"></script>
  <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
  <link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.16/themes/redmond/jquery-ui.css" type="text/css"/>
    <meta charset="utf-8" />
    <title>jqGrid Loading Data - Million Rows from a REST service</title>
</head>
<body>
<br>



<table style="width:100%;overflow:auto;">
    <table id="jqGridTableBook" class="scroll" cellpadding="0" cellspacing="0"></table>
    <div id="listPagerTablesBook" class="scroll" style="text-align:center;"></div>
    <div id="listPsetcolsBook" class="scroll" style="text-align:center;"></div>
    </table>
<script type="text/javascript">
        $(document).ready(
        function () {
            var grid_name_book= '#jqGridTableBook';
            var grid_pager_book= '#listPagerTablesBook';
            var update_url_book='/libreria/updateBook';
            var load_url_book='/libreria/loadBook/';
            var header_container_book='Entrevistadores';
            var addParams_book = {left: 0,width: window.innerWidth-400,top: 20,height: 250,url: update_url_book, closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
            var editParams_book = {left: 0,width: window.innerWidth-400,top: 20,height: 250,url: update_url_book,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,modal: true,
                    width: "500",
                    editfunc: function (rowid) {
                    alert('The "Edit" button was clicked with rowid=' + rowid);
                    }
                };
            var deleteParams_book = {left: 0,width: window.innerWidth-500,top: 20,height: 130,url: update_url_book,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
            var viewParams_book = {left: 0,width: window.innerWidth-700,top: 20,height: 130,url: update_url_book,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
            var searchParams_book = {top: 20,height: 130,width: "500",closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,url: update_url_book,modal: true, };
            var grid_book = jQuery(grid_name_book);
            grid_book.jqGrid({
                url: load_url_book,
                datatype: 'json',
                mtype: 'GET',
                colNames: ['ID','Nombre','Dia agendado','Departamento'],
                colModel: [
                   
                    {name: 'book_id',index: 'id', width: 5,align: 'left',key:true,hidden: true, editable: true,edittype: 'text',editrules: {required: false}},
                     {name: 'book_name',index: 'book_name', width: 25, align: 'right', hidden: false, editable: true, edittype: 'text',editrules: {required: false}},
                     {name: 'dia_agendado',index: 'dia_agendado', formatter: 'date', width: 10,sortable: false,align: 'right',editable: true, editoptions: {size: 20,maxlengh: 10,
                                            dataInit: function (element) {
                                                $(element).datepicker({
                                                    dateFormat: 'yy-mm-dd',
                                                    constrainInput: false,
                                                    showOn: 'button',
                                                    buttonText: 'Seleciona el dia'
                                                });
                                            }
                            },
                            formatoptions: {
                                newformat: "Y-m-d"
                            },

                    },
                    {name: 'departamento',index: 'departamento', width: 30, align: 'right',hidden: false,editable: true, edittype: 'text',editrules: {required: false}},
                    

                ],
                pager: jQuery(grid_pager_book),
                rowNum: 10,
                rowList: [10, 50, 100],
                sortname: 'book_id',
                sortorder: "desc",
                autowidth: true,
                shrinkToFit: true,
                viewrecords: true,
                height: 150,
                caption: header_container_book,
                ondblClickRow: function(rowId) {

                }
            });
            grid_book.jqGrid('navGrid',grid_pager_book,{edit:true,add:true,del:true, search:true},
                            editParams_book,
                            addParams_book,
                            deleteParams_book,
                            searchParams_book,
                            viewParams_book);
        });
        $.extend($.jgrid.nav,{alerttop:1});
    </script>


</body>
</html>