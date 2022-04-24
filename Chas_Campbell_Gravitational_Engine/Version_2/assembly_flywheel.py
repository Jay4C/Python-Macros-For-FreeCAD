import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_flywheel"


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

# part_tige_filetee_m20_1000l
Mesh.insert(u"part_tige_filetee_m20_1000l.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_tige_filetee_m20_1000l").ShapeColor = (0.40,0.20,0.10)
FreeCAD.getDocument("assembly_flywheel").getObject("part_tige_filetee_m20_1000l").Placement = App.Placement(App.Vector(600,35,-(1000-20)/2),App.Rotation(App.Vector(0,0,1),0))

# assembly_slice_flywheel - 0
Mesh.insert(u"assembly_slice_flywheel.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("assembly_slice_flywheel").ShapeColor = (0.10,0.20,0.40)
FreeCAD.getDocument("assembly_flywheel").getObject("assembly_slice_flywheel").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_20m for slice_flywheel
Mesh.insert(u"part_rondelle_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_rondelle_20m").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m").Placement = App.Placement(App.Vector(600,35,20),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_20m for slice_flywheel
Mesh.insert(u"part_rondelle_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_rondelle_20m001").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m001").Placement = App.Placement(App.Vector(600,35,-3),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_20m for slice_flywheel
Mesh.insert(u"part_ecrou_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_ecrou_20m").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m").Placement = App.Placement(App.Vector(600,35,20 + 3),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_20m for slice_flywheel
Mesh.insert(u"part_ecrou_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_ecrou_20m001").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m001").Placement = App.Placement(App.Vector(600,35,- 3 - 20),App.Rotation(App.Vector(0,0,1),0))

# For moteur electrique

# part_poulie_volant_inertie
Mesh.insert(u"part_poulie_volant_inertie.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_poulie_volant_inertie").ShapeColor = (0.20,0.40,0.60)
FreeCAD.getDocument("assembly_flywheel").getObject("part_poulie_volant_inertie").Placement = App.Placement(App.Vector(600,35,510 - 22.2 - 10 - 20 - 3),App.Rotation(App.Vector(0,0,1),0))

# part_moyeu_amovible_volant_inertie
Mesh.insert(u"part_moyeu_amovible_volant_inertie.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_moyeu_amovible_volant_inertie").ShapeColor = (0.50,0.50,0.50)
FreeCAD.getDocument("assembly_flywheel").getObject("part_moyeu_amovible_volant_inertie").Placement = App.Placement(App.Vector(600,35,510 - 22.2 - 10 - 20 - 3),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_20m
Mesh.insert(u"part_rondelle_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_rondelle_20m002").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m002").Placement = App.Placement(App.Vector(600,35,510 - 3 - 10 - 20),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_20m
Mesh.insert(u"part_ecrou_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_ecrou_20m002").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m002").Placement = App.Placement(App.Vector(600,35,510 - 20 - 10),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_20m
Mesh.insert(u"part_rondelle_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_rondelle_20m003").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m003").Placement = App.Placement(App.Vector(600,35,510 - 3 - 10 - 20 - 22.2 - 3),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_20m
Mesh.insert(u"part_ecrou_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_ecrou_20m003").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m003").Placement = App.Placement(App.Vector(600,35,510 - 20 - 10 - 20 - 3 - 22.2 - 3),App.Rotation(App.Vector(0,0,1),0))

# For alternateur

# part_poulie_volant_inertie
Mesh.insert(u"part_poulie_volant_inertie.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_poulie_volant_inertie001").ShapeColor = (0.20,0.40,0.60)
FreeCAD.getDocument("assembly_flywheel").getObject("part_poulie_volant_inertie001").Placement = App.Placement(App.Vector(600,35,-512.2 + 22.2 + 10 + 20 + 3),App.Rotation(App.Vector(0,0,1),0))

# part_moyeu_amovible_volant_inertie
Mesh.insert(u"part_moyeu_amovible_volant_inertie.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_moyeu_amovible_volant_inertie001").ShapeColor = (0.50,0.50,0.50)
FreeCAD.getDocument("assembly_flywheel").getObject("part_moyeu_amovible_volant_inertie001").Placement = App.Placement(App.Vector(600,35,-490 + 10 + 20 + 3),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_20m
Mesh.insert(u"part_rondelle_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_rondelle_20m004").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m004").Placement = App.Placement(App.Vector(600,35,-490 + 10 + 20),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_20m
Mesh.insert(u"part_ecrou_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_ecrou_20m004").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m004").Placement = App.Placement(App.Vector(600,35,-490 + 10),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_20m
Mesh.insert(u"part_rondelle_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_rondelle_20m005").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m005").Placement = App.Placement(App.Vector(600,35,-490 + 10 + 20 + 3 + 22.2),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_20m
Mesh.insert(u"part_ecrou_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_ecrou_20m005").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m005").Placement = App.Placement(App.Vector(600,35,-490 + 10 + 20 + 3 + 22.2 + 3),App.Rotation(App.Vector(0,0,1),0))

# For moteur electrique

# part_rondelle_20m
Mesh.insert(u"part_rondelle_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_rondelle_20m006").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m006").Placement = App.Placement(App.Vector(600,35,510 - 3 - 10 - 20 - 22.2 - 3 - 20),App.Rotation(App.Vector(0,0,1),0))

# part_palier
Mesh.insert(u"part_palier.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_palier").ShapeColor = (0.30,0.30,0.30)
FreeCAD.getDocument("assembly_flywheel").getObject("part_palier").Placement = App.Placement(App.Vector(600 - 127/2,35 + 65/2,510 - 38 - 10 - 20 - 3 - 22.2 - 3 - 20),App.Rotation(App.Vector(1,0,0),90))

# part_rondelle_20m
Mesh.insert(u"part_rondelle_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_rondelle_20m007").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m007").Placement = App.Placement(App.Vector(600,35,510 - 3 - 10 - 20 - 3 - 22.2 - 3 - 20 - 38),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_20m
Mesh.insert(u"part_ecrou_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_ecrou_20m006").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m006").Placement = App.Placement(App.Vector(600,35,510 - 20 - 10 - 20 - 3 - 22.2 - 3 - 20 - 38 - 3),App.Rotation(App.Vector(0,0,1),0))

# For alternateur

# part_rondelle_20m
Mesh.insert(u"part_rondelle_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_rondelle_20m008").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m008").Placement = App.Placement(App.Vector(600,35,-490 + 10 + 20 + 3 + 22.2 + 3 + 20),App.Rotation(App.Vector(0,0,1),0))

# part_palier
Mesh.insert(u"part_palier.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_palier001").ShapeColor = (0.30,0.30,0.30)
FreeCAD.getDocument("assembly_flywheel").getObject("part_palier001").Placement = App.Placement(App.Vector(600 - 127/2,35 + 65/2,-490 + 10 + 20 + 3 + 22.2 + 3 + 20 + 3),App.Rotation(App.Vector(1,0,0),90))

# part_rondelle_20m
Mesh.insert(u"part_rondelle_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_rondelle_20m009").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m009").Placement = App.Placement(App.Vector(600,35,-(490 - 10 - 20 - 3 - 22.2 - 3 - 20 - 3 - 38)),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_20m
Mesh.insert(u"part_ecrou_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_ecrou_20m007").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m007").Placement = App.Placement(App.Vector(600,35,-(490 - 10 - 20 - 3 - 22.2 - 3 - 20 -3 - 38 - 3)),App.Rotation(App.Vector(0,0,1),0))

# For assembly_slice_flywheel - 1
# part_rondelle_20m
Mesh.insert(u"part_rondelle_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_rondelle_20m010").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m010").Placement = App.Placement(App.Vector(600,35,20 + 3 + 20),App.Rotation(App.Vector(0,0,1),0))

# assembly_slice_flywheel
Mesh.insert(u"assembly_slice_flywheel.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("assembly_slice_flywheel001").ShapeColor = (0.10,0.20,0.40)
FreeCAD.getDocument("assembly_flywheel").getObject("assembly_slice_flywheel001").Placement = App.Placement(App.Vector(600 + 35,-600 + 35,20 + 3 + 20 + 3),App.Rotation(App.Vector(0,0,1),90))

# part_rondelle_20m
Mesh.insert(u"part_rondelle_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_rondelle_20m011").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m011").Placement = App.Placement(App.Vector(600,35,20 + 3 + 20 + 3 + 20),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_20m
Mesh.insert(u"part_ecrou_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_ecrou_20m008").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m008").Placement = App.Placement(App.Vector(600,35,20 + 3 + 20 + 3 + 20 + 3),App.Rotation(App.Vector(0,0,1),0))

# For assembly_slice_flywheel - 2
# part_rondelle_20m
Mesh.insert(u"part_rondelle_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_rondelle_20m012").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m012").Placement = App.Placement(App.Vector(600,35,-3 - 20),App.Rotation(App.Vector(0,0,1),0))

# assembly_slice_flywheel
Mesh.insert(u"assembly_slice_flywheel.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("assembly_slice_flywheel002").ShapeColor = (0.10,0.20,0.40)
FreeCAD.getDocument("assembly_flywheel").getObject("assembly_slice_flywheel002").Placement = App.Placement(App.Vector(600 + 35,-600 + 35,-20 - 3 - 20),App.Rotation(App.Vector(0,0,1),90))

# part_rondelle_20m
Mesh.insert(u"part_rondelle_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_rondelle_20m013").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m013").Placement = App.Placement(App.Vector(600,35,-3 - 20 - 3 - 20),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_20m
Mesh.insert(u"part_ecrou_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_ecrou_20m009").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m009").Placement = App.Placement(App.Vector(600,35,-20 - 3 - 20 - 3 - 20),App.Rotation(App.Vector(0,0,1),0))

setview()

# Export assembly_flywheel
__objs__ = []
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_tige_filetee_m20_1000l"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("assembly_slice_flywheel"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m001"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m001"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_poulie_volant_inertie"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_moyeu_amovible_volant_inertie"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m002"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m002"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m003"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m003"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_poulie_volant_inertie001"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_moyeu_amovible_volant_inertie001"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m004"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m004"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m005"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m005"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m006"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_palier"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m007"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m006"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m008"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_palier001"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m009"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m007"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m010"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("assembly_slice_flywheel001"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m011"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m008"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m012"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("assembly_slice_flywheel002"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m013"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m009"))

Mesh.export(__objs__,u"assembly_flywheel.stl")

del __objs__

# Generate PNG files
file = 'assembly_flywheel_v2_'
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
