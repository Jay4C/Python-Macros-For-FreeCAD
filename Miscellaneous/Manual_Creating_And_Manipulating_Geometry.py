# https://wiki.freecadweb.org/Scripting_examples
# https://wiki.freecadweb.org/Manual:Creating_and_manipulating_geometry

App.newDocument("Unnamed")
App.setActiveDocument("Unnamed")
App.ActiveDocument=App.getDocument("Unnamed")
Gui.ActiveDocument=Gui.getDocument("Unnamed")
Gui.activeDocument().activeView().viewDefaultOrientation()

import Part
boxShape = Part.makeBox(3,5,7)
myObj = FreeCAD.ActiveDocument.addObject("Part::Feature","MyNewBox")
myObj.Shape = boxShape
FreeCAD.ActiveDocument.recompute()

print(boxShape.Vertexes)
print(boxShape.Edges)
print(boxShape.Wires)
print(boxShape.Faces)
print(boxShape.Shells)
print(boxShape.Solids)

for f in boxShape.Faces:
   print(f.Area)

for e in boxShape.Edges:
   print("New edge")
   print("Start point:")
   print(e.Vertexes[0].Point)
   print("End point:")
   print(e.Vertexes[1].Point)

print(boxShape.ShapeType)
print(boxShape.Faces[0].ShapeType)
print(boxShape.Vertexes[2].ShapeType)

V1 = FreeCAD.Vector(0, 10, 0)
V2 = FreeCAD.Vector(30, 10, 0)
V3 = FreeCAD.Vector(30, -10, 0)
V4 = FreeCAD.Vector(0, -10, 0)

L1 = Part.LineSegment(V1, V2)
L2 = Part.LineSegment(V4, V3)

print(Edge.Curve)

VC1 = FreeCAD.Vector(-10, 0, 0)
C1 = Part.Arc(V1, VC1, V4)
VC2 = FreeCAD.Vector(40, 0, 0)
C2 = Part.Arc(V2, VC2, V3)

E1 = Part.Edge(L1)
E2 = Part.Edge(L2)
E3 = Part.Edge(C1)
E4 = Part.Edge(C2)

E1 = L1.toShape()
E2 = L2.toShape()

W = Part.Wire([E1, E4, E2, E3])

print(W.isClosed())

F = Part.Face(W)

P = F.extrude(FreeCAD.Vector(0, 0, 10))

print(P.ShapeType)

S = W.extrude(FreeCAD.Vector(0, 0, 10))
print(S.ShapeType)

myObj2 = FreeCAD.ActiveDocument.addObject("Part::Feature", "My_Strange_Solid")
myObj2.Shape = P
FreeCAD.ActiveDocument.recompute()

Part.show(P)

Gui.activeDocument().activeView().viewIsometric()
Gui.SendMsgToActiveView("ViewFit")
