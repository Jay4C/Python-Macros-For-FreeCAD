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

# Parameters
h_rondelle_30m = 4
h_rondelle_16m = 3
h_ecrou_30m = 30
e_support = 5
h_palier_2_fixation_support = 40.2
h_palier_2_fixation_ossature = 48
h_poulie_generator = 25.4
L_tube = 1000 - (e_support + h_palier_2_fixation_support + h_rondelle_30m + h_ecrou_30m + h_rondelle_30m + h_palier_2_fixation_ossature + h_rondelle_30m + h_ecrou_30m + h_rondelle_30m + h_poulie_generator + h_rondelle_30m + h_ecrou_30m) - (e_support + h_palier_2_fixation_support + h_rondelle_30m + h_ecrou_30m + h_rondelle_30m + h_palier_2_fixation_ossature + h_rondelle_30m + h_ecrou_30m)
h1 = (L_tube - 400)/2

# part_support
color = (0.10, 0.20, 0.30)
part_support_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_2/Stl/part_support.stl"
Mesh.insert(part_support_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_support").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_support").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))

# part_palier_2_fixation_support
x = -148/2
y = 80/2
z = h1
color = (0.20, 0.40, 0.60)
part_palier_2_fixation_support_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_2/Stl/part_palier_2_fixation_support.stl"
Mesh.insert(part_palier_2_fixation_support_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_palier_2_fixation_support").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_palier_2_fixation_support").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))    

# part_rondelle_30m
x = 0
y = 0
z = h1 + h_palier_2_fixation_support
color = (0.40, 0.60, 0.80)
part_rondelle_30m_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_2/Stl/part_rondelle_30m.stl"
Mesh.insert(part_rondelle_30m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_rondelle_30m").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_rondelle_30m").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_30m
x = 0
y = 0
z = h1 + h_palier_2_fixation_support + h_rondelle_30m
color = (0.60, 0.80, 0.90)
part_ecrou_30m_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_2/Stl/part_ecrou_30m.stl"
Mesh.insert(part_ecrou_30m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_ecrou_30m").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_ecrou_30m").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_16m
x = 117/2
y = 0
z = h1 + h_palier_2_fixation_support
color = (0.10, 0.00, 0.20)
part_rondelle_16m_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_2/Stl/part_rondelle_16m.stl"
Mesh.insert(part_rondelle_16m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_rondelle_16m").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_rondelle_16m").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_16m
x = -117/2
y = 0
z = h1 + h_palier_2_fixation_support
color = (0.10, 0.00, 0.20)
part_rondelle_16m_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_2/Stl/part_rondelle_16m.stl"
Mesh.insert(part_rondelle_16m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_rondelle_16m001").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_rondelle_16m001").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_16m
x = 117/2
y = 0
z = h1 + h_palier_2_fixation_support + h_rondelle_16m
color = (0.10, 0.90, 0.20)
part_ecrou_16m_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_2/Stl/part_ecrou_16m.stl"
Mesh.insert(part_ecrou_16m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_ecrou_16m").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_ecrou_16m").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_16m
x = -117/2
y = 0
z = h1 + h_palier_2_fixation_support + h_rondelle_16m
color = (0.10, 0.90, 0.20)
part_ecrou_16m_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_2/Stl/part_ecrou_16m.stl"
Mesh.insert(part_ecrou_16m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_ecrou_16m001").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_ecrou_16m001").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

setview()

# Export
__objs__ = []

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_support"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_palier_2_fixation_support"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_rondelle_30m"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_ecrou_30m"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_rondelle_16m"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_rondelle_16m001"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_ecrou_16m"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_ecrou_16m001"))

Mesh.export(__objs__,u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_2/Stl/" + assembly + ".stl")

del __objs__
