import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_complete_electrolyser"


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

# part_bottom_support
cylinder_1 = Part.makeCylinder(34, 2)

cylinder_2 = Part.makeCylinder(2.5, 2)

cylinder_1 = cylinder_1.cut(cylinder_2)

# holes for fixing the disc anode and the disc cathode
degree = 60
for i in range(int(360/degree)):
    radius = 28.5
    alpha=(i*degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 2)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# holes for letting the gas miwture to go out
for i in range(int(360/degree)):
    radius = 14.25
    alpha=(i*degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(5, 2)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

degrees = [30, 90, 150, -30, -90, -150]

for degree in degrees:
    radius = 24
    alpha=(int(degree)*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(5, 2)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

Part.show(cylinder_1)

DOC.recompute()

# change color of assembly_complete_electrolyser
FreeCADGui.getDocument("assembly_complete_electrolyser").getObject("Shape").ShapeColor = (0.67,0.00,0.00)

# insertion part_vis_metal_m5_l20 - 1
Mesh.insert(u"part_vis_metal_m5_l20.stl", "assembly_complete_electrolyser")
FreeCAD.getDocument("assembly_complete_electrolyser").getObject("part_vis_metal_m5_l20").Placement = App.Placement(App.Vector(84, 0, 0), App.Rotation(App.Vector(1,0,0), 0))
FreeCADGui.getDocument("assembly_complete_electrolyser").getObject("part_vis_metal_m5_l20").ShapeColor = (0.33,1.00,1.00)

DOC.recompute()

__objs__=[]
__objs__.append(FreeCAD.getDocument("assembly_complete_electrolyser").getObject("Shape"))

Mesh.export(__objs__,u"assembly_complete_electrolyser.stl")

del __objs__

setview()
         