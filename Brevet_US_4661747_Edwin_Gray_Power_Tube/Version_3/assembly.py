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
FreeCAD.getDocument("assembly").getObject("part_tank").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))
FreeCADGui.getDocument("assembly").getObject("part_tank").Transparency = 80

# part_support_laser_cutting _ 1
Mesh.insert(u"part_support_laser_cutting.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_support_laser_cutting").ShapeColor = (1.00,1.00,0.00)
FreeCAD.getDocument("assembly").getObject("part_support_laser_cutting").Placement = App.Placement(App.Vector(0,0,-2),App.Rotation(App.Vector(0,1,0),0))

# part_tige_filetee_m8_1000l for the cathode
Mesh.insert(u"part_tige_filetee_m8_1000l.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_tige_filetee_m8_1000l").ShapeColor = (0.50,0.50,0.50)
FreeCAD.getDocument("assembly").getObject("part_tige_filetee_m8_1000l").Placement = App.Placement(App.Vector(50/2 - 4 - 4, 0, -20),App.Rotation(App.Vector(0,0,1),0))

# part_tige_filetee_m8_1000l for the anode
Mesh.insert(u"part_tige_filetee_m8_1000l.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_tige_filetee_m8_1000l001").ShapeColor = (0.50,0.50,0.50)
FreeCAD.getDocument("assembly").getObject("part_tige_filetee_m8_1000l001").Placement = App.Placement(App.Vector(-50/2 + 4 + 4, 0, -20),App.Rotation(App.Vector(0,0,1),0))

# Rank 1
# part_rondelle_8m for part_tige_filetee_m8_1000l
Mesh.insert(u"part_rondelle_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_rondelle_8m").ShapeColor = (0.30,0.20,0.20)
FreeCAD.getDocument("assembly").getObject("part_rondelle_8m").Placement = App.Placement(App.Vector(50/2 - 4 - 4, 0, -3.5),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_8m for part_tige_filetee_m8_1000l001
Mesh.insert(u"part_rondelle_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_rondelle_8m001").ShapeColor = (0.30,0.20,0.20)
FreeCAD.getDocument("assembly").getObject("part_rondelle_8m001").Placement = App.Placement(App.Vector(-50/2 + 4 + 4, 0, -3.5),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_8m for part_tige_filetee_m8_1000l
Mesh.insert(u"part_ecrou_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_ecrou_8m").ShapeColor = (0.25,0.25,0.20)
FreeCAD.getDocument("assembly").getObject("part_ecrou_8m").Placement = App.Placement(App.Vector(50/2 - 4 - 4, 0, -11.5),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_8m for part_tige_filetee_m8_1000l001
Mesh.insert(u"part_ecrou_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_ecrou_8m001").ShapeColor = (0.25,0.25,0.20)
FreeCAD.getDocument("assembly").getObject("part_ecrou_8m001").Placement = App.Placement(App.Vector(-50/2 + 4 + 4, 0, -11.5),App.Rotation(App.Vector(0,0,1),0))

# Rank 2
# part_rondelle_8m for part_tige_filetee_m8_1000l
Mesh.insert(u"part_rondelle_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_rondelle_8m002").ShapeColor = (0.30,0.20,0.20)
FreeCAD.getDocument("assembly").getObject("part_rondelle_8m002").Placement = App.Placement(App.Vector(50/2 - 4 - 4, 0, 0),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_8m for part_tige_filetee_m8_1000l001
Mesh.insert(u"part_rondelle_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_rondelle_8m003").ShapeColor = (0.30,0.20,0.20)
FreeCAD.getDocument("assembly").getObject("part_rondelle_8m003").Placement = App.Placement(App.Vector(-50/2 + 4 + 4, 0, 0),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_8m for part_tige_filetee_m8_1000l
Mesh.insert(u"part_ecrou_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_ecrou_8m002").ShapeColor = (0.25,0.25,0.20)
FreeCAD.getDocument("assembly").getObject("part_ecrou_8m002").Placement = App.Placement(App.Vector(50/2 - 4 - 4, 0, 1.5),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_8m for part_tige_filetee_m8_1000l001
Mesh.insert(u"part_ecrou_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_ecrou_8m003").ShapeColor = (0.25,0.25,0.20)
FreeCAD.getDocument("assembly").getObject("part_ecrou_8m003").Placement = App.Placement(App.Vector(-50/2 + 4 + 4, 0, 1.5),App.Rotation(App.Vector(0,0,1),0))

number_of_steps_electrode = 180

number_of_steps = number_of_steps_electrode * 2 + 2

# insertion part_rondelle_8m for the cathode
for i in range(0, number_of_steps):
    location = (2.5*i + 9.5)
    
    if i < 6:
        Mesh.insert(u"part_rondelle_8m.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_rondelle_8m00" + str(i+4)).Placement = App.Placement(App.Vector(50/2 - 4 - 4, 0, location), App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_rondelle_8m00" + str(i+4)).ShapeColor = (0.30,0.20,0.20)
    elif i < 96:
        Mesh.insert(u"part_rondelle_8m.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_rondelle_8m0" + str(i+4)).Placement = App.Placement(App.Vector(50/2 - 4 - 4, 0, location), App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_rondelle_8m0" + str(i+4)).ShapeColor = (0.30,0.20,0.20)
    else:
        Mesh.insert(u"part_rondelle_8m.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_rondelle_8m" + str(i+4)).Placement = App.Placement(App.Vector(50/2 - 4 - 4, 0, location), App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_rondelle_8m" + str(i+4)).ShapeColor = (0.30,0.20,0.20)
        
# insertion part_rondelle_8m for the anode
for i in range(0, number_of_steps):
    location = (2.5*i + 9.5)
    
    Mesh.insert(u"part_rondelle_8m.stl", "assembly")
    FreeCAD.getDocument("assembly").getObject("part_rondelle_8m" + str(i + number_of_steps + 4)).Placement = App.Placement(App.Vector(-50/2 + 4 + 4, 0, location), App.Rotation(App.Vector(0,0,1), 0))
    FreeCADGui.getDocument("assembly").getObject("part_rondelle_8m" + str(i + number_of_steps +4)).ShapeColor = (0.30,0.20,0.20)

# insertion part_electrode_laser_cutting for the cathode
Mesh.insert(u"part_electrode_laser_cutting.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_electrode_laser_cutting").Placement = App.Placement(App.Vector(0, 0, 11), App.Rotation(App.Vector(0, 0, 1), 0))
FreeCADGui.getDocument("assembly").getObject("part_electrode_laser_cutting").ShapeColor = (0.60,0.40,0.20)

for i in range(0, number_of_steps_electrode):
    location = 5*i + 16
    
    if i < 9:
        Mesh.insert(u"part_electrode_laser_cutting.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_electrode_laser_cutting00" + str(i+1)).Placement = App.Placement(App.Vector(0, 0, location), App.Rotation(App.Vector(0, 0, 1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_electrode_laser_cutting00" + str(i+1)).ShapeColor = (0.60,0.40,0.20)
    elif i < 99:
        Mesh.insert(u"part_electrode_laser_cutting.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_electrode_laser_cutting0" + str(i+1)).Placement = App.Placement(App.Vector(0, 0, location), App.Rotation(App.Vector(0, 0, 1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_electrode_laser_cutting0" + str(i+1)).ShapeColor = (0.60,0.40,0.20)
    else:
        Mesh.insert(u"part_electrode_laser_cutting.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_electrode_laser_cutting" + str(i+1)).Placement = App.Placement(App.Vector(0, 0, location), App.Rotation(App.Vector(0, 0, 1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_electrode_laser_cutting" + str(i+1)).ShapeColor = (0.60,0.40,0.20)

# insertion part_electrode_laser_cutting for the anode
for i in range(0, number_of_steps_electrode):
    location = 5*i + 13.5
    
    Mesh.insert(u"part_electrode_laser_cutting.stl", "assembly")
    FreeCAD.getDocument("assembly").getObject("part_electrode_laser_cutting" + str(i + number_of_steps_electrode + 1)).Placement = App.Placement(App.Vector(0, 0, location), App.Rotation(App.Vector(0, 0, 1), 180))
    FreeCADGui.getDocument("assembly").getObject("part_electrode_laser_cutting" + str(i + number_of_steps_electrode + 1)).ShapeColor = (0.20,0.40,0.60)

setview()

# Generate PNG files
file = 'assembly_v3_'
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
