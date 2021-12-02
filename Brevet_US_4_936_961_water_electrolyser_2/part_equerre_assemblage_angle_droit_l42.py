import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_equerre_assemblage_angle_droit_l42"


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

box_1 = Part.makeBox(42, 42, 15)

box_2 = Part.makeBox(40, 40, 15)

# box_1 cut by box_2
box_2_vector = FreeCAD.Vector(2, 2, 0)
box_2.translate(box_2_vector)
box_1 = box_1.cut(box_2)

cylinder_1 = Part.makeCylinder(6, 3)

# box_1 cut by cylinder_1
cylinder_1_vector = FreeCAD.Vector(0, 32.5, 7.5)
cylinder_1.translate(cylinder_1_vector)
axe_y  = FreeCAD.Vector(0, 1, 0)
cylinder_1.rotate(cylinder_1_vector, axe_y, 90)
box_1 = box_1.cut(cylinder_1)

cylinder_2 = Part.makeCylinder(2.5, 3)

# box_1 cut by cylinder_2
cylinder_2_vector = FreeCAD.Vector(35, 0, 7.5)
cylinder_2.translate(cylinder_2_vector)
axe_x = FreeCAD.Vector(1, 0, 0)
cylinder_2.rotate(cylinder_2_vector, axe_x, -90)
box_1 = box_1.cut(cylinder_2)

Part.show(box_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_equerre_assemblage_angle_droit_l42").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Stanley_Meyer/Brevet_US_4_936_961_water_electrolyser_2/part_equerre_assemblage_angle_droit_l42.stl"

Mesh.export(__objs__, stl_file)

setview()
        