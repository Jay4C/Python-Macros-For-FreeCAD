import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_palier_2_fixation_support"


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

# part_palier_2_fixation_support
x = 148
y = 40.2
z = 80
part_palier_2_fixation_support = Part.makeBox(x, y, z)

# Cut part_palier_2_fixation_support by trou_arbre
Da = 30
trou_arbre = Part.makeCylinder(Da/2, y)

# rotation trou_arbre
axe_x = FreeCAD.Vector(1, 0, 0)
trou_arbre_vector = FreeCAD.Vector(0, 0, 0)
trou_arbre.rotate(trou_arbre_vector, axe_x, 90)

# translation trou_arbre
trou_arbre_vector = FreeCAD.Vector(x/2, y, z/2)
trou_arbre.translate(trou_arbre_vector)

part_palier_2_fixation_support = part_palier_2_fixation_support.cut(trou_arbre)

# Cut part_palier_2_fixation_support by trou_vis
D_vis = 16
trou_vis = Part.makeCylinder(D_vis/2, y)

# rotation trou_vis
axe_x = FreeCAD.Vector(1, 0, 0)
trou_vis_vector = FreeCAD.Vector(0, 0, 0)
trou_vis.rotate(trou_vis_vector, axe_x, 90)

# translation trou_vis
E = 117
A = 148
trou_vis_vector = FreeCAD.Vector((A - E)/2, y, z/2)
trou_vis.translate(trou_vis_vector)

part_palier_2_fixation_support = part_palier_2_fixation_support.cut(trou_vis)

# translation trou_vis
trou_vis_vector = FreeCAD.Vector(E, 0, 0)
trou_vis.translate(trou_vis_vector)

part_palier_2_fixation_support = part_palier_2_fixation_support.cut(trou_vis)

Part.show(part_palier_2_fixation_support)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_palier_2_fixation_support").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_2/Stl/part_palier_2_fixation_support.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'C:\\Users\\Jason\\Documents\\Devs\\Python-Macros-For-FreeCAD\\HG\\Version_2\\Png\\part_palier_2_fixation_support_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')
