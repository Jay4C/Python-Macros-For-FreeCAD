import FreeCAD, Part, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_top_support"


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
EPS_C = EPS * (-0.5)

# top_support
top_support = Part.makeBox(200, 200, 6)

# cylinder
cylinder = Part.makeCylinder(2.5, 6)

# top_support cut by cylinder for hole 1
cylinder_vector = FreeCAD.Vector(5.5, 5.5, 0)
cylinder.translate(cylinder_vector)
top_support = top_support.cut(cylinder)

# top_support cut by cylinder for intermediate holes
for i in range(19):
    cylinder_vector = FreeCAD.Vector(9.45, 0, 0)
    cylinder.translate(cylinder_vector)
    top_support = top_support.cut(cylinder)

# top_support cut by cylinder for hole 2
cylinder_vector = FreeCAD.Vector(9.45, 0, 0)
cylinder.translate(cylinder_vector)
top_support = top_support.cut(cylinder)

# top_support cut by cylinder for intermediate holes
for i in range(19):
    cylinder_vector = FreeCAD.Vector(0, 9.45, 0)
    cylinder.translate(cylinder_vector)
    top_support = top_support.cut(cylinder)

# top_support cut by cylinder for hole 3
cylinder_vector = FreeCAD.Vector(0, 9.45, 0)
cylinder.translate(cylinder_vector)
top_support = top_support.cut(cylinder)

# top_support cut by cylinder for intermediate holes
for i in range(19):
    cylinder_vector = FreeCAD.Vector(-9.45, 0, 0)
    cylinder.translate(cylinder_vector)
    top_support = top_support.cut(cylinder)

# top_support cut by cylinder for hole 4
cylinder_vector = FreeCAD.Vector(-9.45, 0, 0)
cylinder.translate(cylinder_vector)
top_support = top_support.cut(cylinder)

# top_support cut by cylinder for intermediate holes
for i in range(19):
    cylinder_vector = FreeCAD.Vector(0, -9.45, 0)
    cylinder.translate(cylinder_vector)
    top_support = top_support.cut(cylinder)

# box_1
box_1 = Part.makeBox(168, 168, 3)
box_1_vector = FreeCAD.Vector(16, 16, 0)
box_1.translate(box_1_vector)

# top_support cut by box_1
top_support = top_support.cut(box_1)

# box_2
box_2 = Part.makeBox(200, 200, 3)

# box_3
box_3 = Part.makeBox(172, 172, 3)
box_3_vector = FreeCAD.Vector(14, 14, 0)
box_3.translate(box_3_vector)

# box_2 cut by box_3
box_2 = box_2.cut(box_3)

# top_support cut by box_2
top_support = top_support.cut(box_2)

# cylinder_1 for volume sensor
cylinder_1 = Part.makeCylinder(4, 6)
cylinder_1_vector = FreeCAD.Vector(100, 100, 0)
cylinder_1.translate(cylinder_1_vector)

# top_support cut by cylinder_1
top_support = top_support.cut(cylinder_1)

# cylinder_2 for gas sensor to computer
cylinder_2 = Part.makeCylinder(8.5, 6)
cylinder_2_vector = FreeCAD.Vector(47.5, 47.5, 0)
cylinder_2.translate(cylinder_2_vector)

# top_support cut by cylinder_2
top_support = top_support.cut(cylinder_2)

# cylinder_3 for gas sensor to human eye
cylinder_3 = Part.makeCylinder(8.5, 6)
cylinder_3_vector = FreeCAD.Vector(47.5, 152.5, 0)
cylinder_3.translate(cylinder_3_vector)

# top_support cut by cylinder_3
top_support = top_support.cut(cylinder_3)

# cylinder_4 for water input
cylinder_4 = Part.makeCylinder(8.5, 6)
cylinder_4_vector = FreeCAD.Vector(152.5, 47.5, 0)
cylinder_4.translate(cylinder_4_vector)

# top_support cut by cylinder_4
top_support = top_support.cut(cylinder_4)

# cylinder_5 for gas output
cylinder_5 = Part.makeCylinder(8.5, 6)
cylinder_5_vector = FreeCAD.Vector(152.5, 152.5, 0)
cylinder_5.translate(cylinder_5_vector)

# top_support cut by cylinder_5
top_support = top_support.cut(cylinder_5)

Part.show(top_support)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_top_support").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Stanley_Meyer/Brevet_US_4_936_961_water_electrolyser_2/part_top_support.stl"

Mesh.export(__objs__, stl_file)

setview()
