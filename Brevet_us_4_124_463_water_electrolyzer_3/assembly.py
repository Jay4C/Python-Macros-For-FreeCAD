import FreeCAD, Part, Mesh, math

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

FreeCADGui.getDocument("assembly").getObject("Shape").Transparency = 80

# insertion part_rondelle_10m - 0
degre = 60
radius = diametre_maximal/2 - 7.5 - 5
alpha=(degre*math.pi)/180
vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), -2)
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_rondelle_10m.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_rondelle_10m").Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_rondelle_10m").ShapeColor = (1.00,1.00,0.00)

# For placing the part_rondelle_10m
i1 = 1
degres = [120, 180, 240, 300, 360]
for degre in degres:
    radius = diametre_maximal/2 - 7.5 - 5
    alpha=(degre*math.pi)/180
    vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), -2)
    Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_rondelle_10m.stl", "assembly")
    FreeCAD.getDocument("assembly").getObject("part_rondelle_10m00" + str(i1)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
    FreeCADGui.getDocument("assembly").getObject("part_rondelle_10m00" + str(i1)).ShapeColor = (1.00,1.00,0.00)
    i1 += 1

# For placing the part_rondelle_10m
for i in range(6, 8):
    Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_rondelle_10m.stl", "assembly")

for i in range(6, 8):
    alpha=(i*180*math.pi)/180
    radius = diametre_maximal/2 - 25 - 3 - 5 - 5 - 5
    vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), -2)
    FreeCAD.getDocument("assembly").getObject("part_rondelle_10m00" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
    FreeCADGui.getDocument("assembly").getObject("part_rondelle_10m00" + str(i)).ShapeColor = (1.00,1.00,0.00)

# For placing the part_rondelle_10m
i1 = 8
degres = [60, 120, 180, 240, 300, 360]
for degre in degres:
    radius = diametre_maximal/2 - 7.5 - 5
    alpha=(degre*math.pi)/180
    vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 6)
    Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_rondelle_10m.stl", "assembly")
    
    if i1 < 10:
        FreeCAD.getDocument("assembly").getObject("part_rondelle_10m00" + str(i1)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_rondelle_10m00" + str(i1)).ShapeColor = (1.00,1.00,0.00)
    else:
        FreeCAD.getDocument("assembly").getObject("part_rondelle_10m0" + str(i1)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_rondelle_10m0" + str(i1)).ShapeColor = (1.00,1.00,0.00)
    
    i1 += 1

# For placing the part_rondelle_10m
for i in range(14, 16):
    Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_rondelle_10m.stl", "assembly")

for i in range(14, 16):
    alpha=(i*180*math.pi)/180
    radius = diametre_maximal/2 - 25 - 3 - 5 - 5 - 5
    vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 6)
    FreeCAD.getDocument("assembly").getObject("part_rondelle_10m0" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
    FreeCADGui.getDocument("assembly").getObject("part_rondelle_10m0" + str(i)).ShapeColor = (1.00,1.00,0.00)

# insertion part_vis_metal_m10_200l - 0
degre = 60
k = 6.40
radius = diametre_maximal/2 - 7.5 - 5
alpha=(degre*math.pi)/180
vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), - 2 - k)
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_vis_metal_m10_200l.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_vis_metal_m10_200l").Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_vis_metal_m10_200l").ShapeColor = (0.00,1.00,1.00)

# For placing the part_vis_metal_m10_200l
i1 = 1
degres = [120, 180, 240, 300, 360]
k = 6.40
for degre in degres:
    radius = diametre_maximal/2 - 7.5 - 5
    alpha=(degre*math.pi)/180
    vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), - 2 - k)
    Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_vis_metal_m10_200l.stl", "assembly")
    FreeCAD.getDocument("assembly").getObject("part_vis_metal_m10_200l00" + str(i1)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
    FreeCADGui.getDocument("assembly").getObject("part_vis_metal_m10_200l00" + str(i1)).ShapeColor = (0.00,1.00,1.00)
    i1 += 1

# insertion part_vis_metal_m10_150l - 0
degre = 180
k = 6.40
radius = diametre_maximal/2 - 25 - 3 - 5 - 5 - 5
alpha=(degre*math.pi)/180
vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), - 2 - k)
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_vis_metal_m10_150l.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_vis_metal_m10_150l").Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_vis_metal_m10_150l").ShapeColor = (0.00,1.00,1.00)

# For placing the part_vis_metal_m10_150l
i1 = 1
degres = [360]
k = 6.40
for degre in degres:
    radius = diametre_maximal/2 - 25 - 3 - 5 - 5 - 5
    alpha=(degre*math.pi)/180
    vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), - 2 - k)
    Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_vis_metal_m10_150l.stl", "assembly")
    FreeCAD.getDocument("assembly").getObject("part_vis_metal_m10_150l00" + str(i1)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
    FreeCADGui.getDocument("assembly").getObject("part_vis_metal_m10_150l00" + str(i1)).ShapeColor = (0.00,1.00,1.00)
    i1 += 1

# insertion part_ecrou_10m - 0
degre = 60
radius = diametre_maximal/2 - 7.5 - 5
alpha=(degre*math.pi)/180
vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 8)
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_ecrou_10m.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_ecrou_10m").Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_ecrou_10m").ShapeColor = (0.00,0.00,1.00)

# For placing the part_ecrou_10m
i1 = 1
degres = [120, 180, 240, 300, 360]
for degre in degres:
    radius = diametre_maximal/2 - 7.5 - 5
    alpha=(degre*math.pi)/180
    vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 8)
    Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_ecrou_10m.stl", "assembly")
    FreeCAD.getDocument("assembly").getObject("part_ecrou_10m00" + str(i1)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
    FreeCADGui.getDocument("assembly").getObject("part_ecrou_10m00" + str(i1)).ShapeColor = (0.00,0.00,1.00)
    i1 += 1

# insertion part_ecrou_10m
degre = 180
radius = diametre_maximal/2 - 25 - 3 - 5 - 5 - 5
alpha=(degre*math.pi)/180
vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 8)
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_ecrou_10m.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_ecrou_10m006").Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_ecrou_10m006").ShapeColor = (0.00,0.00,1.00)

# For placing the part_ecrou_10m
i1 = 7
degres = [360]
for degre in degres:
    radius = diametre_maximal/2 - 25 - 3 - 5 - 5 - 5
    alpha=(degre*math.pi)/180
    vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 8)
    Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_ecrou_10m.stl", "assembly")
    FreeCAD.getDocument("assembly").getObject("part_ecrou_10m00" + str(i1)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
    FreeCADGui.getDocument("assembly").getObject("part_ecrou_10m00" + str(i1)).ShapeColor = (0.00,0.00,1.00)
    i1 += 1

# For placing the part_rondelle_10m
for i in range(16, 18):
    Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_rondelle_10m.stl", "assembly")

for i in range(16, 18):
    alpha=(i*180*math.pi)/180
    radius = diametre_maximal/2 - 25 - 3 - 5 - 5 - 5
    vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 8 + 10)
    FreeCAD.getDocument("assembly").getObject("part_rondelle_10m0" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
    FreeCADGui.getDocument("assembly").getObject("part_rondelle_10m0" + str(i)).ShapeColor = (1.00,1.00,0.00)

# insertion part_capacitor_plate - 0
vector = App.Vector(0, 0, 20)
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_capacitor_plate.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_capacitor_plate").Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 90))
FreeCADGui.getDocument("assembly").getObject("part_capacitor_plate").ShapeColor = (0.00,0.50,0.50)

# For placing the part_rondelle_10m
for i in range(18, 20):
    Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_rondelle_10m.stl", "assembly")

for i in range(18, 20):
    alpha=(i*180*math.pi)/180
    radius = diametre_maximal/2 - 25 - 3 - 5 - 5 - 5
    vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 21)
    FreeCAD.getDocument("assembly").getObject("part_rondelle_10m0" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
    FreeCADGui.getDocument("assembly").getObject("part_rondelle_10m0" + str(i)).ShapeColor = (1.00,1.00,0.00)

# insertion part_capacitor_plate - 1
vector = App.Vector(0, 0, 23)
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_capacitor_plate.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_capacitor_plate001").Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 270))
FreeCADGui.getDocument("assembly").getObject("part_capacitor_plate001").ShapeColor = (0.00,0.50,0.50)

# For placing all the part_capacitor_plate
for i in range(2, 10):
    if i % 2 == 0:
        vector = App.Vector(0, 0, i*3 + 20)
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_capacitor_plate.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_capacitor_plate00" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 90))
        FreeCADGui.getDocument("assembly").getObject("part_capacitor_plate00" + str(i)).ShapeColor = (0.00,0.50,0.50)
    else:
        vector = App.Vector(0, 0, i*3 + 20)
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_capacitor_plate.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_capacitor_plate00" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 270))
        FreeCADGui.getDocument("assembly").getObject("part_capacitor_plate00" + str(i)).ShapeColor = (0.00,0.50,0.50)

# For placing all the part_capacitor_plate
for i in range(10, 37):
    if i % 2 == 0:
        vector = App.Vector(0, 0, i*3 + 20)
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_capacitor_plate.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_capacitor_plate0" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 90))
        FreeCADGui.getDocument("assembly").getObject("part_capacitor_plate0" + str(i)).ShapeColor = (0.00,0.50,0.50)
    else:
        vector = App.Vector(0, 0, i*3 + 20)
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_capacitor_plate.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_capacitor_plate0" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 270))
        FreeCADGui.getDocument("assembly").getObject("part_capacitor_plate0" + str(i)).ShapeColor = (0.00,0.50,0.50)

# For placing the part_tank_d20_170l
vector = App.Vector(0, 0, 3)
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_tank_d20_170l.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_tank_d20_170l").Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_tank_d20_170l").ShapeColor = (0.20,0.20,0.20)
FreeCADGui.getDocument("assembly").getObject("part_tank_d20_170l").Transparency = 40

# For placing the part_top_support_250d
# vector = App.Vector(0, 0, 176)
# Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_top_support_250d.stl", "assembly")
# FreeCAD.getDocument("assembly").getObject("part_top_support_250d").Placement = App.Placement(vector, App.Rotation(App.Vector(1,0,0), 180))
# FreeCADGui.getDocument("assembly").getObject("part_top_support_250d").ShapeColor = (0.00,1.00,0.00)
# FreeCADGui.getDocument("assembly").getObject("part_top_support_250d").Transparency = 80

# For placing the part_top_support_250d_v1
vector = App.Vector(0, 0, 176)
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_top_support_250d_v1.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_top_support_250d_v1").Placement = App.Placement(vector, App.Rotation(App.Vector(1,0,0), 180))
FreeCADGui.getDocument("assembly").getObject("part_top_support_250d_v1").ShapeColor = (0.00,1.00,0.00)
FreeCADGui.getDocument("assembly").getObject("part_top_support_250d_v1").Transparency = 80

# For placing the part_rondelle_10m
for i in range(20, 56):
    Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_rondelle_10m.stl", "assembly")

for i in range(20, 56):
    alpha=(180*math.pi)/180
    radius = diametre_maximal/2 - 25 - 3 - 5 - 5 - 5
    vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), i*3 - 36)
    FreeCAD.getDocument("assembly").getObject("part_rondelle_10m0" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
    FreeCADGui.getDocument("assembly").getObject("part_rondelle_10m0" + str(i)).ShapeColor = (1.00,1.00,0.00)

# For placing the part_rondelle_10m
for i in range(56, 62):
    Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_rondelle_10m.stl", "assembly")
    alpha=(i*60*math.pi)/180
    radius = diametre_maximal/2 - 7.5 - 5
    vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 176)
    FreeCAD.getDocument("assembly").getObject("part_rondelle_10m0" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
    FreeCADGui.getDocument("assembly").getObject("part_rondelle_10m0" + str(i)).ShapeColor = (1.00,1.00,0.00)

# For placing the part_rondelle_10m
for i in range(62, 68):
    Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_rondelle_10m.stl", "assembly")
    alpha=(i*60*math.pi)/180
    radius = diametre_maximal/2 - 7.5 - 5
    vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 176 - 8)
    FreeCAD.getDocument("assembly").getObject("part_rondelle_10m0" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
    FreeCADGui.getDocument("assembly").getObject("part_rondelle_10m0" + str(i)).ShapeColor = (1.00,1.00,0.00)

# For placing the part_ecrou_10m
i1 = 8
degres = [60, 120, 180, 240, 300, 360]
for degre in degres:
    if i1 < 10:
        radius = diametre_maximal/2 - 7.5 - 5
        alpha=(degre*math.pi)/180
        vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 176 + 2)
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_ecrou_10m.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_ecrou_10m00" + str(i1)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_ecrou_10m00" + str(i1)).ShapeColor = (0.00,0.00,1.00)
    else:
        radius = diametre_maximal/2 - 7.5 - 5
        alpha=(degre*math.pi)/180
        vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 176 + 2)
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_ecrou_10m.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_ecrou_10m0" + str(i1)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_ecrou_10m0" + str(i1)).ShapeColor = (0.00,0.00,1.00)
    
    i1 += 1

# For placing the part_ecrou_10m
i1 = 14
degres = [180, 360]
for degre in degres:
    radius = diametre_maximal/2 - 25 - 3 - 5 - 5 - 5
    alpha=(degre*math.pi)/180
    vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 56*3 - 36)
    Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_ecrou_10m.stl", "assembly")
    FreeCAD.getDocument("assembly").getObject("part_ecrou_10m0" + str(i1)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
    FreeCADGui.getDocument("assembly").getObject("part_ecrou_10m0" + str(i1)).ShapeColor = (0.00,0.00,1.00)
    i1 += 1

# For placing the part_rondelle_10m0
for i in range(68, 104):
    if i < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_rondelle_10m.stl", "assembly")
        alpha=(360*math.pi)/180
        radius = diametre_maximal/2 - 25 - 3 - 5 - 5 - 5
        vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), i*3 - 180)
        FreeCAD.getDocument("assembly").getObject("part_rondelle_10m0" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_rondelle_10m0" + str(i)).ShapeColor = (1.00,1.00,0.00)
    else:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_rondelle_10m.stl", "assembly")
        alpha=(360*math.pi)/180
        radius = diametre_maximal/2 - 25 - 3 - 5 - 5 - 5
        vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), i*3 - 180)
        FreeCAD.getDocument("assembly").getObject("part_rondelle_10m" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_rondelle_10m" + str(i)).ShapeColor = (1.00,1.00,0.00)

# For placing the part_ecrou_10m
i1 = 16
degres = [60, 120, 180, 240, 300, 360]
for degre in degres:
    radius = diametre_maximal/2 - 7.5 - 5
    alpha=(degre*math.pi)/180
    vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 176 - 6 - 2 - 10)
    Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_ecrou_10m.stl", "assembly")
    FreeCAD.getDocument("assembly").getObject("part_ecrou_10m0" + str(i1)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
    FreeCADGui.getDocument("assembly").getObject("part_ecrou_10m0" + str(i1)).ShapeColor = (0.00,0.00,1.00)
    i1 += 1

# insertion part_vis_metal_m10_30l - 0
degre = 90
k = 6.40
radius = diametre_maximal/2 - 7.5 - 5
alpha=(degre*math.pi)/180
vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), - 6 - k)
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_vis_metal_m10_30l.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_vis_metal_m10_30l").Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_vis_metal_m10_30l").ShapeColor = (0.00,1.00,1.00)

# insertion part_vis_metal_m10_30l
degres = [210, 330]
i1 = 1
for degre in degres:
    k = 6.40
    radius = diametre_maximal/2 - 7.5 - 5
    alpha=(degre*math.pi)/180
    vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), - 6 - k)
    Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_vis_metal_m10_30l.stl", "assembly")
    FreeCAD.getDocument("assembly").getObject("part_vis_metal_m10_30l00" + str(i1)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
    FreeCADGui.getDocument("assembly").getObject("part_vis_metal_m10_30l00" + str(i1)).ShapeColor = (0.00,1.00,1.00)
    i1 += 1
    
# For placing the part_rondelle_10m
degres = [90, 210, 330]
i = 104
for degre in degres:
    k = 6.40
    Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_rondelle_10m.stl", "assembly")
    alpha=(degre*math.pi)/180
    radius = diametre_maximal/2 - 7.5 - 5
    vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), - 2)
    FreeCAD.getDocument("assembly").getObject("part_rondelle_10m" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
    FreeCADGui.getDocument("assembly").getObject("part_rondelle_10m" + str(i)).ShapeColor = (1.00,1.00,0.00)
    i += 1

# For placing the part_rondelle_10m
degres = [90, 210, 330]
i = 107
for degre in degres:
    k = 6.40
    Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_rondelle_10m.stl", "assembly")
    alpha=(degre*math.pi)/180
    radius = diametre_maximal/2 - 7.5 - 5
    vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), - 6)
    FreeCAD.getDocument("assembly").getObject("part_rondelle_10m" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
    FreeCADGui.getDocument("assembly").getObject("part_rondelle_10m" + str(i)).ShapeColor = (1.00,1.00,0.00)
    i += 1

# For placing the part_rondelle_10m
degres = [90, 210, 330]
i = 110
for degre in degres:
    k = 6.40
    Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_rondelle_10m.stl", "assembly")
    alpha=(degre*math.pi)/180
    radius = diametre_maximal/2 - 7.5 - 5
    vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 6)
    FreeCAD.getDocument("assembly").getObject("part_rondelle_10m" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
    FreeCADGui.getDocument("assembly").getObject("part_rondelle_10m" + str(i)).ShapeColor = (1.00,1.00,0.00)
    i += 1

# For placing the part_ecrou_10m
i1 = 22
degres = [90, 210, 330]
for degre in degres:
    radius = diametre_maximal/2 - 7.5 - 5
    alpha=(degre*math.pi)/180
    vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 8)
    Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_ecrou_10m.stl", "assembly")
    FreeCAD.getDocument("assembly").getObject("part_ecrou_10m0" + str(i1)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
    FreeCADGui.getDocument("assembly").getObject("part_ecrou_10m0" + str(i1)).ShapeColor = (0.00,0.00,1.00)
    i1 += 1

# For placing capteur de volume
# Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/part_capteur_de_volume.stl", "assembly")
# vector = App.Vector(0, 0, 73)
# FreeCAD.getDocument("assembly").getObject("part_capteur_de_volume").Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
# FreeCADGui.getDocument("assembly").getObject("part_capteur_de_volume").ShapeColor = (0.00,0.00,1.00)

setview()

__objs__=[]
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m007"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m005"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m011"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m012"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m010"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_capacitor_plate022"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_10m"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_capacitor_plate"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m019"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_10m002"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_10m003"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_capacitor_plate001"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_capacitor_plate020"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_vis_metal_m10_150l"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_vis_metal_m10_150l001"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_capacitor_plate021"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_10m004"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m013"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m009"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m001"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_vis_metal_m10_200l"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_vis_metal_m10_200l001"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m002"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m003"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m004"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m008"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m029"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m030"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m043"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m021"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m053"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m055"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m075"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m061"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m020"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m042"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m044"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m056"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_top_support_250d"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("Shape"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m037"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_capacitor_plate033"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_capacitor_plate036"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_capacitor_plate034"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_tank_d20_170l"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_capacitor_plate035"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m022"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m023"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m033"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m035"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m024"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m034"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m036"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_capacitor_plate015"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_capacitor_plate018"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_capacitor_plate027"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_capacitor_plate028"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_capacitor_plate017"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_capacitor_plate019"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_capacitor_plate025"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_capacitor_plate026"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_capacitor_plate029"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_capacitor_plate030"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_capacitor_plate016"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_capacitor_plate031"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_capacitor_plate032"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m108"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m109"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m107"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_10m018"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_10m022"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_vis_metal_m10_30l"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_10m023"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_10m021"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_10m024"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_10m020"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m064"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m038"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m051"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m048"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m040"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m050"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_10m001"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m065"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m067"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_10m008"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m066"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_10m012"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_10m013"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_10m014"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m071"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_10m009"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_10m010"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m070"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m072"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_10m011"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_capacitor_plate007"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_capacitor_plate005"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_capacitor_plate006"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_capacitor_plate009"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_capacitor_plate010"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_capacitor_plate004"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_capacitor_plate011"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_capacitor_plate012"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_capacitor_plate013"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_capacitor_plate002"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_capacitor_plate003"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_capacitor_plate014"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_capacitor_plate008"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m092"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m091"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m093"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_vis_metal_m10_30l001"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m082"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m052"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m039"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m057"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m080"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m032"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m074"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m081"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m031"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m054"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m068"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m069"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m073"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m018"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m089"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m090"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m102"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m103"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_10m016"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_10m017"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_10m019"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m086"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m085"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m087"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m083"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m088"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m084"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_vis_metal_m10_200l004"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_vis_metal_m10_200l005"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_vis_metal_m10_200l002"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_vis_metal_m10_200l003"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m017"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m058"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m014"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m015"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_10m007"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_capacitor_plate023"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m025"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m110"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m106"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m101"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m062"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m077"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m060"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m076"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_10m006"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m027"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m079"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m098"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m099"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m097"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m104"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m078"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_capacitor_plate024"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m094"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m045"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m049"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_10m005"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_vis_metal_m10_30l002"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m111"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_10m015"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m096"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m100"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m047"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m063"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m112"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m028"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m016"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m026"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m041"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m006"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m046"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m059"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m095"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_10m105"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/assembly_water_electrolyzer.stl"

Mesh.export(__objs__, stl_file)

del __objs__

# Generate PNG files
file = 'assembly_'
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
        