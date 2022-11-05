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

# Parameters
h_rondelle_30m = 4
h_ecrou_30m = 30
e_support = 5
h_rondelle_16m = 3
h_ecrou_16m = 13
h_palier_2_fixation_support = 40.2
h_palier_2_fixation_ossature = 48
h_poulie_generator = 25.4
L_tube = 1000 - (e_support + h_palier_2_fixation_support + h_rondelle_30m + h_ecrou_30m + h_rondelle_30m + h_palier_2_fixation_ossature + h_rondelle_30m + h_ecrou_30m + h_rondelle_30m + h_poulie_generator + h_rondelle_30m + h_ecrou_30m) - (e_support + h_palier_2_fixation_support + h_rondelle_30m + h_ecrou_30m + h_rondelle_30m + h_palier_2_fixation_ossature + h_rondelle_30m + h_ecrou_30m)
h1 = (L_tube - 400)/2

# assembly_shaft
color = (0.10, 0.20, 0.30)
assembly_shaft_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_2/Stl/assembly_shaft.stl"
Mesh.insert(assembly_shaft_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("assembly_shaft").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("assembly_shaft").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))

# assembly_support
x = 0
y = 0
z = (1000 - L_tube)/2 + h1 - 5
color = (0.20, 0.40, 0.60)
assembly_support_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_2/Stl/assembly_support.stl"
Mesh.insert(assembly_support_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("assembly_support").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("assembly_support").Placement = App.Placement(App.Vector(0,0,z),App.Rotation(App.Vector(0,1,0),180))

# assembly_support
x = 0
y = 0
z = (1000 - L_tube)/2 + L_tube - h1 + 5 + 2
color = (0.20, 0.40, 0.60)
assembly_support_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_2/Stl/assembly_support.stl"
Mesh.insert(assembly_support_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("assembly_support001").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("assembly_support001").Placement = App.Placement(App.Vector(0,0,z),App.Rotation(App.Vector(0,0,1),0))

# part_tige_filetee_m16_1000l_cut
x = 117/2
y = 0
z = h1 + h_palier_2_fixation_support - 6
color = (0.30, 0.90, 0.60)
part_tige_filetee_m16_1000l_cut_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_2/Stl/part_tige_filetee_m16_1000l_cut.stl"
Mesh.insert(part_tige_filetee_m16_1000l_cut_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_tige_filetee_m16_1000l_cut").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_tige_filetee_m16_1000l_cut").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

# part_tige_filetee_m16_1000l_cut
x = -117/2
y = 0
z = h1 + h_palier_2_fixation_support - 6
color = (0.30, 0.90, 0.60)
part_tige_filetee_m16_1000l_cut_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_2/Stl/part_tige_filetee_m16_1000l_cut.stl"
Mesh.insert(part_tige_filetee_m16_1000l_cut_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_tige_filetee_m16_1000l_cut001").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_tige_filetee_m16_1000l_cut001").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_30m
x = 0
y = 0
z = (1000 - L_tube)/2 - 5 - h_palier_2_fixation_support - h_rondelle_30m - h_ecrou_30m - h_rondelle_30m
color = (0.90, 0.50, 0.40)
part_rondelle_30m_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_2/Stl/part_rondelle_30m.stl"
Mesh.insert(part_rondelle_30m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_rondelle_30m").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_rondelle_30m").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))

# part_palier_2_fixation_ossature
x = -165/2
y = 84/2
z = (1000 - L_tube)/2 - 5 - h_palier_2_fixation_support - h_rondelle_30m - h_ecrou_30m - h_rondelle_30m - h_palier_2_fixation_ossature
color = (0.50, 0.90, 0.40)
part_palier_2_fixation_ossature_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_2/Stl/part_palier_2_fixation_ossature.stl"
Mesh.insert(part_palier_2_fixation_ossature_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_palier_2_fixation_ossature").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_palier_2_fixation_ossature").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))

# part_rondelle_30m
x = 0
y = 0
z = (1000 - L_tube)/2 - 5 - h_palier_2_fixation_support - h_rondelle_30m - h_ecrou_30m - h_rondelle_30m - h_palier_2_fixation_ossature - h_rondelle_30m
color = (0.90, 0.50, 0.40)
part_rondelle_30m_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_2/Stl/part_rondelle_30m.stl"
Mesh.insert(part_rondelle_30m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_rondelle_30m001").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_rondelle_30m001").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))

# part_ecrou_30m
x = 0
y = 0
z = (1000 - L_tube)/2 - 5 - h_palier_2_fixation_support - h_rondelle_30m - h_ecrou_30m - h_rondelle_30m - h_palier_2_fixation_ossature - h_rondelle_30m - h_ecrou_30m
color = (0.40, 0.30, 0.00)
part_ecrou_30m_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_2/Stl/part_ecrou_30m.stl"
Mesh.insert(part_ecrou_30m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_ecrou_30m").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_ecrou_30m").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))

# part_rondelle_30m
x = 0
y = 0
z = (1000 - L_tube)/2 + L_tube + h_palier_2_fixation_support + h_rondelle_30m + h_ecrou_30m + h_rondelle_30m + 3
color = (0.90, 0.50, 0.40)
part_rondelle_30m_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_2/Stl/part_rondelle_30m.stl"
Mesh.insert(part_rondelle_30m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_rondelle_30m002").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_rondelle_30m002").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))

# part_palier_2_fixation_ossature
x = -165/2
y = 84/2
z = (1000 - L_tube)/2 + L_tube + h_palier_2_fixation_support + h_rondelle_30m + h_ecrou_30m + h_rondelle_30m + 3 + h_rondelle_30m
color = (0.50, 0.90, 0.40)
part_palier_2_fixation_ossature_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_2/Stl/part_palier_2_fixation_ossature.stl"
Mesh.insert(part_palier_2_fixation_ossature_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_palier_2_fixation_ossature001").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_palier_2_fixation_ossature001").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))

# part_rondelle_30m
x = 0
y = 0
z = (1000 - L_tube)/2 + L_tube + h_palier_2_fixation_support + h_rondelle_30m + h_ecrou_30m + h_rondelle_30m + 3 + h_rondelle_30m + h_palier_2_fixation_ossature
color = (0.90, 0.50, 0.40)
part_rondelle_30m_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_2/Stl/part_rondelle_30m.stl"
Mesh.insert(part_rondelle_30m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_rondelle_30m003").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_rondelle_30m003").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))

# part_ecrou_30m
x = 0
y = 0
z = (1000 - L_tube)/2 + L_tube + h_palier_2_fixation_support + h_rondelle_30m + h_ecrou_30m + h_rondelle_30m + 3 + h_rondelle_30m + h_palier_2_fixation_ossature + h_rondelle_30m
color = (0.40, 0.30, 0.00)
part_ecrou_30m_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_2/Stl/part_ecrou_30m.stl"
Mesh.insert(part_ecrou_30m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_ecrou_30m001").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_ecrou_30m001").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))

# assembly_poulie
x = 0
y = 0
z = - h_palier_2_fixation_ossature - h_rondelle_30m - h_ecrou_30m + 1
color = (0.40, 0.40, 0.40)
assembly_poulie_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_2/Stl/assembly_poulie.stl"
Mesh.insert(assembly_poulie_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("assembly_poulie").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("assembly_poulie").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))

# assembly_poulie
x = 0
y = 0
z = (1000 - L_tube)/2 + L_tube + h1 + h_palier_2_fixation_support + h_rondelle_30m + h_ecrou_30m + h_rondelle_30m + h_palier_2_fixation_ossature + h_rondelle_30m + h_ecrou_30m + h_ecrou_30m/2 + 2
color = (0.40, 0.40, 0.40)
assembly_poulie_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_2/Stl/assembly_poulie.stl"
Mesh.insert(assembly_poulie_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("assembly_poulie001").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("assembly_poulie001").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),180))

setview()

# Export
__objs__ = []

__objs__.append(FreeCAD.getDocument(assembly).getObject("assembly_shaft"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("assembly_support"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("assembly_support001"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_tige_filetee_m16_1000l_cut"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_tige_filetee_m16_1000l_cut001"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_palier_2_fixation_ossature"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_palier_2_fixation_ossature001"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_rondelle_30m"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_rondelle_30m001"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_ecrou_30m"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_rondelle_30m002"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_ecrou_30m001"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("assembly_poulie"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("assembly_poulie001"))

Mesh.export(__objs__,u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_2/Stl/" + assembly + ".stl")

del __objs__

# Generate PNG files
file = 'C:\\Users\\Jason\\Documents\\Devs\\Python-Macros-For-FreeCAD\\HG\\Version_2\\Png\\assembly_generator_'
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
