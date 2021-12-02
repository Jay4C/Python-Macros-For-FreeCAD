import FreeCAD, Part, Mesh, math, ImportGui

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_squelette_d35_l80"


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

cylinder_1 = Part.makeCylinder(35/2, 80)

cylinder_2 = Part.makeCylinder(5, 80)

cylinder_3 = Part.makeCylinder(35/2, 37)

cylinder_4 = Part.makeCylinder(26/2, 37)

# cylinder_1 cut by cylinder_2
cylinder_1 = cylinder_1.cut(cylinder_2)

# cylinder_3 cut by cylinder_4
cylinder_3 = cylinder_3.cut(cylinder_4)

# cylinder_1 cut by cylinder_3 in 2 times
cylinder_3_vector = FreeCAD.Vector(0, 0, 2)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)
cylinder_3_vector = FreeCAD.Vector(0, 0, 39)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

# cylinder_1 cut by cylinder_5 in several times
degre = 40
for i in range(int(360/degre)):
    radius = 5 + 1.5 + 2.5
    alpha=(i*degre*math.pi)/180
    cylinder_5_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    cylinder_5 = Part.makeCylinder(2.5, 80)
    cylinder_5.translate(cylinder_5_vector)
    cylinder_1 = cylinder_1.cut(cylinder_5)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_squelette_d35_l80").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Stanley_Meyer/Brevet_US_4_936_961_water_electrolyser_2/part_squelette_d35_l80.stl"

Mesh.export(__objs__, stl_file)

step_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Stanley_Meyer/Brevet_US_4_936_961_water_electrolyser_2/part_squelette_d35_l80.step"

ImportGui.export(__objs__, step_file)

setview()
        