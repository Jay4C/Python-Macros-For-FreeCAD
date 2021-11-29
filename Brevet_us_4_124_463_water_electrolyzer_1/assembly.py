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

cylinder_1 = Part.makeCylinder(32, 2)

cylinder_2 = Part.makeCylinder(2.5, 2)

cylinder_1 = cylinder_1.cut(cylinder_2)

# holes for fixing the disc anode and the disc cathode
degre = 60
for i in range(int(360/degre)):
    radius = 32 - 3.5 - 2.5
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 2)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# holes for letting the gas mixture to go out
for i in range(int(360/degre)):
    radius = 14.25
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(6, 2)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

degres = [30, 90, 150, -30, -90, -150]

for degre in degres:
    radius = 24
    alpha=(int(degre)*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(6, 2)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

Part.show(cylinder_1)

DOC.recompute()

# insertion part_rondelle_m5_12d - 0
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_1/part_rondelle_m5_12d.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_rondelle_m5_12d").Placement = App.Placement(App.Vector(0, 0, -1), App.Rotation(App.Vector(0,1,0), 0))
FreeCADGui.getDocument("assembly").getObject("part_rondelle_m5_12d").ShapeColor = (0.67,0.33,0.50)

# insertion part_rondelle_m5_12d - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_1/part_rondelle_m5_12d.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_rondelle_m5_12d001").Placement = App.Placement(App.Vector(0, 0, 2), App.Rotation(App.Vector(0,1,0), 0))
FreeCADGui.getDocument("assembly").getObject("part_rondelle_m5_12d001").ShapeColor = (0.67,0.33,0.50)

# For placing all the part_rondelle_m5_12d for fixing the anodes and the cathodes
i1 = 2
degre = 60
for i in range(int(360/degre)):
    radius = 32 - 3.5 - 2.5
    alpha=(i*degre*math.pi)/180
    part_rondelle_m5_d12_vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), -1)
    Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_1/part_rondelle_m5_12d.stl", "assembly")
    FreeCAD.getDocument("assembly").getObject("part_rondelle_m5_12d00" + str(i1)).Placement = App.Placement(part_rondelle_m5_d12_vector, App.Rotation(App.Vector(0,1,0), 0))
    FreeCADGui.getDocument("assembly").getObject("part_rondelle_m5_12d00" + str(i1)).ShapeColor = (0.67,0.33,0.50)
    i1 += 1

# For placing all the part_rondelle_m5_12d for fixing the anodes and the cathodes
i1 = 8
degre = 60
for i in range(int(360/degre)):
    if i1 < 10:
        radius = 32 - 3.5 - 2.5
        alpha=(i*degre*math.pi)/180
        part_rondelle_m5_d12_vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 2)
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_1/part_rondelle_m5_12d.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_rondelle_m5_12d00" + str(i1)).Placement = App.Placement(part_rondelle_m5_d12_vector, App.Rotation(App.Vector(0,1,0), 0))
        FreeCADGui.getDocument("assembly").getObject("part_rondelle_m5_12d00" + str(i1)).ShapeColor = (0.67,0.33,0.50)
    else:
        radius = 32 - 3.5 - 2.5
        alpha=(i*degre*math.pi)/180
        part_rondelle_m5_d12_vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 2)
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_1/part_rondelle_m5_12d.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_rondelle_m5_12d0" + str(i1)).Placement = App.Placement(part_rondelle_m5_d12_vector, App.Rotation(App.Vector(0,1,0), 0))
        FreeCADGui.getDocument("assembly").getObject("part_rondelle_m5_12d0" + str(i1)).ShapeColor = (0.67,0.33,0.50)
    
    i1 += 1

# insertion part_vis_metal_m5_100l - 0
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_1/part_vis_metal_m5_100l.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_vis_metal_m5_100l").Placement = App.Placement(App.Vector(0, 0, 5), App.Rotation(App.Vector(1,0,0), 180))
FreeCADGui.getDocument("assembly").getObject("part_vis_metal_m5_100l").ShapeColor = (0.00,0.00,1.00)

# For placing all the part_vis_metal_m5_100l for fixing the anodes and the cathodes
i1 = 1
degre = 60
for i in range(int(360/degre)):
    radius = 32 - 3.5 - 2.5
    alpha=(i*degre*math.pi)/180
    vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), -3)
    Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_1/part_vis_metal_m5_100l.stl", "assembly")
    FreeCAD.getDocument("assembly").getObject("part_vis_metal_m5_100l00" + str(i1)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,1,0), 0))
    FreeCADGui.getDocument("assembly").getObject("part_vis_metal_m5_100l00" + str(i1)).ShapeColor = (0.00,0.00,1.00)
    i1 += 1

# insertion part_ecrou_5m - 0
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_1/part_ecrou_5m.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_ecrou_5m").Placement = App.Placement(App.Vector(0, 0, -5), App.Rotation(App.Vector(0,1,0), 0))
FreeCADGui.getDocument("assembly").getObject("part_ecrou_5m").ShapeColor = (1.00,1.00,1.00)

# For placing all the part_ecrou_5m for fixing the anodes and the cathodes
i1 = 1
degre = 60
for i in range(int(360/degre)):
    radius = 32 - 3.5 - 2.5
    alpha=(i*degre*math.pi)/180
    vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 3)
    Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_1/part_ecrou_5m.stl", "assembly")
    FreeCAD.getDocument("assembly").getObject("part_ecrou_5m00" + str(i1)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,1,0), 0))
    FreeCADGui.getDocument("assembly").getObject("part_ecrou_5m00" + str(i1)).ShapeColor = (1.00,1.00,1.00)
    i1 += 1

# For placing all the part_rondelle_m5_12d for fixing the anodes and the cathodes
i1 = 14
degre = 60
for i in range(int(360/degre)):
    radius = 32 - 3.5 - 2.5
    alpha=(i*degre*math.pi)/180
    part_rondelle_m5_d12_vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 7)
    Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_1/part_rondelle_m5_12d.stl", "assembly")
    FreeCAD.getDocument("assembly").getObject("part_rondelle_m5_12d0" + str(i1)).Placement = App.Placement(part_rondelle_m5_d12_vector, App.Rotation(App.Vector(0,1,0), 0))
    FreeCADGui.getDocument("assembly").getObject("part_rondelle_m5_12d0" + str(i1)).ShapeColor = (0.67,0.33,0.50)
    i1 += 1

# insertion part_capacitor_plate - 0
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_1/part_capacitor_plate.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_capacitor_plate").Placement = App.Placement(App.Vector(0, 0, 8), App.Rotation(App.Vector(0,1,0), 0))
FreeCADGui.getDocument("assembly").getObject("part_capacitor_plate").ShapeColor = (1.00,1.00,0.00)

# For placing all the part_rondelle_m5_12d for fixing the anodes and the cathodes
i1 = 20
degre = 60
for i in range(int(360/degre)):
    radius = 32 - 3.5 - 2.5
    alpha=(i*degre*math.pi)/180
    part_rondelle_m5_d12_vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 9)
    Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_1/part_rondelle_m5_12d.stl", "assembly")
    FreeCAD.getDocument("assembly").getObject("part_rondelle_m5_12d0" + str(i1)).Placement = App.Placement(part_rondelle_m5_d12_vector, App.Rotation(App.Vector(0,1,0), 0))
    FreeCADGui.getDocument("assembly").getObject("part_rondelle_m5_12d0" + str(i1)).ShapeColor = (0.67,0.33,0.50)
    i1 += 1

# insertion part_capacitor_plate - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_1/part_capacitor_plate.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_capacitor_plate001").Placement = App.Placement(App.Vector(0, 0, 10), App.Rotation(App.Vector(0,0,1), 60))
FreeCADGui.getDocument("assembly").getObject("part_capacitor_plate001").ShapeColor = (1.00,0.67,0.00)

# For placing all the part_rondelle_m5_12d for fixing the anodes and the cathodes
i1 = 26
degre = 60
for i in range(int(360/degre)):
    radius = 32 - 3.5 - 2.5
    alpha=(i*degre*math.pi)/180
    part_rondelle_m5_d12_vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 11)
    Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_1/part_rondelle_m5_12d.stl", "assembly")
    FreeCAD.getDocument("assembly").getObject("part_rondelle_m5_12d0" + str(i1)).Placement = App.Placement(part_rondelle_m5_d12_vector, App.Rotation(App.Vector(0,1,0), 0))
    FreeCADGui.getDocument("assembly").getObject("part_rondelle_m5_12d0" + str(i1)).ShapeColor = (0.67,0.33,0.50)
    i1 += 1

# insertion part_capacitor_plate - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_1/part_capacitor_plate.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_capacitor_plate002").Placement = App.Placement(App.Vector(0, 0, 12), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_capacitor_plate002").ShapeColor = (1.00,1.00,0.00)

# For placing all the part_rondelle_m5_12d for fixing the anodes and the cathodes
i1 = 32
degre = 60
for i in range(int(360/degre)):
    radius = 32 - 3.5 - 2.5
    alpha=(i*degre*math.pi)/180
    part_rondelle_m5_d12_vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 13)
    Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_1/part_rondelle_m5_12d.stl", "assembly")
    FreeCAD.getDocument("assembly").getObject("part_rondelle_m5_12d0" + str(i1)).Placement = App.Placement(part_rondelle_m5_d12_vector, App.Rotation(App.Vector(0,1,0), 0))
    FreeCADGui.getDocument("assembly").getObject("part_rondelle_m5_12d0" + str(i1)).ShapeColor = (0.67,0.33,0.50)
    i1 += 1

# insertion part_capacitor_plate - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_1/part_capacitor_plate.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_capacitor_plate003").Placement = App.Placement(App.Vector(0, 0, 14), App.Rotation(App.Vector(0,0,1), 60))
FreeCADGui.getDocument("assembly").getObject("part_capacitor_plate003").ShapeColor = (1.00,0.67,0.00)

# For placing all the part_rondelle_m5_12d for fixing the anodes and the cathodes
i1 = 38
degre = 60
for i in range(int(360/degre)):
    radius = 32 - 3.5 - 2.5
    alpha=(i*degre*math.pi)/180
    part_rondelle_m5_d12_vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 15)
    Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_1/part_rondelle_m5_12d.stl", "assembly")
    FreeCAD.getDocument("assembly").getObject("part_rondelle_m5_12d0" + str(i1)).Placement = App.Placement(part_rondelle_m5_d12_vector, App.Rotation(App.Vector(0,1,0), 0))
    FreeCADGui.getDocument("assembly").getObject("part_rondelle_m5_12d0" + str(i1)).ShapeColor = (0.67,0.33,0.50)
    i1 += 1

# For placing all the part_capacitor_plate
for i in range(4, 10):
    if i % 2 == 0:
        vector = App.Vector(0, 0, i*2 + 8)
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_1/part_capacitor_plate.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_capacitor_plate00" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_capacitor_plate00" + str(i)).ShapeColor = (1.00,1.00,0.00)
    else:
        vector = App.Vector(0, 0, i*2 + 8)
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_1/part_capacitor_plate.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_capacitor_plate00" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 60))
        FreeCADGui.getDocument("assembly").getObject("part_capacitor_plate00" + str(i)).ShapeColor = (1.00,0.67,0.00)

# For placing all the part_capacitor_plate
for i in range(10, 40):
    if i % 2 == 0:
        vector = App.Vector(0, 0, i*2 + 8)
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_1/part_capacitor_plate.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_capacitor_plate0" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_capacitor_plate0" + str(i)).ShapeColor = (1.00,1.00,0.00)
    else:
        vector = App.Vector(0, 0, i*2 + 8)
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_1/part_capacitor_plate.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_capacitor_plate0" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 60))
        FreeCADGui.getDocument("assembly").getObject("part_capacitor_plate0" + str(i)).ShapeColor = (1.00,0.67,0.00)

setview()
        