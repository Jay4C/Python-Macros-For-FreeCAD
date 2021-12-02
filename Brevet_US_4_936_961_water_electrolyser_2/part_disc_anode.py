import FreeCAD, Part, math, Mesh

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

# EPS = tolerance to use to cut the parts
EPS = 0.10
EPS_C = EPS * -0.5

# disc_anode
disc_anode = Part.makeBox(162, 140, 5)

# cylinder_screw
cylinder_screw = Part.makeCylinder(2.5, 5)

# Cut the holes for fixing the disc on the bottom support
# hole n�1
cylinder_screw_vector = FreeCAD.Vector(5.5, 5.5, 0)
cylinder_screw.translate(cylinder_screw_vector)
disc_anode = disc_anode.cut(cylinder_screw)

# hole n�2
cylinder_screw_vector = FreeCAD.Vector(151, 0, 0)
cylinder_screw.translate(cylinder_screw_vector)
disc_anode = disc_anode.cut(cylinder_screw)

# hole n�3
cylinder_screw_vector = FreeCAD.Vector(0, 129, 0)
cylinder_screw.translate(cylinder_screw_vector)
disc_anode = disc_anode.cut(cylinder_screw)

# hole n�4
cylinder_screw_vector = FreeCAD.Vector(-151, 0, 0)
cylinder_screw.translate(cylinder_screw_vector)
disc_anode = disc_anode.cut(cylinder_screw)

# Cut the holes for fixing the anodes
cylinder_anode = Part.makeCylinder(2, 5)

cylinder_anode_vector = FreeCAD.Vector(13.5, 11, 0)
cylinder_anode.translate(cylinder_anode_vector)
disc_anode = disc_anode.cut(cylinder_anode)

for w in range(11):
    for l in range(11):
        cylinder_anode_vector = FreeCAD.Vector(math.pow(-1, w)*12, 0, 0)
        cylinder_anode.translate(cylinder_anode_vector)
        disc_anode = disc_anode.cut(cylinder_anode)

    if w < 10:
        cylinder_anode_vector = FreeCAD.Vector(0, 12, 0)
        cylinder_anode.translate(cylinder_anode_vector)
        disc_anode = disc_anode.cut(cylinder_anode)

# box_evidemment_1
box_evidemment_1 = Part.makeBox(140, 3, 5)

box_evidemment_1_vector = FreeCAD.Vector(11, 0, 0)
box_evidemment_1.translate(box_evidemment_1_vector)
disc_anode = disc_anode.cut(box_evidemment_1)

box_evidemment_1_vector = FreeCAD.Vector(0, 137, 0)
box_evidemment_1.translate(box_evidemment_1_vector)
disc_anode = disc_anode.cut(box_evidemment_1)

# box_evidemment_2
box_evidemment_2 = Part.makeBox(3, 110, 5)

box_evidemment_2_vector = FreeCAD.Vector(0, 15, 0)
box_evidemment_2.translate(box_evidemment_2_vector)
disc_anode = disc_anode.cut(box_evidemment_2)

box_evidemment_2_vector = FreeCAD.Vector(159, 0, 0)
box_evidemment_2.translate(box_evidemment_2_vector)
disc_anode = disc_anode.cut(box_evidemment_2)

Part.show(disc_anode)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_disc_anode").getObject("Shape"))

stl_file = u"part_disc_anode.stl"

Mesh.export(__objs__, stl_file)

setview()
