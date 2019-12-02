# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import expose, flash, require, url, lurl
from tg import request, redirect, tmpl_context
from tg.i18n import ugettext as _, lazy_ugettext as l_
from tg.exceptions import HTTPFound
from tg import predicates
from myproject import model
from myproject.controllers.secure import SecureController
from myproject.model import DBSession
import transaction
from myproject.model.auth import User, Group, Permission
from tg import render_template
from myproject.model.tables import Tracker, Distribuciones, PhoneBook, Loans
from myproject.model.tableslibreria import Usuario, Book, prestamo_books_table
from tgext.admin.tgadminconfig import BootstrapTGAdminConfig as TGAdminConfig
from tgext.admin.controller import AdminController
from myproject.controllers.jqgrid import jqgridDataGrabber
import base64

from myproject.lib.base import BaseController
from myproject.controllers.error import ErrorController
import requests

__all__ = ['LibreriaController']


class LibreriaController(BaseController):

    def __init___(self):
        pass

    @expose('myproject.templates.libreria.libreria')
    def libreria(self):
        return dict()

    @expose('myproject.templates.libreria.entrevistador')
    def entrevistador(self):
        return dict()

    @expose('myproject.templates.libreria.relacion')
    def relacion(self):
        return dict()


    @expose('json')
    def loadUsuario(self, **kw):
        filter = []
        return jqgridDataGrabber(Usuario, 'usuario_id', filter, kw).loadGrid()

    @expose('json')
    def updateUsuario(self, **kw):
        filter = []
        return jqgridDataGrabber(Usuario, 'usuario_id', filter, kw).updateGrid()

    @expose('json')
    def addUsuario(self, **kw):
        print(kw)
        if kw["usuario_id"] == "0":
            kw['handler'] = Usuario()
            print(kw)
        else:
            kw['handler'] = DBSession.query(Usuario).filter_by(usuario_id=kw['usuario_id']).first()
            print(kw)
        dialogagrega = render_template(kw, "mako", 'myproject.templates.libreria.agregausuario')
        print(kw)
        return dict(dialogagrega=dialogagrega)

    @expose('json')
    def saveFile(self, **kw):
        print(kw)
        name = kw["name"]
        age = kw["age"]
        phone = kw["phone"]
        email_address = kw["email_address"]

        if name == "" or age == "" or phone == "" or email_address == "":
            return dict(error="Campos obligatorios")

        if kw["usuario_id"] == "0":
            if kw["image"] == "undefined":
                return dict(error="Archivo obligatorio")
            handler = Usuario()
            i=0
        else:
            handler = DBSession.query(Usuario).filter_by(usuario_id=kw['usuario_id']).first()
            i = 1

        if kw["image"] != "undefined":
            image = kw["image"]
            if image.file:
                fileName = image.filename
                if fileName.find(".png") > 0 or fileName.find(".jpeg") > 0 or fileName.find(".jpg") > 0 or fileName.find(".doc") > 0 or fileName.find(".PDF") > 0 or fileName.find(".pdf") > 0:
                    ftyoe = ""
                    if fileName.find(".png") > 0 or fileName.find(".jpeg") > 0 or fileName.find(".jpg") > 0:
                        ftyoe = "image"
                    if fileName.find(".doc") > 0:
                        ftyoe = "doc"
                    if fileName.find(".pdf") > 0:
                        ftyoe = "pdf"
                    if fileName.find(".PDF") > 0:
                        ftyoe = "pdf"
                    handler.image = image.file.read()
                else:
                    return dict(error="Archivo obligatorio de tipo PNG, JPEG, DOC, PDF")

        handler.name = name
        handler.age = age
        handler.phone = phone
        handler.email_address = email_address

        if i == 0:
            DBSession.add(handler)
        DBSession.flush()
        return dict(error="ok", usuario_id=handler.usuario_id)

 

    @expose('json')
    def loadBook(self, **kw):
        filter = []
        return jqgridDataGrabber(Book, 'book_id', filter, kw).loadGrid()

    @expose('json')
    def updateBook(self, **kw):
        filter = []
        return jqgridDataGrabber(Book, 'book_id', filter, kw).updateGrid()

    @expose('json')
    def openClose(self, **kw):
        handler_user = DBSession.query(prestamo_books_table).filter_by(usuario_id=kw['id']).all()
        kw['usuario'] = DBSession.query(Usuario).filter_by(usuario_id=kw['id']).first()
        kw['book'] = []
        kw['image'] = ""

        for item in handler_user:
            handler_book = DBSession.query(Book).filter_by(book_id=item.book_id).first()
            if handler_book != None:
                kw['book'].append({'book_name': handler_book.book_name})
        if kw['usuario'].image != None:
            kw['image'] = base64.b64encode(kw['usuario'].image)
            kw['image'] = str(kw['image']).replace("b'", "")
            kw['image'] = str(kw['image']).replace("'", "")
        dialogtemplate = render_template(kw, "mako", 'myproject.templates.libreria.hello')
        return dict(dialogtemplate=dialogtemplate)

  
    @expose('json')
    def tablaBaseConec(self, **kw):
        prestamos = DBSession.query(prestamo_books_table).all()  # prestamos recibe todos los elementos de la tabla prestamos
        relacion = []  # Se crea una nueva lista donde almacenaremos datos
        for prestamo in prestamos:  # Recorremos los elementos de prestamos
            usuario = DBSession.query(Usuario).filter_by(usuario_id=prestamo.usuario_id).first()  # la variable usuario recibe elementos de la tabla Usuario donde usuario_id es igual a la misma posicion en prestamos
            libro = DBSession.query(Book).filter_by(book_id=prestamo.book_id).first()  # la variable libro recibe elementos de la tabla Book donde book_id es igual a la misma posicion en prestamos
            relacion.append({'usuario_id': usuario.name, 'book_id': libro.book_name})  # Se regresa a relacion cada posicion recorrida en prestamos y se envia el nombre de las tablas Book y Usuario
        return dict(total=200, page=1, records=500, rows=relacion)  # Regresamos un Json con formato total, page, records, rows que es como lo requiere nuestro jqgrid

    @expose('json')
    def prestamosTemplate(self, **kw):
        list = []
        prestamostemplate = render_template({"list": list}, "mako", 'myproject.templates.libreria.prestamostemplate')
        return dict(prestamostemplate=prestamostemplate)



    @expose('json')
    def DeletePrestamo(self, **kw):
        print(kw)
        usuario_id = kw["usuario_id"]
        book_id = kw["book_id"]
        print(usuario_id)
        print(book_id)
        current_usuario = DBSession.query(Usuario).filter_by(usuario_id=usuario_id).first()
        current_book = DBSession.query(Book).filter_by(book_id=book_id).first()
        current_usuario.books.remove(current_book)
        DBSession.flush()
        return dict()
  