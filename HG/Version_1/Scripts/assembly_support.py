import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_support"


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

assembly = "assembly_support"

# part_palier_4_fixations dimensions
r_f_p = math.sqrt(math.pow(32, 2) + math.pow(32, 2))

# part_support
part_support_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_support.stl"
Mesh.insert(part_support_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_support").ShapeColor = (0.10,0.10,0.10)
FreeCAD.getDocument(assembly).getObject("part_support").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))

# part_palier_4_fixations
x = -86/2
y = -86/2
z = (700 - 170)/2
part_palier_4_fixations_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_palier_4_fixations.stl"
Mesh.insert(part_palier_4_fixations_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_palier_4_fixations").ShapeColor = (0.30,0.50,0.70)
FreeCAD.getDocument(assembly).getObject("part_palier_4_fixations").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_8m
color = (0.90, 0.80, 0.70)
i = 0
title = 'part_rondelle_8m'
stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/" + title + ".stl"
for degre in [45, 45*3, 45*5, 45*7]:
    radius = r_f_p
    alpha = (degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = (700 - 170)/2 - 5 - 1.5

    if i == 0:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 1 and i < 10:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "00" + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 10 and i < 100:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "0" + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 100 and i < 1000:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    
    i += 1
    
color = (0.90, 0.80, 0.70)
title = 'part_rondelle_8m'
stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/" + title + ".stl"
for degre in [45, 45*3, 45*5, 45*7]:
    radius = r_f_p
    alpha = (degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = (700 - 170)/2 + 33.3

    if i == 0:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 1 and i < 10:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "00" + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 10 and i < 100:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "0" + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 100 and i < 1000:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    
    i += 1

# part_ecrou_8m
color = (0.80, 0.90, 0.10)
i1 = 0
title = 'part_ecrou_8m'
stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/" + title + ".stl"
for degre in [45, 45*3, 45*5, 45*7]:
    radius = r_f_p
    alpha = (degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = (700 - 170)/2 + 33.3 + 1.5

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

# part_vis_metal_m8_50l
color = (0.80, 0.00, 0.50)
i2 = 0
title = 'part_vis_metal_m8_50l'
stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/" + title + ".stl"
for degre in [45, 45*3, 45*5, 45*7]:
    radius = r_f_p
    alpha = (degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = (700 - 170)/2 - 5 - 1.5 - 5.3

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
    
# part_mamelon_a_visser_12_17_m
d_mamelon = 16
degre = 90
radius = (86 + 25 + d_mamelon)/2
alpha = (degre*math.pi)/180
x = radius*math.cos(alpha)
y = radius*math.sin(alpha)
z = (700 - 170)/2 - 5 - 11
color = (0.30, 0.50, 0.70)
part_mamelon_a_visser_12_17_m_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_mamelon_a_visser_12_17_m.stl"
Mesh.insert(part_mamelon_a_visser_12_17_m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_mamelon_a_visser_12_17_m").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_mamelon_a_visser_12_17_m").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

# part_manchon_a_visser_12_17_f
degre = 90
d_mamelon = 16
radius = (86 + 25 + d_mamelon)/2
alpha = (degre*math.pi)/180
x = radius*math.cos(alpha)
y = radius*math.sin(alpha)
z = (700 - 170)/2
color = (0.30, 0.60, 0.90)
part_manchon_a_visser_12_17_f_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_manchon_a_visser_12_17_f.stl"
Mesh.insert(part_manchon_a_visser_12_17_f_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_manchon_a_visser_12_17_f").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_manchon_a_visser_12_17_f").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

setview()

# Export
__objs__ = []

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_support"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_palier_4_fixations"))

title = "part_rondelle_8m"
for i in range(0, 8):
    if i == 0:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + str(i)))

title = "part_ecrou_8m"
for i in range(0, 4):
    if i == 0:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + str(i)))

title = "part_vis_metal_m8_50l"
for i in range(0, 4):
    if i == 0:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + str(i)))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_mamelon_a_visser_12_17_m"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_manchon_a_visser_12_17_f"))

Mesh.export(__objs__,u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/" + assembly + ".stl")

del __objs__
