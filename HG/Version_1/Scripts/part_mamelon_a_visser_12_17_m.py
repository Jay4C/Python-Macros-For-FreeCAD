import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_mamelon_a_visser_12_17_m"

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

diametre_maximal = 19

cylinder_1 = Part.makeCylinder(diametre_maximal/2, 19)

cylinder_2 = Part.makeCylinder(11/2, 19)

cylinder_1 = cylinder_1.cut(cylinder_2)

cylinder_3 = Part.makeCylinder(diametre_maximal/2, 8)

cylinder_4 = Part.makeCylinder(16/2, 8)

cylinder_3 = cylinder_3.cut(cylinder_4)

cylinder_1 = cylinder_1.cut(cylinder_3)

cylinder_3_vector = FreeCAD.Vector(0, 0, 11)

cylinder_3.translate(cylinder_3_vector)

cylinder_1 = cylinder_1.cut(cylinder_3)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_mamelon_a_visser_12_17_m").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_mamelon_a_visser_12_17_m.stl"

Mesh.export(__objs__, stl_file)

setview()
