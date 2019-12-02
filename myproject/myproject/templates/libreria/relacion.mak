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
    <table id="jqGrid"></table>
    <div id="jqGridPager"></div>
    <div style="red" id="dialogForm01"  title="Agenda"></div>
    </table>

 <script type="text/javascript">

     function EliminaFila(rowId) {
         var selRowId = jQuery('#jqGrid').jqGrid('getGridParam', 'selrow');
         var rowData = jQuery("#jqGrid").getRowData(selRowId);
         var usuario_id = rowData['usuario_id'];
         var book_id = rowData['book_id'];


         if (!selRowId) {
             alert("Seleccione una fila")
         } else {
             $('#dialogForm01').html("¿Deseas eliminar este registro?");
             var winHeight = Math.round(window.innerHeight * .345)
             var winWidth = Math.round(window.innerWidth * .445)
             var ContDialog = $("#dialogForm01").dialog({
                 autoOpen: false,
                 height: winHeight - 100,
                 width: winWidth - 300,
                 modal: true,
                 title: "${_('Eliminar')}",
                 dialogClass: "noclose",
                 closeOnEscape: false,
                 buttons: {
                     "${_('Si')}": function () {
                         $('#dialogForm01').html("");

                         <!-- Aquí inicia la funcion para enviar los datos del row al EndPoint-->
                         var formData = new FormData();
                         formData.append("usuario_id", usuario_id);
                         formData.append("book_id", book_id);
                         var request = new XMLHttpRequest();
                         request.open("POST", '${h.url()}/libreria/DeletePrestamo');
                         request.send(formData);
                         $('#jqGrid').trigger('reloadGrid');

                         ContDialog.dialog("close");
                     },
                     "${_('No')}": function () {
                         $('#dialogForm01').html("");
                         ContDialog.dialog("close");
                     }
                 },
                 close: function () {
                 }
             });
             ContDialog.dialog("open");
         }
     }
        $(document).ready(
            function () {

            $("#jqGrid").jqGrid({
                url: "${tg.url('/libreria/tablaBaseConec')}",
                datatype: "json",
                colNames: ['Solicitante', 'Entrevistador'],
                colModel: [
                    { name: 'name', index :'name', width: 250 },
                    { name: 'book_name', index :'book_name',width: 250 },
                ],
        viewrecords: true,
                height: 250,
                rowNum: 20,
                pager: "#jqGridPager",
                caption: "Agenda"
            });
            jQuery("#jqGrid").jqGrid('navGrid','#jqGridPager',{edit:false,add:false,del:false});
            jQuery("#jqGrid").navButtonAdd('#jqGridPager',
                {
                    buttonicon: "ui-icon-plus",
                    title: "${_('Agrgar una Fila')}",
                    caption: "${_(' ')}",
                    position: "first",
                    onClickButton: function(){
                        displayPrestamo();
                    }
                })
            jQuery("#jqGrid").navButtonAdd('#jqGridPager',
                {
                    buttonicon: " ui-icon-trash",
                    title: "Eliminar",
                    caption: " ",
                    position: "last",
                    onClickButton: function(rowId){
                        EliminaFila(rowId);
                    }
                });
        });


function  displayPrestamo() {
    // Create Dialog
                 var winHeight=Math.round(window.innerHeight*.75)
                 var winWidth=Math.round(window.innerWidth*.86)
                 var Dialog01 = $( "#dialogForm01" ).dialog({
                        autoOpen: false,
                        height: winHeight-330,
                        width: winWidth-900,
                        modal: true,

                        close: function() {

                            //form[ 0 ].reset();
                            //allFields.removeClass( "ui-state-error" );
                        },
                        
                 });
                 $.ajax({
                    type: "GET",
                    url: "${tg.url('/libreria/prestamosTemplate')}",
                    contentType: "application/json; charset=utf-8",
                    data: { 'param':'gaugeParameters' },
                    success: function(parameterdata) {
                        //Insert HTML code
                        $( "#dialogForm01" ).html(parameterdata.prestamostemplate);
                        $( "#dialogForm01" ).show();
                        Dialog01.dialog( "open" );
                    },
                    error: function() {
                        alert("Error accessing server /libreria/prestamosTemplate")
                    },
                    complete: function() {
                    }
                 });

        }
   </script>


</body>
</html>