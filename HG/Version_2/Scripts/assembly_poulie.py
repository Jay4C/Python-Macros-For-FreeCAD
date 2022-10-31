import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_poulie"


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

assembly = "assembly_poulie"

# Parameters
h_rondelle_30m = 4
h_poulie_generator = 25.4
k_vis_metal_30m_70l = 18.7

# part_moyeu_amovible_generator
color = (0.10, 0.20, 0.30)
part_moyeu_amovible_generator_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_2/Stl/part_moyeu_amovible_generator.stl"
Mesh.insert(part_moyeu_amovible_generator_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_moyeu_amovible_generator").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_moyeu_amovible_generator").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))

# part_poulie_generator
color = (0.30, 0.60, 0.90)
part_poulie_generator_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_2/Stl/part_poulie_generator.stl"
Mesh.insert(part_poulie_generator_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_poulie_generator").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_poulie_generator").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_30m
x = 0
y = 0
z = h_poulie_generator
color = (0.10, 0.00, 0.00)
part_rondelle_30m_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_2/Stl/part_rondelle_30m.stl"
Mesh.insert(part_rondelle_30m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_rondelle_30m").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_rondelle_30m").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_30m
x = 0
y = 0
z = - h_rondelle_30m
color = (0.10, 0.00, 0.00)
part_rondelle_30m_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_2/Stl/part_rondelle_30m.stl"
Mesh.insert(part_rondelle_30m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_rondelle_30m001").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_rondelle_30m001").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

# part_vis_metal_m30_70l
x = 0
y = 0
z = - h_rondelle_30m - k_vis_metal_30m_70l
color = (0.10, 0.90, 0.90)
part_vis_metal_m30_70l_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_2/Stl/part_vis_metal_m30_70l.stl"
Mesh.insert(part_vis_metal_m30_70l_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_vis_metal_m30_70l").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_vis_metal_m30_70l").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

# part_accouplement_rigide_mecanique
x = 0
y = 0
z = h_poulie_generator + h_rondelle_30m
color = (0.20, 0.70, 0.90)
part_accouplement_rigide_mecanique_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_2/Stl/part_accouplement_rigide_mecanique.stl"
Mesh.insert(part_accouplement_rigide_mecanique_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_accouplement_rigide_mecanique").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_accouplement_rigide_mecanique").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

setview()

# Export
__objs__ = []

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_moyeu_amovible_generator"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_poulie_generator"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_rondelle_30m"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_rondelle_30m001"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_vis_metal_m30_70l"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_accouplement_rigide_mecanique"))

Mesh.export(__objs__,u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_2/Stl/" + assembly + ".stl")

del __objs__
