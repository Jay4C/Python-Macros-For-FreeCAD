import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_squelette_primaire_d80_l80"


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

cylinder_1 = Part.makeCylinder(40, 80)

cylinder_2 = Part.makeCylinder(5, 80)

# cylinder_1 cut by cylinder_2
cylinder_1 = cylinder_1.cut(cylinder_2)

cylinder_3 = Part.makeCylinder(40, 33.5)

cylinder_4 = Part.makeCylinder(26/2, 33.5)

# cylinder_3 cut by cylinder_4
cylinder_3 = cylinder_3.cut(cylinder_4)

# cylinder_1 cut by cylinder_3 in 2 times
cylinder_3_vector = FreeCAD.Vector(0, 0, 2)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)
cylinder_3_vector = FreeCAD.Vector(0, 0, 42.5)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

cylinder_5 = Part.makeCylinder(40, 5)

cylinder_6 = Part.makeCylinder(26/2, 5)

# cylinder_5 cut by cylinder_6
cylinder_5 = cylinder_5.cut(cylinder_6)

# cylinder_1 cut by cylinder_5
cylinder_5_vector = FreeCAD.Vector(0, 0, 37.5)
cylinder_5.translate(cylinder_5_vector)
cylinder_1 = cylinder_1.cut(cylinder_5)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_squelette_primaire_d80_l80").getObject("Shape"))

stl_file = u"part_squelette_primaire_d80_l80.stl"

Mesh.export(__objs__, stl_file)

setview()
        