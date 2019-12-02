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



    <div id="dialogActivityVenus4" title="${_('Close Activity')}"></div>
    <table style="width:100%;overflow:auto;">
    <table id="jqGridTableUsuario" class="scroll" cellpadding="0" cellspacing="0"></table>
    <div id="listPagerTablesUsuario" class="scroll" style="text-align:center;"></div>
    <div id="listPsetcolsUsuario" class="scroll" style="text-align:center;"></div>
    <div id="dialogAgrgaUsuario" title="${_('Agrega Usuario')}"></div>
    </table>

<script type="text/javascript">

    function addUsuario(usuario_id) {

        $.ajax({
                        type: "GET",
                        url: "${tg.url('/libreria/addUsuario')}",
                        contentType: "application/json; charset=utf-8",
                        data: {"usuario_id":usuario_id},
                        success: function(parameterdata) {
                            //Insert HTML code
                            $( "#dialogAgrgaUsuario" ).html(parameterdata.dialogagrega);
                            $("#dialogAgrgaUsuario").show();
                        },
                        error: function() {
                            $.alert("${_('Error accessing server')} libreria/addUsuario",{type: "danger"});
                        },
                        complete: function() {
                        }
                    });


                    var ContDialogadd = $( "#dialogAgrgaUsuario" ).dialog({
                            autoOpen: false,
                            height: Math.round(window.innerHeight*.5),
                            width: Math.round(window.innerWidth*.6),
                            modal: true,
                            title: "${_('Agregar Archivo')}",
                            dialogClass: "noclose",
                            closeOnEscape: false,
                            buttons: {
                                "${_('Agregar')}": function() {
                                    var usuario_id = $('#user_id').val();
                                    var name = $('#user_name').val();
                                    var age = $('#user_edad').val();
                                    var phone = $('#user_tel').val();
                                    var email_address = $('#user_email').val();

                                    var input = document.querySelector('input[type=file]');
                                    file = input.files[0];

                                    var formData = new FormData();
                                    formData.append("usuario_id", usuario_id);
                                    formData.append("name", name);
                                    formData.append("age", age);
                                    formData.append("phone", phone);
                                    formData.append("email_address", email_address);
                                    formData.append("image", file);

                                    var request = new XMLHttpRequest();
                                    request.open("POST", '${h.url()}/libreria/saveFile');
                                    request.send(formData);

                                    request.onload  = function() {
                                    var response = JSON.parse(request.responseText);

                                    if (response.error == "ok"){
                                        $.alert("${_('File Saved')}",{type: "success"});
                                        $('#jqGridTableUsuario').trigger( 'reloadGrid' );
                                        ContDialogadd.dialog( "close" );
                                    }else{
                                        $.alert(response.error,{type: "warning"});
                                    }
                                };
                                },

                                "${_('Cerrar')}": function() {
                                    ContDialogadd.dialog( "close" );
                                    $('#addUsuasrio').html("");
                                    $('#dialogAgrgaUsuario').html("");
                                }
                            },
                            close: function() {
                                $('#addUsuasrio').html("");
                                $('#dialogAgrgaUsuario').html("");
                            }
                        });
                    ContDialogadd.dialog( "open" );


    }

        function closeVenusActivity(rowID) {
        $.ajax({
            type: "GET",
            url: '${h.url()}/libreria/openClose?id='+rowID,
            contentType: "application/json; charset=utf-8",
            data: { },
            success: function(parameterdata) {
                //Insert HTML code
                $( "#dialogActivityVenus4" ).html(parameterdata.dialogtemplate);
                $("#dialogActivityVenus4").show();
            },
            error: function() {
                $.alert("${_('Error accessing server')}/libreria/openClose",{type: "danger"});
            },
            complete: function() {
            }
        });

        var ContDialog = $( "#dialogActivityVenus4" ).dialog({
            autoOpen: false,
            height: Math.round(window.innerHeight*.46),
            width: Math.round(window.innerWidth*.186),
            modal: true,
            title: "${_('Solicitantes')}",
            dialogClass: "noclose",
            closeOnEscape: false,
            buttons: {
                "${_('Salir')}": function() {
                    $('#dialogActivityVenus4').html("");
                    ContDialog.dialog( "close" );
                },
                "${_('Otros')}": function() {
                    $('#dialogActivityVenus4').html("");
                    ContDialog.dialog( "close" );
                }


            },
            close: function() {
            }
        });
        ContDialog.dialog( "open" );
    }

function formatImage(cellValue, options, rowObject) {
var imageHtml = "<img src='images/" + cellValue + "' originalValue='" + cellValue + "' />";
var imageHtml = '<img src="data:image/png;base64,'+cellValue+'" width="150" height="50" />';
return imageHtml;
}
        $(document).ready(
        function () {
            var grid_name_usuario= '#jqGridTableUsuario';
            var grid_pager_usuario= '#listPagerTablesUsuario';
            var update_url_usuario='/libreria/updateUsuario';
            var load_url_usuario='/libreria/loadUsuario/';
            var header_container_usuario='Solicitantes';
            var addParams_usuario = {left: 0,width: window.innerWidth-400,top: 20,height: 250,url: update_url_usuario, closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
            var editParams_usuario = {left: 0,width: window.innerWidth-400,top: 20,height: 250,url: update_url_usuario,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,modal: true,
                    width: "500",
                    editfunc: function (rowid) {
                    alert('The "Edit" button was clicked with rowid=' + rowid);
                    }
                };
            var deleteParams_usuario = {left: 0,width: window.innerWidth-500,top: 20,height: 130,url: update_url_usuario,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
            var viewParams_usuario = {left: 0,width: window.innerWidth-700,top: 20,height: 130,url: update_url_usuario,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
            var searchParams_usuario = {top: 20,height: 130,width: "500",closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,url: update_url_usuario,modal: true, };
            var grid_usuario = jQuery(grid_name_usuario);
            grid_usuario.jqGrid({
                url: load_url_usuario,
                datatype: 'json',
                mtype: 'GET',
                colNames: ['Num_Usuario', 'Nombre','Edad','Telefono','Email','Fecha de ingreso','Foto'],
                colModel: [
                    {name: 'usuario_id',index: 'usuario_id', width: 5,align: 'left',key:true,hidden: true, editable: true,edittype: 'text',editrules: {required: false}},
                    {name: 'name',index: 'name', width: 30, align: 'right',hidden: false,editable: true, edittype: 'text',editrules: {required: false}},
                    {name: 'age',index: 'age', width: 30, align: 'right',hidden: false,editable: true, edittype: 'text',editrules: {required: false}},
                    {name: 'phone',index: 'phone', width: 30, align: 'right',hidden: false,editable: true, edittype: 'text',editrules: {required: false}},
                    {name: 'email_address',index: 'email_address', width: 30, align: 'right',hidden: false,editable: true, edittype: 'text',editrules: {required: false}},
                    {name: 'created',index: 'created', width: 30, align: 'right',hidden: false,editable: true, edittype: 'text',editrules: {required: false}},
                    {name: 'image',index: 'image', formatter: formatImage,align: 'left',hidden:true ,width:200,editable: true, edittype: 'string',editrules: {required: false}},
                ],
                pager: jQuery(grid_pager_usuario),
                rowNum: 10,
                rowList: [10, 50, 100],
                sortname: 'name',
                sortorder: "desc",
                autowidth: true,
                shrinkToFit: true,
                viewrecords: true,
                height: 150,
                caption: header_container_usuario,
                ondblClickRow: function(rowid) {
                          closeVenusActivity(rowid);
                      }

            });
            grid_usuario.jqGrid('navGrid',grid_pager_usuario,{edit:false,add:false,del:true, search:true},
                            editParams_usuario,
                            <!--addParams_usuario,-->
                            deleteParams_usuario,
                            searchParams_usuario,
                            viewParams_usuario);

            grid_usuario.navButtonAdd(grid_pager_usuario,
                {
                    buttonicon: "ui-icon-circle-plus",
                    title: "",
                    caption: "",
                    position: "last",
                    onClickButton: function(rowId){
                        var selRowId = grid_usuario.jqGrid ('getGridParam', 'selrow');
                        var usuario_id = grid_usuario.jqGrid('getCell',selRowId,'usuario_id');

                        if (!selRowId) {
                            alert("Selecciona una fila");
                        }
                        else {
                            closeVenusActivity(usuario_id);
                        }

                    },
                })
            .navButtonAdd(grid_pager_usuario,
                {
                    buttonicon: "ui-icon-plus",
                    title: "Agrgar una nueva fila",
                    caption: "",
                    position: "firts",
                    onClickButton: function(){

                        addUsuario(0);

                    },
                })
            .navButtonAdd(grid_pager_usuario,
                {
                    buttonicon: "ui-icon-pencil",
                    title: "Editar fila",
                    caption: "",
                    position: "last",
                    onClickButton: function(rowId){
                        var selRowId = grid_usuario.jqGrid ('getGridParam', 'selrow');
                        var usuario_id = grid_usuario.jqGrid('getCell',selRowId,'usuario_id');

                        if (!selRowId) {
                            alert("Selecciona una fila");
                        }
                        else {
                            addUsuario(usuario_id);
                        }
                    },
                });
        });
        $.extend($.jgrid.nav,{alerttop:1});
    </script>


</body>
</html>