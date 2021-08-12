import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "equerre_assemblage_plat_l100"


def clear_doc():
    # Clear the active document deleting all the objects
    for obj in DOC.Objects:
        DOC.removeObject(obj.Name)


def setview():
    # Rearrange View
    FreeCAD.Gui.SendMsgToActiveView("ViewFit")
    FreeCAD.Gui.activeDocument().activeView().viewAxometric()


if DOC is None:
    FreeCAD.newDocument(DOC_NAME)
    FreeCAD.setActiveDocument(DOC_NAME)
    DOC = FreeCAD.activeDocument()
else:
    clear_doc()

# EPS= tolerance to use to cut the parts
EPS = 0.10
EPS_C = EPS * -0.5

box_1 = Part.makeBox(100, 15, 2)

cylinder_1 = Part.makeCylinder(6, 3)

# box_1 cut by cilnder_1 in 2 times
cylinder_1_vector = FreeCAD.Vector(8, 7.5, 0)
cylinder_1.translate(cylinder_1_vector)
box_1 = box_1.cut(cylinder_1)

cylinder_1_vector = FreeCAD.Vector(84, 0, 0)
cylinder_1.translate(cylinder_1_vector)
box_1 = box_1.cut(cylinder_1)

Part.show(box_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("equerre_assemblage_plat_l100").getObject("Shape"))

stl_file = u"equerre_assemblage_plat_l100.stl"

Mesh.export(__objs__, stl_file)

setview()
        