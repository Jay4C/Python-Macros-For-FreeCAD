import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly"


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

# part_tank
Mesh.insert(u"part_tank.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_tank").ShapeColor = (0.10,0.10,0.10)
FreeCAD.getDocument("assembly").getObject("part_tank").Placement = App.Placement(App.Vector(0,0,20),App.Rotation(App.Vector(0,0,1),0))
FreeCADGui.getDocument("assembly").getObject("part_tank").Transparency = 80

# part_support_laser_cutting _ 1
Mesh.insert(u"part_support_laser_cutting.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_support_laser_cutting").ShapeColor = (1.00,1.00,0.00)
FreeCAD.getDocument("assembly").getObject("part_support_laser_cutting").Placement = App.Placement(App.Vector(0,0,18),App.Rotation(App.Vector(0,1,0),0))

# part_support_laser_cutting _ 2
Mesh.insert(u"part_support_laser_cutting.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_support_laser_cutting001").ShapeColor = (1.00,1.00,0.00)
FreeCAD.getDocument("assembly").getObject("part_support_laser_cutting001").Placement = App.Placement(App.Vector(0,0,1000 - 20),App.Rotation(App.Vector(0,1,0),0))

# part_vis_metal_m8_50l
Mesh.insert(u"part_vis_metal_m8_50l.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_vis_metal_m8_50l").ShapeColor = (0.60,0.60,0.10)
FreeCAD.getDocument("assembly").getObject("part_vis_metal_m8_50l").Placement = App.Placement(App.Vector(0,0,1000 - 21 - 29 - 5.3),App.Rotation(App.Vector(0,1,0),0))

# part_tige_filetee_m8_1000l for electrode
Mesh.insert(u"part_tige_filetee_m8_1000l.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_tige_filetee_m8_1000l").ShapeColor = (0.50,0.50,0.50)
FreeCAD.getDocument("assembly").getObject("part_tige_filetee_m8_1000l").Placement = App.Placement(App.Vector(0,0,- 21 - 29 - 5.3 - 3),App.Rotation(App.Vector(0,0,1),0))

# part_tige_filetee_m8_1000l for fixing the assembly _ 1
Mesh.insert(u"part_tige_filetee_m8_1000l.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_tige_filetee_m8_1000l001").ShapeColor = (0.50,0.50,0.50)
FreeCAD.getDocument("assembly").getObject("part_tige_filetee_m8_1000l001").Placement = App.Placement(App.Vector(86/2 + 8 + 4,0,0),App.Rotation(App.Vector(0,0,1),0))

# part_tige_filetee_m8_1000l for fixing the assembly _ 2
Mesh.insert(u"part_tige_filetee_m8_1000l.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_tige_filetee_m8_1000l002").ShapeColor = (0.50,0.50,0.50)
FreeCAD.getDocument("assembly").getObject("part_tige_filetee_m8_1000l002").Placement = App.Placement(App.Vector(-86/2 - 8 - 4,0,0),App.Rotation(App.Vector(0,0,1),0))

# Rank 1
# part_rondelle_8m for part_tige_filetee_m8_1000l
Mesh.insert(u"part_rondelle_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_rondelle_8m").ShapeColor = (0.30,0.20,0.20)
FreeCAD.getDocument("assembly").getObject("part_rondelle_8m").Placement = App.Placement(App.Vector(0,0,16.5),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_8m for part_tige_filetee_m8_1000l001
Mesh.insert(u"part_rondelle_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_rondelle_8m001").ShapeColor = (0.30,0.20,0.20)
FreeCAD.getDocument("assembly").getObject("part_rondelle_8m001").Placement = App.Placement(App.Vector(86/2 + 8 + 4,0,16.5),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_8m for part_tige_filetee_m8_1000l002
Mesh.insert(u"part_rondelle_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_rondelle_8m002").ShapeColor = (0.30,0.20,0.20)
FreeCAD.getDocument("assembly").getObject("part_rondelle_8m002").Placement = App.Placement(App.Vector(-86/2 - 8 - 4,0,16.5),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_8m for part_tige_filetee_m8_1000l
Mesh.insert(u"part_ecrou_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_ecrou_8m").ShapeColor = (0.25,0.25,0.20)
FreeCAD.getDocument("assembly").getObject("part_ecrou_8m").Placement = App.Placement(App.Vector(0,0,8.5),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_8m for part_tige_filetee_m8_1000l001
Mesh.insert(u"part_ecrou_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_ecrou_8m001").ShapeColor = (0.25,0.25,0.20)
FreeCAD.getDocument("assembly").getObject("part_ecrou_8m001").Placement = App.Placement(App.Vector(86/2 + 8 + 4,0,8.5),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_8m for part_tige_filetee_m8_1000l002
Mesh.insert(u"part_ecrou_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_ecrou_8m002").ShapeColor = (0.25,0.25,0.20)
FreeCAD.getDocument("assembly").getObject("part_ecrou_8m002").Placement = App.Placement(App.Vector(-86/2 - 8 - 4,0,8.5),App.Rotation(App.Vector(0,0,1),0))

# Rank 2
# part_rondelle_8m for part_tige_filetee_m8_1000l
Mesh.insert(u"part_rondelle_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_rondelle_8m003").ShapeColor = (0.30,0.20,0.20)
FreeCAD.getDocument("assembly").getObject("part_rondelle_8m003").Placement = App.Placement(App.Vector(0,0,20),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_8m for part_tige_filetee_m8_1000l001
Mesh.insert(u"part_rondelle_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_rondelle_8m004").ShapeColor = (0.30,0.20,0.20)
FreeCAD.getDocument("assembly").getObject("part_rondelle_8m004").Placement = App.Placement(App.Vector(86/2 + 8 + 4,0,20),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_8m for part_tige_filetee_m8_1000l002
Mesh.insert(u"part_rondelle_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_rondelle_8m005").ShapeColor = (0.30,0.20,0.20)
FreeCAD.getDocument("assembly").getObject("part_rondelle_8m005").Placement = App.Placement(App.Vector(-86/2 - 8 - 4,0,20),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_8m for part_tige_filetee_m8_1000l
Mesh.insert(u"part_ecrou_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_ecrou_8m003").ShapeColor = (0.25,0.25,0.20)
FreeCAD.getDocument("assembly").getObject("part_ecrou_8m003").Placement = App.Placement(App.Vector(0,0,21.5),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_8m for part_tige_filetee_m8_1000l001
Mesh.insert(u"part_ecrou_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_ecrou_8m004").ShapeColor = (0.25,0.25,0.20)
FreeCAD.getDocument("assembly").getObject("part_ecrou_8m004").Placement = App.Placement(App.Vector(86/2 + 8 + 4,0,21.5),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_8m for part_tige_filetee_m8_1000l002
Mesh.insert(u"part_ecrou_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_ecrou_8m005").ShapeColor = (0.25,0.25,0.20)
FreeCAD.getDocument("assembly").getObject("part_ecrou_8m005").Placement = App.Placement(App.Vector(-86/2 - 8 - 4,0,21.5),App.Rotation(App.Vector(0,0,1),0))

# Rank 3
# part_rondelle_8m for part_tige_filetee_m8_1000l
Mesh.insert(u"part_rondelle_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_rondelle_8m006").ShapeColor = (0.30,0.20,0.20)
FreeCAD.getDocument("assembly").getObject("part_rondelle_8m006").Placement = App.Placement(App.Vector(0,0,1000 - 21.5),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_8m for part_tige_filetee_m8_1000l001
Mesh.insert(u"part_rondelle_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_rondelle_8m007").ShapeColor = (0.30,0.20,0.20)
FreeCAD.getDocument("assembly").getObject("part_rondelle_8m007").Placement = App.Placement(App.Vector(86/2 + 8 + 4,0,1000 - 21.5),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_8m for part_tige_filetee_m8_1000l002
Mesh.insert(u"part_rondelle_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_rondelle_8m008").ShapeColor = (0.30,0.20,0.20)
FreeCAD.getDocument("assembly").getObject("part_rondelle_8m008").Placement = App.Placement(App.Vector(-86/2 - 8 - 4,0,1000 - 21.5),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_8m for part_tige_filetee_m8_1000l
Mesh.insert(u"part_ecrou_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_ecrou_8m006").ShapeColor = (0.25,0.25,0.20)
FreeCAD.getDocument("assembly").getObject("part_ecrou_8m006").Placement = App.Placement(App.Vector(0,0,1000 - 21.5 - 8),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_8m for part_tige_filetee_m8_1000l001
Mesh.insert(u"part_ecrou_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_ecrou_8m007").ShapeColor = (0.25,0.25,0.20)
FreeCAD.getDocument("assembly").getObject("part_ecrou_8m007").Placement = App.Placement(App.Vector(86/2 + 8 + 4,0,1000 - 21.5 - 8),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_8m for part_tige_filetee_m8_1000l002
Mesh.insert(u"part_ecrou_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_ecrou_8m008").ShapeColor = (0.25,0.25,0.20)
FreeCAD.getDocument("assembly").getObject("part_ecrou_8m008").Placement = App.Placement(App.Vector(-86/2 - 8 - 4,0,1000 - 21.5 - 8),App.Rotation(App.Vector(0,0,1),0))

# Rank 4
# part_rondelle_8m for part_tige_filetee_m8_1000l
Mesh.insert(u"part_rondelle_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_rondelle_8m009").ShapeColor = (0.30,0.20,0.20)
FreeCAD.getDocument("assembly").getObject("part_rondelle_8m009").Placement = App.Placement(App.Vector(0,0,1000 - 21 + 3),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_8m for part_tige_filetee_m8_1000l001
Mesh.insert(u"part_rondelle_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_rondelle_8m010").ShapeColor = (0.30,0.20,0.20)
FreeCAD.getDocument("assembly").getObject("part_rondelle_8m010").Placement = App.Placement(App.Vector(86/2 + 8 + 4,0,1000 - 21 + 3),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_8m for part_tige_filetee_m8_1000l002
Mesh.insert(u"part_rondelle_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_rondelle_8m011").ShapeColor = (0.30,0.20,0.20)
FreeCAD.getDocument("assembly").getObject("part_rondelle_8m011").Placement = App.Placement(App.Vector(-86/2 - 8 - 4,0,1000 - 21 + 3),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_8m for part_tige_filetee_m8_1000l
Mesh.insert(u"part_ecrou_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_ecrou_8m009").ShapeColor = (0.25,0.25,0.20)
FreeCAD.getDocument("assembly").getObject("part_ecrou_8m009").Placement = App.Placement(App.Vector(0,0,1000 - 21 + 3 + 1.5),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_8m for part_tige_filetee_m8_1000l001
Mesh.insert(u"part_ecrou_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_ecrou_8m010").ShapeColor = (0.25,0.25,0.20)
FreeCAD.getDocument("assembly").getObject("part_ecrou_8m010").Placement = App.Placement(App.Vector(86/2 + 8 + 4,0,1000 - 21 + 3 + 1.5),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_8m for part_tige_filetee_m8_1000l002
Mesh.insert(u"part_ecrou_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_ecrou_8m011").ShapeColor = (0.25,0.25,0.20)
FreeCAD.getDocument("assembly").getObject("part_ecrou_8m011").Placement = App.Placement(App.Vector(-86/2 - 8 - 4,0,1000 - 21 + 3 + 1.5),App.Rotation(App.Vector(0,0,1),0))

setview()

# Export assembly
__objs__=[]
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_8m008"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_tank"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_8m011"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_8m"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_tige_filetee_m8_1000l002"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_8m005"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_8m007"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_8m010"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_8m003"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_8m006"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_8m005"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_8m004"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_vis_metal_m8_50l"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_8m004"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_8m009"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_8m010"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_8m009"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_support_laser_cutting001"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_8m007"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_8m003"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_8m008"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_tige_filetee_m8_1000l"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_8m001"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_8m006"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_tige_filetee_m8_1000l001"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_8m002"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_8m002"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_support_laser_cutting"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_8m001"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_8m"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_8m011"))

Mesh.export(__objs__,u"assembly.stl")

del __objs__

# Generate PNG files
file = 'assembly_v2_'
# Ombr�
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
