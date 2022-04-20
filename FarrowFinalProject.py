'''
Final Project: Batch Processing Viewsheds

This script tool takes a large amount of shapefile point data and calculates a viewshed for each point.

Requirements:
The user must input a workspace, a DEM, a file to be processed, and a location/name for the output

Written by Clare Farrow on December 11th, 2017
Contact Info: cefarrow@crimson.ua.edu
'''

import arcpy
from arcpy import env
from arcpy.sa import *
import os

# Check license:
if arcpy.CheckExtension("Spatial") == "Available":
    arcpy.CheckOutExtension("Spatial")
else:
    print "Spatial Analyst license is unavailable"

# Request workspace folder path from user:
workspace = arcpy.GetParameterAsText(0)
arcpy.env.workspace = workspace
arcpy.env.OverwriteOutput = True

# Request Output location/file name:
output = arcpy.GetParameterAsText(3)

# Request input DEM raster file:
DEM = arcpy.GetParameterAsText(1)

# Request input file name from user
input = arcpy.GetParameterAsText(2)

# Alert user if input file or DEM does not exist
if os.path.exists(input) == False:
    print 'Input file does not exist! Please exit and try again'
if os.path.exists(DEM) == False:
    print 'DEM file does not exist! Please exit and try again'

# Create a list of these individual files
points = arcpy.ListFeatureClasses ()
i = 1
for point in points:
    viewshed = arcpy.sa.Viewshed(DEM,point)
    viewshed.save(output+'/'+'view'+str(i))
    i = i+1


