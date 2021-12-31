import FreeCAD, Part, Drawing, math, Mesh, importDXF

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_electrode_laser_cutting"


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

maximal_diameter = 100

# part_electrode_laser_cutting
part_electrode_laser_cutting = Part.makeCylinder(maximal_diameter/2, 1)

cylinder_1 = Part.makeCylinder(5, 1)

# part_electrode_laser_cutting cut by cylinder_1
part_electrode_laser_cutting = part_electrode_laser_cutting.cut(cylinder_1)

# holes for the thrust
degre = 90
for i in range(int(360/degre)):
    radius = 15
    alpha = (i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(5, 1)
    hole.translate(hole_vector)
    part_electrode_laser_cutting = part_electrode_laser_cutting.cut(hole)

# holes for the thrust
degre = 30
for i in range(int(360/degre)):
    radius = 30
    alpha = (i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(5, 1)
    hole.translate(hole_vector)
    part_electrode_laser_cutting = part_electrode_laser_cutting.cut(hole)

# holes for fixing the electrodes together
degre = 15
for i in range(int(360/degre)):
    radius = 45
    alpha = (i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 1)
    hole.translate(hole_vector)
    part_electrode_laser_cutting = part_electrode_laser_cutting.cut(hole)

Part.show(part_electrode_laser_cutting)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_electrode_laser_cutting").getObject("Shape"))

stl_file = u"part_electrode_laser_cutting.stl"

Mesh.export(__objs__, stl_file)

dxf_file = u"part_electrode_laser_cutting.dxf"

importDXF.export(__objs__, dxf_file)

setview()
