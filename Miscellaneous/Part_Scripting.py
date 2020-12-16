# https://wiki.freecadweb.org/Scripting_examples
# https://wiki.freecadweb.org/Part_scripting
import Part, PartGui 
doc = App.newDocument()  
l = Part.LineSegment()
l.StartPoint=(0.0,0.0,0.0)
l.EndPoint=(1.0,1.0,1.0)
doc.addObject("Part::Feature","Line").Shape=l.toShape() 
doc.recompute()

import FreeCAD
import Part
DOC = FreeCAD.newDocument()

def mycreateLine(pt1, pt2, objName):
    obj = DOC.addObject("Part::Line", objName)
    obj.X1 = pt1[0]
    obj.Y1 = pt1[1]
    obj.Z1 = pt1[2]

    obj.X2 = pt2[0]
    obj.Y2 = pt2[1]
    obj.Z2 = pt2[2]

    DOC.recompute()
    return obj

line = mycreateLine((0,0,0), (0,10,0), "LineName")

import Part
doc = App.activeDocument()
c = Part.Circle() 
c.Radius=10.0  
f = doc.addObject("Part::Feature", "Circle")
f.Shape = c.toShape()
doc.recompute()

import FreeCAD
import Part
DOC = FreeCAD.newDocument()

def mycreateCircle(rad, objName):
    obj = DOC.addObject("Part::Circle", objName)
    obj.Radius = rad

    DOC.recompute()
    return obj

circle = mycreateCircle(5.0, "CircleName")

s = f.Shape
e = s.Edges[0]
c = e.Curve
