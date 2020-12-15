# Box
doc = FreeCAD.newDocument()
box = doc.addObject("Part::Box", "myBox")
doc.recompute()
Gui.activeDocument().activeView().viewIsometric()
Gui.SendMsgToActiveView("ViewFit")
box.Height
box.Height = 5

# Vectors
myvec = FreeCAD.Vector(2, 0, 0)
myvec.x
myvec.y
othervec = FreeCAD.Vector(0, 3, 0)
sumvec = myvec.add(othervec)

# Placements
box.Placement
box.Placement.Base
box.Placement.Base = sumvec
otherpla = FreeCAD.Placement()
box.Placement = otherpla

doc.recompute()

# App and Gui
vo = box.ViewObject
vo.Transparency = 80
vo.hide()
vo.show()

# Modules
doc.supportedTypes()

# Mesh
import Mesh

mymesh = Mesh.createSphere()
mymesh.Facets
mymesh.Points

meshobj = doc.addObject("Mesh::Feature", "MyMesh")
meshobj.Mesh = mymesh
doc.recompute()

# Part
import Part
myshape = Part.makeSphere(10)
myshape.Volume
myshape.Area

shapeobj = doc.addObject("Part::Feature", "MyShape")
shapeobj.Shape = myshape
doc.recompute()

# Draft
import Draft
rec = Draft.makeRectangle(5, 2)
mvec = FreeCAD.Vector(4, 4, 0)
Draft.move(rec, mvec)
Draft.move(box, mvec)

# Interface
from PySide import QtGui
QtGui.QMessageBox.information(None, "Apollo program", "Houston, we have a problem")

Gui.activeDocument().activeView().viewIsometric()
Gui.SendMsgToActiveView("ViewFit")
