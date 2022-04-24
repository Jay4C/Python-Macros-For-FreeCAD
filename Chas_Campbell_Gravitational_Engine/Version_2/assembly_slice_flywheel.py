import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_slice_flywheel"


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

# part_support_masselotte
Mesh.insert(u"part_support_masselotte.stl","assembly_slice_flywheel")
FreeCADGui.getDocument("assembly_slice_flywheel").getObject("part_support_masselotte").ShapeColor = (0.10,0.10,0.10)
FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_support_masselotte").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))

number_of_masselottes = 56
i1 = round((number_of_masselottes/4)*1)
i2 = round((number_of_masselottes/4)*2)
i3 = round((number_of_masselottes/4)*3)
i4 = round((number_of_masselottes/4)*4)

# part_masselotte
for i in range(0, i1):
    x = 1000
    y = -i * 20
    z = -25
    
    if i == 0:
        Mesh.insert(u"part_masselotte.stl","assembly_slice_flywheel")
        FreeCADGui.getDocument("assembly_slice_flywheel").getObject("part_masselotte").ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))
    elif i >= 1 and i < 10:
        Mesh.insert(u"part_masselotte.stl","assembly_slice_flywheel")
        FreeCADGui.getDocument("assembly_slice_flywheel").getObject("part_masselotte00" + str(i)).ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte00" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))
    elif i >= 10 and i < 100:
        Mesh.insert(u"part_masselotte.stl","assembly_slice_flywheel")
        FreeCADGui.getDocument("assembly_slice_flywheel").getObject("part_masselotte0" + str(i)).ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))
    elif i >= 100 and i < 1000:
        Mesh.insert(u"part_masselotte.stl","assembly_slice_flywheel")
        FreeCADGui.getDocument("assembly_slice_flywheel").getObject("part_masselotte" + str(i)).ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))
            
# part_masselotte
for i in range(i1, i2):
    x = 1000
    y = 90 + 20 * (i - i1)
    z = -25
    
    if i == 0:
        Mesh.insert(u"part_masselotte.stl","assembly_slice_flywheel")
        FreeCADGui.getDocument("assembly_slice_flywheel").getObject("part_masselotte").ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))
    elif i >= 1 and i < 10:
        Mesh.insert(u"part_masselotte.stl","assembly_slice_flywheel")
        FreeCADGui.getDocument("assembly_slice_flywheel").getObject("part_masselotte00" + str(i)).ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte00" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))
    elif i >= 10 and i < 100:
        Mesh.insert(u"part_masselotte.stl","assembly_slice_flywheel")
        FreeCADGui.getDocument("assembly_slice_flywheel").getObject("part_masselotte0" + str(i)).ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))
    elif i >= 100 and i < 1000:
        Mesh.insert(u"part_masselotte.stl","assembly_slice_flywheel")
        FreeCADGui.getDocument("assembly_slice_flywheel").getObject("part_masselotte" + str(i)).ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))

# part_masselotte
for i in range(i2, i3):
    x = 0
    y = -20 * (i - i2)
    z = -25
    
    if i == 0:
        Mesh.insert(u"part_masselotte.stl","assembly_slice_flywheel")
        FreeCADGui.getDocument("assembly_slice_flywheel").getObject("part_masselotte").ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))
    elif i >= 1 and i < 10:
        Mesh.insert(u"part_masselotte.stl","assembly_slice_flywheel")
        FreeCADGui.getDocument("assembly_slice_flywheel").getObject("part_masselotte00" + str(i)).ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte00" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))
    elif i >= 10 and i < 100:
        Mesh.insert(u"part_masselotte.stl","assembly_slice_flywheel")
        FreeCADGui.getDocument("assembly_slice_flywheel").getObject("part_masselotte0" + str(i)).ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))
    elif i >= 100 and i < 1000:
        Mesh.insert(u"part_masselotte.stl","assembly_slice_flywheel")
        FreeCADGui.getDocument("assembly_slice_flywheel").getObject("part_masselotte" + str(i)).ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))

# part_masselotte
for i in range(i3, i4):
    x = 0
    y = 90 + 20 * (i - i3)
    z = -25
    
    if i == 0:
        Mesh.insert(u"part_masselotte.stl","assembly_slice_flywheel")
        FreeCADGui.getDocument("assembly_slice_flywheel").getObject("part_masselotte").ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))
    elif i >= 1 and i < 10:
        Mesh.insert(u"part_masselotte.stl","assembly_slice_flywheel")
        FreeCADGui.getDocument("assembly_slice_flywheel").getObject("part_masselotte00" + str(i)).ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte00" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))
    elif i >= 10 and i < 100:
        Mesh.insert(u"part_masselotte.stl","assembly_slice_flywheel")
        FreeCADGui.getDocument("assembly_slice_flywheel").getObject("part_masselotte0" + str(i)).ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))
    elif i >= 100 and i < 1000:
        Mesh.insert(u"part_masselotte.stl","assembly_slice_flywheel")
        FreeCADGui.getDocument("assembly_slice_flywheel").getObject("part_masselotte" + str(i)).ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))

setview()

# Export assembly_slice_flywheel
__objs__=[]
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_support_masselotte"))

for i in range(0, i1):
    if i == 0:
        __objs__.append(FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte"))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte" + str(i)))

for i in range(i1, i2):
    if i == 0:
        __objs__.append(FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte"))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte" + str(i)))

for i in range(i2, i3):
    if i == 0:
        __objs__.append(FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte"))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte" + str(i)))
    
for i in range(i3, i4):
    if i == 0:
        __objs__.append(FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte"))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte" + str(i)))

Mesh.export(__objs__,u"assembly_slice_flywheel.stl")

del __objs__

# Generate PNG files
file = 'assembly_slice_flywheel_v2_'
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
