import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_generator"


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

assembly = "assembly_generator"

# tube diameter
d_tube = 140 + 10*2 + 5*2

# nut diameter
d_nut = 24

r_f_d = (d_tube + 5*2 + 2*2 + d_nut)/2

# assembly_shaft
assembly_shaft_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/assembly_shaft.stl"
Mesh.insert(assembly_shaft_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("assembly_shaft").ShapeColor = (0.10,0.10,0.10)
FreeCAD.getDocument(assembly).getObject("assembly_shaft").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))

# part_tube
color = (0.20,0.50,0.70)
x = 0
y = 0
z = 150
part_tube_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_tube.stl"
Mesh.insert(part_tube_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_tube").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_tube").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

# assembly_support
color = (0.20,0.00,0.70)
x = 0
y = 0
z = 150 + (700 - 170)/2 - 5
assembly_support_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/assembly_support.stl"
Mesh.insert(assembly_support_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("assembly_support").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("assembly_support").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,1,0),180))

# assembly_support
color = (0.20,0.00,0.70)
x = 0
y = 0
z = 700 - 110
assembly_support_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/assembly_support.stl"
Mesh.insert(assembly_support_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("assembly_support001").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("assembly_support001").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,1,0),0))

# part_rondelle_12m
i1 = 0
degre = 30
color = (0.30,0.90,0.30)
title = 'part_rondelle_12m'
stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/" + title + ".stl"
for i in range(int(360/degre)):
    radius = r_f_d
    alpha = (i*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = 150 + (700 - 170)/2 - 5 - 5 - 2.5

    if i1 == 0:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i1 >= 1 and i1 < 10:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "00" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "00" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i1 >= 10 and i1 < 100:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "0" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "0" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i1 >= 100 and i1 < 1000:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + str(i1)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    
    i1 += 1

degre = 30
color = (0.30,0.90,0.30)
title = 'part_rondelle_12m'
stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/" + title + ".stl"
for i in range(int(360/degre)):
    radius = r_f_d
    alpha = (i*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = 150 + (700 - 170)/2 + 180

    if i1 == 0:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i1 >= 1 and i1 < 10:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "00" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "00" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i1 >= 10 and i1 < 100:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "0" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "0" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i1 >= 100 and i1 < 1000:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + str(i1)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    
    i1 += 1

# part_ecrou_12m
i2 = 0
degre = 30
color = (0.10,0.50,0.10)
title = 'part_ecrou_12m'
stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/" + title + ".stl"
for i in range(int(360/degre)):
    radius = r_f_d
    alpha = (i*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = 150 + (700 - 170)/2 + 180 + 2.5

    if i2 == 0:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i2 >= 1 and i2 < 10:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "00" + str(i2)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "00" + str(i2)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i2 >= 10 and i2 < 100:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "0" + str(i2)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "0" + str(i2)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i2 >= 100 and i2 < 1000:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + str(i2)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + str(i2)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    
    i2 += 1

# part_vis_metal_m12_200l
i3 = 0
degre = 30
color = (0.00,0.90,0.90)
title = 'part_vis_metal_m12_200l'
stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/" + title + ".stl"
for i in range(int(360/degre)):
    radius = r_f_d
    alpha = (i*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = 150 + (700 - 170)/2 - 5 - 5 - 2.5 - 7.5

    if i3 == 0:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i3 >= 1 and i3 < 10:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "00" + str(i3)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "00" + str(i3)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i3 >= 10 and i3 < 100:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "0" + str(i3)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "0" + str(i3)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i3 >= 100 and i3 < 1000:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + str(i2)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + str(i2)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    
    i3 += 1

# part_rondelle_20m
color = (0.40,0.30,0.70)
x = 0
y = 0
z = 150 - 5 - 33.3 - 3
part_rondelle_20m_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_rondelle_20m.stl"
Mesh.insert(part_rondelle_20m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_rondelle_20m").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_rondelle_20m").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,1,0),0))

# part_rondelle_20m
color = (0.40,0.30,0.70)
x = 0
y = 0
z = 150 + 700 + 5 + 33.3
part_rondelle_20m_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_rondelle_20m.stl"
Mesh.insert(part_rondelle_20m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_rondelle_20m001").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_rondelle_20m001").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,1,0),0))

# part_ecrou_20m
color = (0.50,0.00,0.40)
x = 0
y = 0
z = 150 - 5 - 33.3 - 3 - 3 - 16 - 1
part_ecrou_20m_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_ecrou_20m.stl"
Mesh.insert(part_ecrou_20m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_ecrou_20m").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_ecrou_20m").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,1,0),0))

# part_ecrou_20m
color = (0.50,0.00,0.40)
x = 0
y = 0
z = 150 + 700 + 5 + 33.3 + 3
part_ecrou_20m_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_ecrou_20m.stl"
Mesh.insert(part_ecrou_20m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_ecrou_20m001").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_ecrou_20m001").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,1,0),0))

# part_rondelle_20m
color = (0.40,0.30,0.70)
x = 0
y = 0
z = 150 - 5 - 33.3 - 3 - 3 - 16 - 3
part_rondelle_20m_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_rondelle_20m.stl"
Mesh.insert(part_rondelle_20m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_rondelle_20m002").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_rondelle_20m002").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,1,0),0))

# part_rondelle_20m
color = (0.40,0.30,0.70)
x = 0
y = 0
z = 150 + 700 + 5 + 33.3 + 3 + 16 + 4
part_rondelle_20m_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_rondelle_20m.stl"
Mesh.insert(part_rondelle_20m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_rondelle_20m003").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_rondelle_20m003").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,1,0),0))

# part_palier
color = (0.20,0.60,0.20)
x = - 127/2
y = 65/2
z = 150 - 5 - 33.3 - 3 - 3 - 16 - 3 - 1 - 38 + 1
part_palier_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_palier.stl"
Mesh.insert(part_palier_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_palier").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_palier").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))

# part_palier
color = (0.20,0.60,0.20)
x = - 127/2
y = 65/2
z = 150 + 700 + 5 + 33.3 + 3 + 3 + 38 - 18
part_palier_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_palier.stl"
Mesh.insert(part_palier_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_palier001").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_palier001").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))

# part_rondelle_20m
color = (0.40,0.30,0.70)
x = 0
y = 0
z = 150 - 5 - 33.3 - 3 - 16 - 3 - 1 - 38 - 16 + 11
part_rondelle_20m_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_rondelle_20m.stl"
Mesh.insert(part_rondelle_20m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_rondelle_20m004").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_rondelle_20m004").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,1,0),0))

# part_rondelle_20m
color = (0.40,0.30,0.70)
x = 0
y = 0
z = 150 + 700 + 5 + 33.3 + 3 + 38 - 18 + 38 + 3
part_rondelle_20m_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_rondelle_20m.stl"
Mesh.insert(part_rondelle_20m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_rondelle_20m005").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_rondelle_20m005").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,1,0),0))

# part_ecrou_20m
color = (0.50,0.00,0.40)
x = 0
y = 0
z = 150 - 5 - 33.3 - 3 - 16 - 3 - 1 - 38 - 16 + 11 - 3 - 16 - 1
part_ecrou_20m_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_ecrou_20m.stl"
Mesh.insert(part_ecrou_20m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_ecrou_20m002").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_ecrou_20m002").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,1,0),0))

# part_ecrou_20m
color = (0.50,0.00,0.40)
x = 0
y = 0
z = 150 + 700 + 5 + 33.3 + 3 + 38 - 18 + 38 + 3 + 3
part_ecrou_20m_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_ecrou_20m.stl"
Mesh.insert(part_ecrou_20m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_ecrou_20m003").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_ecrou_20m003").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,1,0),0))

# part_moyeu_amovible_generator
'''
color = (0.60,0.60,0.60)
x = 0
y = 0
z = 150 - 5 - 33.3 - 3 - 16 - 3 - 1 - 38 - 16 + 11 - 3 - 16 - 1 - 21.5
part_moyeu_amovible_generator_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_moyeu_amovible_generator.stl"
Mesh.insert(part_moyeu_amovible_generator_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_moyeu_amovible_generator").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_moyeu_amovible_generator").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
'''

# part_poulie_generator
'''
color = (0.60,0.10,0.10)
x = 0
y = 0
z = 150 - 5 - 33.3 - 3 - 16 - 3 - 1 - 38 - 16 + 11 - 3 - 16 - 1 - 21.5
part_poulie_generator_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_poulie_generator.stl"
Mesh.insert(part_poulie_generator_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_poulie_generator").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_poulie_generator").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
'''

setview()

# Export
__objs__ = []

__objs__.append(FreeCAD.getDocument(assembly).getObject("assembly_shaft"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_tube"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("assembly_support"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("assembly_support001"))

title = "part_rondelle_12m"
for i in range(0, int(360/30)):
    if i == 0:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + str(i)))

title = "part_rondelle_12m"
for i in range(int(360/30), int(360/30) * 2):
    if i == 0:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + str(i)))

title = "part_ecrou_12m"
for i in range(0, int(360/30)):
    if i == 0:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + str(i)))

title = "part_vis_metal_m12_200l"
for i in range(0, int(360/30)):
    if i == 0:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + str(i)))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_rondelle_20m"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_rondelle_20m001"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_ecrou_20m"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_ecrou_20m001"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_palier"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_palier001"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_rondelle_20m002"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_rondelle_20m003"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_rondelle_20m004"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_rondelle_20m005"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_ecrou_20m002"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_ecrou_20m003"))

# __objs__.append(FreeCAD.getDocument(assembly).getObject("part_moyeu_amovible_generator"))

# __objs__.append(FreeCAD.getDocument(assembly).getObject("part_poulie_generator"))

Mesh.export(__objs__,u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/" + assembly + ".stl")

del __objs__

# Generate PNG files
file = 'C:\\Users\\Jason\\Documents\\Devs\\Python-Macros-For-FreeCAD\\HG\\Version_1\\Png\\assembly_generator_'
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
