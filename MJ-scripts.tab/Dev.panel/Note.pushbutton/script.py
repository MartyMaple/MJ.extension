# -*- coding: utf-8 -*-
__title__ = "Text note creation"
__doc__ = """Version = 0.1
Date: 05.04.2024
---------------------------------------------------------------------
Description:

Creates a new note
----------------------------------------------------------------------
How-to-use:

-> Click the button
-> Create a new text note

----------------------------------------------------------------------
Last update:
[05.04.2024 - 0.1 RELEASE]

----------------------------------------------------------------------
To-Do:
Perhaps make it work?

----------------------------------------------------------------------
Author: Martin Javurek (MartyMaple)
""" #Button Description shown in Revit UI

__author__ = "Martin Javurek"
#__helpurl__ = "" #update URL
__min_revit_version__ = 2018
__max_revit_version__ = 2025


# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝  IMPORTS
#===================================================
# Regular + Autodesk
import os, sys, math, datetime, time
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB import Transaction, Element, ElementId, FilteredElementCollector

# pyRevit
from pyrevit import revit, forms

# CUSTOM Imports
from Snippets._selection import get_selected_elements
from Snippets._convert import convert_internal_to_m

# .NET Imports
#clr.AddReference("System")
from System.Collections.Generic import List


# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝ VARIABLES
#===================================================

document    = __revit__.ActiveUIDocument.Document
viewId      =   document.ActiveView.Id
position    = XYZ(0,0,0)
text        = "New text note"
typeId      = document.GetDefaultElementTypeId(ElementTypeGroup.TextNoteType)


# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝
#===================================================

t = Transaction(document,"Create TextNote")
t.Start()

new_text = TextNote.Create(document, viewId, position, text, typeId)

t.Commit()


print("-" * 50)
print("Script is finished!")