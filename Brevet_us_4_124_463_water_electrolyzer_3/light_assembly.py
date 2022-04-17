import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "light_assembly"


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

# Diametre maximal
diametre_maximal = 250

cylinder_1 = Part.makeCylinder(diametre_maximal/2, 6)

cylinder_2 = Part.makeCylinder(diametre_maximal/2 - 25, 3)

cylinder_3 = Part.makeCylinder(diametre_maximal/2 - 25 - 3, 3)

# cylinder_2 cut by cylinder_3
cylinder_2 = cylinder_2.cut(cylinder_3)

# cylinder_1 cut by cylinder_2
cylinder_2_vector = FreeCAD.Vector(0, 0, 3)
cylinder_2.translate(cylinder_2_vector)
cylinder_1 = cylinder_1.cut(cylinder_2)

# holes for fixing the tank
degre = 60
for i in range(int(360/degre)):
    radius = diametre_maximal/2 - 7.5 - 5
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(5, 6)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# holes for fixing the anodes and the cathodes
degre = 180
for i in range(int(360/degre)):
    radius = diametre_maximal/2 - 25 - 3 - 5 - 5 - 5
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(5, 6)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# holes for fixing the bottom support
degres = [90, 210, 330]
for degre in degres:
    radius = diametre_maximal/2 - 7.5 - 5
    alpha=(degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(5, 6)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

Part.show(cylinder_1)

DOC.recompute()

FreeCADGui.getDocument("light_assembly").getObject("Shape").Transparency = 80

# insertion part_rondelle_10m - 0
degre = 60
radius = diametre_maximal/2 - 7.5 - 5
alpha=(degre*math.pi)/180
vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), -2)
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_rondelle_10m.stl", "light_assembly")
FreeCAD.getDocument("light_assembly").getObject("part_rondelle_10m").Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("light_assembly").getObject("part_rondelle_10m").ShapeColor = (1.00,1.00,0.00)

# For placing the part_rondelle_10m
i1 = 1
degres = [120, 180, 240, 300, 360]
for degre in degres:
    radius = diametre_maximal/2 - 7.5 - 5
    alpha=(degre*math.pi)/180
    vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), -2)
    Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_rondelle_10m.stl", "light_assembly")
    FreeCAD.getDocument("light_assembly").getObject("part_rondelle_10m00" + str(i1)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
    FreeCADGui.getDocument("light_assembly").getObject("part_rondelle_10m00" + str(i1)).ShapeColor = (1.00,1.00,0.00)
    i1 += 1

# For placing the part_rondelle_10m
for i in range(6, 8):
    Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_rondelle_10m.stl", "light_assembly")

for i in range(6, 8):
    alpha=(i*180*math.pi)/180
    radius = diametre_maximal/2 - 25 - 3 - 5 - 5 - 5
    vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), -2)
    FreeCAD.getDocument("light_assembly").getObject("part_rondelle_10m00" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
    FreeCADGui.getDocument("light_assembly").getObject("part_rondelle_10m00" + str(i)).ShapeColor = (1.00,1.00,0.00)

# For placing the part_rondelle_10m
i1 = 8
degres = [60, 120, 180, 240, 300, 360]
for degre in degres:
    radius = diametre_maximal/2 - 7.5 - 5
    alpha=(degre*math.pi)/180
    vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 6)
    Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_rondelle_10m.stl", "light_assembly")

    if i1 < 10:
        FreeCAD.getDocument("light_assembly").getObject("part_rondelle_10m00" + str(i1)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("light_assembly").getObject("part_rondelle_10m00" + str(i1)).ShapeColor = (1.00,1.00,0.00)
    else:
        FreeCAD.getDocument("light_assembly").getObject("part_rondelle_10m0" + str(i1)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("light_assembly").getObject("part_rondelle_10m0" + str(i1)).ShapeColor = (1.00,1.00,0.00)

    i1 += 1

# For placing the part_rondelle_10m
for i in range(14, 16):
    Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_rondelle_10m.stl", "light_assembly")

for i in range(14, 16):
    alpha=(i*180*math.pi)/180
    radius = diametre_maximal/2 - 25 - 3 - 5 - 5 - 5
    vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 6)
    FreeCAD.getDocument("light_assembly").getObject("part_rondelle_10m0" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
    FreeCADGui.getDocument("light_assembly").getObject("part_rondelle_10m0" + str(i)).ShapeColor = (1.00,1.00,0.00)

# insertion part_vis_metal_m10_200l - 0
degre = 60
k = 6.40
radius = diametre_maximal/2 - 7.5 - 5
alpha=(degre*math.pi)/180
vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), - 2 - k)
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_vis_metal_m10_200l.stl", "light_assembly")
FreeCAD.getDocument("light_assembly").getObject("part_vis_metal_m10_200l").Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("light_assembly").getObject("part_vis_metal_m10_200l").ShapeColor = (0.00,1.00,1.00)

# For placing the part_vis_metal_m10_200l
i1 = 1
degres = [120, 180, 240, 300, 360]
k = 6.40
for degre in degres:
    radius = diametre_maximal/2 - 7.5 - 5
    alpha=(degre*math.pi)/180
    vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), - 2 - k)
    Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_vis_metal_m10_200l.stl", "light_assembly")
    FreeCAD.getDocument("light_assembly").getObject("part_vis_metal_m10_200l00" + str(i1)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
    FreeCADGui.getDocument("light_assembly").getObject("part_vis_metal_m10_200l00" + str(i1)).ShapeColor = (0.00,1.00,1.00)
    i1 += 1

# insertion part_vis_metal_m10_150l - 0
degre = 180
k = 6.40
radius = diametre_maximal/2 - 25 - 3 - 5 - 5 - 5
alpha=(degre*math.pi)/180
vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), - 2 - k)
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_vis_metal_m10_150l.stl", "light_assembly")
FreeCAD.getDocument("light_assembly").getObject("part_vis_metal_m10_150l").Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("light_assembly").getObject("part_vis_metal_m10_150l").ShapeColor = (0.00,1.00,1.00)

# For placing the part_vis_metal_m10_150l
i1 = 1
degres = [360]
k = 6.40
for degre in degres:
    radius = diametre_maximal/2 - 25 - 3 - 5 - 5 - 5
    alpha=(degre*math.pi)/180
    vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), - 2 - k)
    Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_vis_metal_m10_150l.stl", "light_assembly")
    FreeCAD.getDocument("light_assembly").getObject("part_vis_metal_m10_150l00" + str(i1)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
    FreeCADGui.getDocument("light_assembly").getObject("part_vis_metal_m10_150l00" + str(i1)).ShapeColor = (0.00,1.00,1.00)
    i1 += 1

# insertion part_ecrou_10m - 0
degre = 60
radius = diametre_maximal/2 - 7.5 - 5
alpha=(degre*math.pi)/180
vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 8)
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_ecrou_10m.stl", "light_assembly")
FreeCAD.getDocument("light_assembly").getObject("part_ecrou_10m").Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("light_assembly").getObject("part_ecrou_10m").ShapeColor = (0.00,0.00,1.00)

# For placing the part_ecrou_10m
i1 = 1
degres = [120, 180, 240, 300, 360]
for degre in degres:
    radius = diametre_maximal/2 - 7.5 - 5
    alpha=(degre*math.pi)/180
    vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 8)
    Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_ecrou_10m.stl", "light_assembly")
    FreeCAD.getDocument("light_assembly").getObject("part_ecrou_10m00" + str(i1)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
    FreeCADGui.getDocument("light_assembly").getObject("part_ecrou_10m00" + str(i1)).ShapeColor = (0.00,0.00,1.00)
    i1 += 1

# insertion part_ecrou_10m
degre = 180
radius = diametre_maximal/2 - 25 - 3 - 5 - 5 - 5
alpha=(degre*math.pi)/180
vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 8)
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_ecrou_10m.stl", "light_assembly")
FreeCAD.getDocument("light_assembly").getObject("part_ecrou_10m006").Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("light_assembly").getObject("part_ecrou_10m006").ShapeColor = (0.00,0.00,1.00)

# For placing the part_ecrou_10m
i1 = 7
degres = [360]
for degre in degres:
    radius = diametre_maximal/2 - 25 - 3 - 5 - 5 - 5
    alpha=(degre*math.pi)/180
    vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 8)
    Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_ecrou_10m.stl", "light_assembly")
    FreeCAD.getDocument("light_assembly").getObject("part_ecrou_10m00" + str(i1)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
    FreeCADGui.getDocument("light_assembly").getObject("part_ecrou_10m00" + str(i1)).ShapeColor = (0.00,0.00,1.00)
    i1 += 1

# For placing the part_rondelle_10m
for i in range(16, 18):
    Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_rondelle_10m.stl", "light_assembly")

for i in range(16, 18):
    alpha=(i*180*math.pi)/180
    radius = diametre_maximal/2 - 25 - 3 - 5 - 5 - 5
    vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 8 + 10)
    FreeCAD.getDocument("light_assembly").getObject("part_rondelle_10m0" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
    FreeCADGui.getDocument("light_assembly").getObject("part_rondelle_10m0" + str(i)).ShapeColor = (1.00,1.00,0.00)

# insertion part_capacitor_plate - 0
vector = App.Vector(0, 0, 20)
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_capacitor_plate.stl", "light_assembly")
FreeCAD.getDocument("light_assembly").getObject("part_capacitor_plate").Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 90))
FreeCADGui.getDocument("light_assembly").getObject("part_capacitor_plate").ShapeColor = (0.00,0.50,0.50)

setview()

# Generate PNG files
file = 'light_assembly_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/3/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/3/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/3/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/3/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/3/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/3/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/3/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/3/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/3/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/3/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/3/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/3/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/3/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/3/' + file + str(i) + '.png',1117,388,'Current')
        