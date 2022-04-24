import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_support_flywheel"


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

# assembly_socle
Mesh.insert(u"assembly_socle.stl","assembly_support_flywheel")
FreeCADGui.getDocument("assembly_support_flywheel").getObject("assembly_socle").ShapeColor = (0.10,0.10,0.10)
FreeCAD.getDocument("assembly_support_flywheel").getObject("assembly_socle").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))

height_alternateur = 200
total_number_of_masselottes = 840
number_of_masselottes_per_slice_flywheel_per_block = round(total_number_of_masselottes/4)
radius_flywheel = 500
maximal_radius_masselotte_compiled = round(math.sqrt(math.pow(radius_flywheel, 2) + math.pow(number_of_masselottes_per_slice_flywheel_per_block*20 + 35, 2)))
total_number_of_masselotte_compiled = round((maximal_radius_masselotte_compiled + height_alternateur)/20) - 1

# assembly_flywheel
Mesh.insert(u"assembly_flywheel.stl","assembly_support_flywheel")
FreeCADGui.getDocument("assembly_support_flywheel").getObject("assembly_flywheel").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_support_flywheel").getObject("assembly_flywheel").Placement = App.Placement(App.Vector(0,490,70 + 100 + total_number_of_masselotte_compiled*20 - 2.5),App.Rotation(FreeCAD.Vector(1,0,0),-90))

setview()

# Export assembly_support_flywheel
__objs__ = []
__objs__.append(FreeCAD.getDocument("assembly_support_flywheel").getObject("assembly_socle"))
__objs__.append(FreeCAD.getDocument("assembly_support_flywheel").getObject("assembly_flywheel"))

Mesh.export(__objs__,u"assembly_support_flywheel.stl")

del __objs__

# Generate PNG files
file = 'assembly_support_flywheel_v3_'
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
