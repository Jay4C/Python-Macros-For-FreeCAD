import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_support"


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

# tube diameter
d_tube = 140 + 10*2 + 5*2

# nut diameter
d_nut = 24

# main diameter
d1 = d_tube + 5*2 + 2*2 + d_nut*2 + 2*2

# maximum length
h1 = (700 - 170)/2

# hole length
h2 = h1 - 5

# inner diamter for fixing the tube
d_inner_tube = d_tube

# radius for fixing the device
r_f_d = (d_tube + 5*2 + 2*2 + d_nut)/2

# screw diameter
d_vis = 12.1

d3 = d1

d4 = d_tube + 5*2

d_arbre = 20.1

# part_palier_4_fixations dimensions
r_f_p = math.sqrt(math.pow(32, 2) + math.pow(32, 2))

d_mamelon = 16

d_vis_palier = 8.1

# Cylinder_1
cylinder_1 = Part.makeCylinder(d1/2, h1)

# Cut cylinder_1 by cylinder_2
cylinder_2 = Part.makeCylinder(d_inner_tube/2, h2)
cylinder_1 = cylinder_1.cut(cylinder_2)

# holes for fixing the device
degre = 15
for i in range(int(360/degre)):
    radius = r_f_d
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(d_vis/2, h1)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# Cylinder_3
cylinder_3 = Part.makeCylinder(d3/2, h2)

# Cut cylinder_3 by cylinder_4
cylinder_4 = Part.makeCylinder(d4/2, h2)
cylinder_3 = cylinder_3.cut(cylinder_4)

# Cut cylinder_1 by cylinder_3
cylinder_3_vector = FreeCAD.Vector(0, 0, 5)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

# Cut cylinder_1 by cylinder_5
cylinder_5 = Part.makeCylinder(d_arbre/2, h1)
cylinder_1 = cylinder_1.cut(cylinder_5)

# cut cylinder_1 by trou_vis for fixing the part_palier_4_fixations
for degre in [45, 45*3, 45*5, 45*7]:
    radius = r_f_p
    alpha = (degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(d_vis_palier/2, h1)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# cut cylinder_1 by trou_mamelon for fixing the mamelon to poor mercury
for degre in [90]:
    radius = (86 + 25 + d_mamelon)/2
    alpha = (degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(d_mamelon/2, h1)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

Part.show(cylinder_1)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_support").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_support.stl"

Mesh.export(__objs__, stl_file)

setview()
