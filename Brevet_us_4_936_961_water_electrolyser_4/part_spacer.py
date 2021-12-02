import FreeCAD, Part, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_spacer"


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

# spacer
spacer = Part.makeCylinder(4.5, 13)

# anode
anode = Part.makeCylinder(2, 13)

# cut spacer by anode
spacer = spacer.cut(anode)

# space_anode_cathode
space_anode_cathode = Part.makeCylinder(4.5, 12)

# space_plus_anode
space_plus_anode = Part.makeCylinder(3, 12)

# space_anode_cathode cut by space_plus_anode
space_anode_cathode = space_anode_cathode.cut(space_plus_anode)

# spacer cut by space_anode_cathode
space_anode_cathode_vector = FreeCAD.Vector(0, 0, 2)
space_anode_cathode.translate(space_anode_cathode_vector)
spacer = spacer.cut(space_anode_cathode)

# space_bubble
degre = 10
for i in range(int(360/degre)):
    radius = 2
    alpha=(i*degre*math.pi)/180
    space_bubble_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    space_bubble = Part.makeCylinder(0.3, 13)
    space_bubble.translate(space_bubble_vector)
    spacer = spacer.cut(space_bubble)

Part.show(spacer)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_spacer").getObject("Shape"))

stl_file = u"part_spacer.stl"

Mesh.export(__objs__, stl_file)

setview()
        