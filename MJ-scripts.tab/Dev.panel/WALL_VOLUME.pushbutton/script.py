# -*- coding: utf-8 -*-
__title__ = "Wall Volume"
__doc__ = """Version = 0.1
Date: 04.04.2024
---------------------------------------------------------------------
Description:

Calculates total volume of all walls in the model.
----------------------------------------------------------------------
How-to-use:

-> Click the button
-> Get the volume of walls in the project

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

"""Calculates total volume of all walls in the model."""

from Autodesk.Revit import DB

doc = __revit__.ActiveUIDocument.Document


# Creating collector instance and collecting all the walls from the model
wall_collector = DB.FilteredElementCollector(doc)\
                   .OfCategory(DB.BuiltInCategory.OST_Walls)\
                   .WhereElementIsNotElementType()


# Iterate over wall and collect Volume data
total_volume = 0.0

for wall in wall_collector:
    vol_param = wall.Parameter[DB.BuiltInParameter.HOST_VOLUME_COMPUTED]

    if vol_param:
        vol_param_m = round(vol_param.AsDouble() * 0.0283168466 , 5)
        total_volume = total_volume + vol_param_m

# now that results are collected, print the total
print("Total Wall Volume is: {} m3".format(total_volume))

print("-" * 50)
print("Script is finished!")