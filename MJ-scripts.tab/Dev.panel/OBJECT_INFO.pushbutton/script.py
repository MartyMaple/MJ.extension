# -*- coding: utf-8 -*-
__title__ = "Object Info"
__doc__ = """Version = 0.1
Date: 04.04.2024
---------------------------------------------------------------------
Description:

Gets information about the selected element.
----------------------------------------------------------------------
How-to-use:

-> Click the button
-> Click to select the element you want to inspect
-> See the info

----------------------------------------------------------------------
Last update:
[04.04.2024 - 0.1 RELEASE]

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


from Autodesk.Revit import DB
from pyrevit import forms, revit
doc = __revit__.ActiveUIDocument.Document


# Pick element
with forms.WarningBar(title='Pick an Element:'):
    element = revit.pick_element()

element_type = type(element)

# Get some information
e_name      = element.Name
e_id        = element.Id
e_level     = doc.GetElement(element.LevelId)

e_width     = element.Width

print(element_type)
print(element)
print("-" * 50)

print("Element.Name: {}" .format(e_name))
print("Element.Id: {}" .format(e_id))
print("Element.Level: {}" .format(e_level.Name))
print("Wall.Width: {}" .format(e_width))

print("-" * 50)
print("Script is finished!")

