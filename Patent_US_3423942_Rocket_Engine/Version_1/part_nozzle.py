import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_nozzle"


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

diametre_maximal_of_nozzle_front = 85

# part_nozzle
part_nozzle = Part.makeCylinder(diametre_maximal_of_nozzle_front/2, 3)

# part_nozzle cut by cylinder_1
cylinder_1 = Part.makeCylinder(diametre_maximal_of_nozzle_front/2 - 3.5 - 5 - 4.5 - 2, 3)
part_nozzle = part_nozzle.cut(cylinder_1)

# holes for fixing the nozzle
degree = 60
for i in range(int(360/degree)):
    radius = diametre_maximal_of_nozzle_front/2 - 2.5 - 3.5
    alpha=(i*degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 3)
    hole.translate(hole_vector)
    part_nozzle = part_nozzle.cut(hole)

# cone_1
cone_1_radius_1 = diametre_maximal_of_nozzle_front/2 - 3.5 - 5 - 4.5
cone_1_radius_2 = 20/2
cone_1_height = 50
cone_1 = Part.makeCone(cone_1_radius_1, cone_1_radius_2, cone_1_height)    

# cone_2
cone_2_radius_1 = cone_1_radius_1 - 2
cone_2_radius_2 = cone_1_radius_2 - 2
cone_2_height = 50
cone_2 = Part.makeCone(cone_2_radius_1, cone_2_radius_2, cone_2_height)    

# cone_1 cut by cone_2
cone_1 = cone_1.cut(cone_2)

# part_nozzle fused with cone_1
cone_1_vector = FreeCAD.Vector(0, 0, 3)
cone_1.translate(cone_1_vector)
part_nozzle = part_nozzle.fuse(cone_1)

# cone_3
cone_3_radius_1 = 20/2
cone_3_radius_2 = diametre_maximal_of_nozzle_front/2
cone_3_height = 100
cone_3 = Part.makeCone(cone_3_radius_1, cone_3_radius_2, cone_3_height)    

# cone_4
cone_4_radius_1 = cone_3_radius_1 - 2
cone_4_radius_2 = cone_3_radius_2 - 2
cone_4_height = 100
cone_4 = Part.makeCone(cone_4_radius_1, cone_4_radius_2, cone_4_height)    

# cone_3 cut by cone_4
cone_3 = cone_3.cut(cone_4)

# part_nozzle fused with cone_3
cone_3_vector = FreeCAD.Vector(0, 0, 3 + cone_1_height)
cone_3.translate(cone_3_vector)
part_nozzle = part_nozzle.fuse(cone_3)

Part.show(part_nozzle)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_nozzle").getObject("Shape"))

stl_file = u"part_nozzle.stl"

Mesh.export(__objs__, stl_file)

setview()
