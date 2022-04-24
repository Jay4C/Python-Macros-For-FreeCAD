import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_steel_box_tube_for_support_elevator_flywheel"


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

# part_steel_box_tube_for_support_elevator_flywheel
h = 50
l = 50
L = 500 + 50*3
e = 3
part_steel_box_tube_for_support_elevator_flywheel = Part.makeBox(L, h, l)

# Cut part_steel_box_tube_for_support_elevator_flywheel by box_1
box_1 = Part.makeBox(L, h - e*2, l - e*2)
box_1_vector = FreeCAD.Vector(0, e, e)
box_1.translate(box_1_vector)
part_steel_box_tube_for_support_elevator_flywheel = part_steel_box_tube_for_support_elevator_flywheel.cut(box_1)

Part.show(part_steel_box_tube_for_support_elevator_flywheel)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_steel_box_tube_for_support_elevator_flywheel").getObject("Shape"))

stl_file = u"A://///Python__Flask__Cristal_Ball////////part_steel_box_tube_for_support_elevator_flywheel.stl"

Mesh.export(__objs__, stl_file)

setview()
        