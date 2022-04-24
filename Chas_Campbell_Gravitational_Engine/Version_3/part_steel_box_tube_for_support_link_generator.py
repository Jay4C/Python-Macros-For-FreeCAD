import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_steel_box_tube_for_support_link_generator"


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

# part_steel_box_tube_for_support_link_generator
h = 50
l = 50
L = 806
e = 3
part_steel_box_tube_for_support_link_generator = Part.makeBox(L, h, l)

# Cut part_steel_box_tube_for_support_link_generator by box_1
box_1 = Part.makeBox(L, h - e*2, l - e*2)
box_1_vector = FreeCAD.Vector(0, e, e)
box_1.translate(box_1_vector)
part_steel_box_tube_for_support_link_generator = part_steel_box_tube_for_support_link_generator.cut(box_1)

Part.show(part_steel_box_tube_for_support_link_generator)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_steel_box_tube_for_support_link_generator").getObject("Shape"))

stl_file = u"A://///Python__Flask__Cristal_Ball////////part_steel_box_tube_for_support_link_generator.stl"

Mesh.export(__objs__, stl_file)

setview()
        