<%inherit file="local:templates.master"/>
<html lang="en">
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
  <script src="https://code.jquery.com/ui/1.10.4/jquery-ui.min.js"></script>
    <script src="//cdn.jsdelivr.net/free-jqgrid/4.8.0/js/i18n/grid.locale-es.js"></script>
  <script src="//cdn.jsdelivr.net/free-jqgrid/4.8.0/js/jquery.jqgrid.min.js"></script>
  <link rel="stylesheet" href="//cdn.jsdelivr.net/free-jqgrid/4.8.0/css/ui.jqgrid.css">

  <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

  <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
  <link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.16/themes/redmond/jquery-ui.css" type="text/css"/>

    <script src="${tg.url('/javascript/multi-select-master/js/jquery.multi-select.js')}"></script>
    <link rel="stylesheet" type="text/css" media="screen" href="/javascript/multi-select-master/css/multi-select.css" />
    <meta charset="utf-8" />

  <meta charset="utf-8" />

<html lang="en">
<head>
    <!-- The jQuery library is a prerequisite for all jqSuite products
    <script type="text/ecmascript" src="../../../js/jquery.multiselect.js"></script>
        This is the Javascript file of jqGrid --

    <script type="text/ecmascript" src="../../../js/trirand/jquery.jqGrid.min.js"></script>
    <!- This is the localization file of the grid controlling messages, labels, etc.
    <!- We support more than 40 localizations --
    <script type="text/ecmascript" src="../../../js/trirand/i18n/grid.locale-en.js"></script>
    <!- A link to a jQuery UI ThemeRoller theme, more than 22 built-in and many more custom --
    <link rel="stylesheet" type="text/css" media="screen" href="../../../css/jquery-ui.css" />
    <link rel="stylesheet" type="text/css" media="screen" href="../../../css/jquery.multiselect.css" />
    <!- The link to the CSS that the grid needs --
    <link rel="stylesheet" type="text/css" media="screen" href="../../../css/trirand/ui.jqgrid.css" /> -->

    <meta charset="utf-8" />
    <title>jqGrid Loading Data - Toolbar Searching</title>
</head>
<body>

    <style type="text/css">

        /* set the size of the datepicker search control for Order Date*/
        #ui-datepicker-div { font-size:11px; }

        /* set the size of the autocomplete search control*/
        .ui-menu-item {

        }

         .ui-autocomplete {
            font-size: 11px;
        }

    </style>
	<label for="search_cells">
		Search Grid:
	</label>
	<input id="search_cells" type="search"/>
    <table id="jqGrid"></table>
    <div id="jqGridPager"></div>
    <script type="text/javascript">

        $(document).ready(function () {
			var filter;
            $("#jqGrid").jqGrid({

                url: '/reload/loadJsonReload',
                mtype: "GET",
                datatype: "json",
				colModel: [
                    {   label : "Order ID",
						//sorttype: 'integer',
						name: 'OrderID',
						key: true,
						width: 75 ,
						colmenu : true,
						searchoptions : {
							searchOperMenu : false,
							sopt : ['eq','gt','lt','ge','le']
						}
					},
                    {
						label: "Customer ID",
                        name: 'CustomerID',
                        width: 150,
						hidedlg : true,
                        // stype defines the search type control - in this case HTML select (dropdownlist)
                        stype: "select",
                        // searchoptions value - name values pairs for the dropdown - they will appear as options
                        searchoptions: {
							value: " :[All];ALFKI:ALFKI;ANATR:ANATR;ANTON:ANTON;AROUT:AROUT;BERGS:BERGS;BLAUS:BLAUS;BLONP:BLONP;BOLID:BOLID;BONAP:BONAP;BOTTM:BOTTM;BSBEV:BSBEV;CACTU:CACTU;CENTC:CENTC;CHOPS:CHOPS;COMMI:COMMI;CONSH:CONSH;DRACD:DRACD;DUMON:DUMON;EASTC:EASTC;ERNSH:ERNSH;FAMIA:FAMIA;FOLIG:FOLIG;FOLKO:FOLKO;FRANK:FRANK;FRANR:FRANR;FRANS:FRANS;FURIB:FURIB;GALED:GALED;GODOS:GODOS;GOURL:GOURL;GREAL:GREAL;GROSR:GROSR;HANAR:HANAR;HILAA:HILAA;HUNGC:HUNGC;HUNGO:HUNGO;ISLAT:ISLAT;KOENE:KOENE;LACOR:LACOR;LAMAI:LAMAI;LAUGB:LAUGB;LAZYK:LAZYK;LEHMS:LEHMS;LETSS:LETSS;LILAS:LILAS;LINOD:LINOD;LONEP:LONEP;MAGAA:MAGAA;MAISD:MAISD;MEREP:MEREP;MORGK:MORGK;NORTS:NORTS;OCEAN:OCEAN;OLDWO:OLDWO;OTTIK:OTTIK;PERIC:PERIC;PICCO:PICCO;PRINI:PRINI;QUEDE:QUEDE;QUEEN:QUEEN;QUICK:QUICK;RANCH:RANCH;RATTC:RATTC;REGGC:REGGC;RICAR:RICAR;RICSU:RICSU;ROMEY:ROMEY;SANTG:SANTG;SAVEA:SAVEA;SEVES:SEVES;SIMOB:SIMOB;SPECD:SPECD;SPLIR:SPLIR;SUPRD:SUPRD;THEBI:THEBI;THECR:THECR;TOMSP:TOMSP;TORTU:TORTU;TRADH:TRADH;TRAIH:TRAIH;VAFFE:VAFFE;VICTE:VICTE;VINET:VINET;WANDK:WANDK;WARTH:WARTH;WELLI:WELLI;WHITC:WHITC;WILMK:WILMK;WOLZA:WOLZA"
						}
                    },
                    {
						label: "Order Date",
                        name: 'OrderDate',
                        width: 150,
						sorttype:'date',
						formatter: 'date',
						srcformat: 'Y-m-d',
						stype : 'text',
						newformat: 'n/j/Y',
                        searchoptions: {
                            // dataInit is the client-side event that fires upon initializing the toolbar search field for a column
                            // use it to place a third party control to customize the toolbar
                            dataInit: function (element) {
                                $(element).datepicker({
                                    id: 'orderDate_datePicker',
                                    dateFormat: 'm/d/yy',
                                    //minDate: new Date(2010, 0, 1),
                                    maxDate: new Date(2020, 0, 1),
                                    showOn: 'focus'
                                });
                            }

                        }
                    },
                    {
						label : "Ship Name",
                        name: 'ShipName',
                        width: 150,
                        searchoptions: {
                            // dataInit is the client-side event that fires upon initializing the toolbar search field for a column
                            // use it to place a third party control to customize the toolbar

                            dataInit: function (element) {
                                $(element).autocomplete({
                                    id: 'AutoComplete',
                                    source: function(request, response){
										this.xhr = $.ajax({
											url: 'http://trirand.com/blog/phpjqgrid/examples/jsonp/autocompletep.php?callback=?&acelem=ShipName',
											data: request,
											dataType: "jsonp",
											success: function( data ) {
												response( data );
											},
											error: function(model, response, options) {
												response([]);
											}
										});
									},
                                    autoFocus: true
                                });
                            },

							sopt : ['cn']
                        }
                    },
                    {
						label: "Freight",
						sorttype: 'number',
						name: 'Freight',
						width: 150,
						sopt : ['eq']
					},
                ],
				loadonce: true,
				viewrecords: true,
                width: 780,
                height: 250,
                rowNum: 10,
				colMenu : true,
				shrinkToFit : false,
                pager: "#jqGridPager"
            });
			// activate the toolbar searching
			$('#jqGrid').jqGrid('navGrid',"#jqGridPager", {
                search: false, // show search button on the toolbar
                add: false,
                edit: false,
                del: false,
                refresh: true
            });
			var timer;
			$("#search_cells").on("keyup", function() {
				var self = this;
				if(timer) { clearTimeout(timer); }
				timer = setTimeout(function(){
					//timer = null;
					$("#jqGrid").jqGrid('filterInput', self.value);
				},0);
			});
        });

    </script>


</body>
</html>