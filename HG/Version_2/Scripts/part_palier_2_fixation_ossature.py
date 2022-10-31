import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_palier_2_fixation_ossature"


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

# part_palier_2_fixation_ossature
x = 165
y = 48
z = 84
part_palier_2_fixation_ossature = Part.makeBox(x, y, z)

Da = 30
trou_arbre = Part.makeCylinder(Da/2, y)

# Cut part_palier_2_fixation_ossature by trou_arbre
# rotation trou_arbre
axe_x = FreeCAD.Vector(1, 0, 0)
trou_arbre_vector = FreeCAD.Vector(0, 0, 0)
trou_arbre.rotate(trou_arbre_vector, axe_x, 90)

# translation trou_arbre
trou_arbre_vector = FreeCAD.Vector(x/2, y, 42.9)
trou_arbre.translate(trou_arbre_vector)

part_palier_2_fixation_ossature = part_palier_2_fixation_ossature.cut(trou_arbre)

# Cut part_palier_2_fixation_ossature by trou_vis
D_vis = 17
trou_vis = Part.makeCylinder(D_vis/2, z)

# translation trou_vis
E = 121
A = 165
trou_vis_vector = FreeCAD.Vector((A - E)/2, y/2, 0)
trou_vis.translate(trou_vis_vector)

part_palier_2_fixation_ossature = part_palier_2_fixation_ossature.cut(trou_vis)

# translation trou_vis
trou_vis_vector = FreeCAD.Vector(E, 0, 0)
trou_vis.translate(trou_vis_vector)

part_palier_2_fixation_ossature = part_palier_2_fixation_ossature.cut(trou_vis)

Part.show(part_palier_2_fixation_ossature)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_palier_2_fixation_ossature").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_2/Stl/part_palier_2_fixation_ossature.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'C:\\Users\\Jason\\Documents\\Devs\\Python-Macros-For-FreeCAD\\HG\\Version_2\\Png\\part_palier_2_fixation_ossature_'
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
