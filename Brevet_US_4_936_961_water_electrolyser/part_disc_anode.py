import FreeCAD, Part, Drawing, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_disc_anode"


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

cylinder_1 = Part.makeCylinder(160, 15)
cylinder_2 = Part.makeCylinder(135, 15)
disc = cylinder_1.cut(cylinder_2)

# Cut the holes for fixing the anodes
for i in range(12):
    radius_anode = 150
    alpha=(i*2*math.pi)/12
    cylinder_vector=(radius_anode*math.cos(alpha), radius_anode*math.sin(alpha), 0)
    cylinder_3 = Part.makeCylinder(6.35, 10)
    cylinder_3.translate(cylinder_vector)
    disc = disc.cut(cylinder_3)
    cylinder_4 = Part.makeCylinder(3.5, 15)
    cylinder_4.translate(cylinder_vector)
    disc = disc.cut(cylinder_4)

# Cut the holes for the screws fixing the anodes on the disc
for i in range(12):
    axe_y = FreeCAD.Vector(0, 1, 0)
    axe_z = FreeCAD.Vector(0, 0, 1)
    radius_screw = 133
    alpha = (i*2*math.pi)/12
    cylinder_vector = FreeCAD.Vector(radius_screw*math.cos(alpha), radius_screw*math.sin(alpha), 4.5)
    cylinder = Part.makeCylinder(2.5, 17, cylinder_vector, axe_y)
    cylinder.rotate(cylinder_vector, axe_z, alpha*(360/(2*math.pi)) - 90)
    disc = disc.cut(cylinder)
    
Part.show(disc)

DOC.recompute()

step_file = "C:\\part_disc_anode.stp"

Part.export([disc], step_file) 

setview()
