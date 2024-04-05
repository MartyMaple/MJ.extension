# -*- coding: utf-8 -*-
__title__ = "Level Elevation"
__doc__ = """Version = 0.1
Date: 04.04.2024
---------------------------------------------------------------------
Description:

This tool will add/update your level name to have its elevation.
----------------------------------------------------------------------
How-to-use:

-> Click on the button
-> Change Settings (optional)
-> Rename Levels

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
doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
app = __revit__.Application
PATH_SCRIPT = os.path.dirname(__file__)

# Symbols
symbol_start = "〔"
symbol_end = "〕"


# ╔═╗╦ ╦╔╗╔╔═╗╔╦╗╦╔═╗╔╗╔
# ╠╣ ║ ║║║║║   ║ ║║ ║║║║
# ╚  ╚═╝╝╚╝╚═╝ ╩ ╩╚═╝╝╚╝ FUNCTION
#===================================================
def get_text_in_brackets(text, symbol_start, symbol_end):
    """Function to get content between 2 symbols
    :param text:            Initial Text
    :param symbol_start:    Start Symbol
    :param symbol_end:      End Symbol
    :return:                Text between 2 symbols, if found.
    e.g. get_text_in_brackets('this is [not] very important message.', '[', ']') -> 'not'"""
    if symbol_start in text and symbol_end in text:
        start = text.find(symbol_start) + len(symbol_start)
        stop = text.find(symbol_end)
        return text[start:stop]
    return ""


# ╔═╗╦  ╔═╗╔═╗╔═╗╔═╗╔═╗
# ║  ║  ╠═╣╚═╗╚═╗║╣ ╚═╗
# ╚═╝╩═╝╩ ╩╚═╝╚═╝╚═╝╚═╝ CLASSES
#===================================================


# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝
#===================================================
if __name__ == '__main__':

    #get all levels
    all_levels = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Levels).WhereElementIsNotElementType().ToElements()

    # get levels elevation + convert to meters

    t = Transaction(doc, __title__)
    t.Start()
    for lvl in all_levels:
        lvl_elevation = lvl.Elevation
        lvl_elevation_m = round(convert_internal_to_m( lvl_elevation), 4)
        lvl_elevation_m_str = "+" + str(lvl_elevation_m) if lvl_elevation > 0 else str(lvl_elevation_m)

        #ELEVATION EXISTS (update)
        if symbol_start in lvl.Name and symbol_end in lvl.Name:
            current_value=get_text_in_brackets(lvl.Name, symbol_start, symbol_end)
            new_name = lvl.Name.replace(current_value, lvl_elevation_m_str)

        # ELEVATION DOES NOT EXIST (new)
        else:
            elevatiom_value = symbol_start + lvl_elevation_m_str + "m" + symbol_end
            new_name = lvl.Name + " " + elevatiom_value

        try:
            if lvl.Name == new_name:
                pass
            else:
                current_name = lvl.Name
                lvl.Name = new_name
                print("Renamed: {} -> {}".format(current_name, new_name))
        except:
            print("Could not change Level name..")

    t.Commit()

    print("-"*50)
    print("Script is finished!")

