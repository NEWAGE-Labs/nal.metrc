# -*- coding: utf-8 -*-
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import directives
from plone.supermodel import model
from zope import schema
from zope.interface import provider

@provider(IFormFieldProvider)
class ICannabis(model.Schema):

    directives.fieldset(
        'metrc',
        label=u'METRC',
        fields=('rfid','room'),
    )

    rfid = schema.TextLine(
        title=u'RFID Tag',
        required=False,
    )

    room = schema.TextLine(
        title=u'Room',
        required=False,
    )
