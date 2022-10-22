import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_palier_4_fixations"


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

# part_palier_4_fixations
x = 86
y = x
z = 33.3
part_palier_4_fixations = Part.makeBox(x, y, z)

# cylinder_1
r1 = 4
L1 = z
cylinder_1 = Part.makeCylinder(r1, L1)

# cylinder_2
r2 = 10
L2 = z
cylinder_2 = Part.makeCylinder(r2, L2)

# cut part_palier_4_fixations by trou_arbre
trou_arbre = Part.makeCylinder(r2, z)
trou_arbre_vector = FreeCAD.Vector(x/2, y/2, 0)
trou_arbre.translate(trou_arbre_vector)
part_palier_4_fixations = part_palier_4_fixations.cut(trou_arbre)

# cut part_palier_4_fixations by trou_vis
x1 = (x - 64)/2
y1 = (y - 64)/2
trou_vis = Part.makeCylinder(r1, z)
trou_vis_vector = FreeCAD.Vector(x1, y1, 0)
trou_vis.translate(trou_vis_vector)
part_palier_4_fixations = part_palier_4_fixations.cut(trou_vis)

x1 = 64 + (x - 64)/2
y1 = (y - 64)/2
trou_vis = Part.makeCylinder(r1, z)
trou_vis_vector = FreeCAD.Vector(x1, y1, 0)
trou_vis.translate(trou_vis_vector)
part_palier_4_fixations = part_palier_4_fixations.cut(trou_vis)

x1 = (x - 64)/2
y1 = 64 + (y - 64)/2
trou_vis = Part.makeCylinder(r1, z)
trou_vis_vector = FreeCAD.Vector(x1, y1, 0)
trou_vis.translate(trou_vis_vector)
part_palier_4_fixations = part_palier_4_fixations.cut(trou_vis)

x1 = 64 + (x - 64)/2
y1 = 64 + (y - 64)/2
trou_vis = Part.makeCylinder(r1, z)
trou_vis_vector = FreeCAD.Vector(x1, y1, 0)
trou_vis.translate(trou_vis_vector)
part_palier_4_fixations = part_palier_4_fixations.cut(trou_vis)

# Show part
Part.show(part_palier_4_fixations)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_palier_4_fixations").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_palier_4_fixations.stl"

Mesh.export(__objs__, stl_file)

setview()
