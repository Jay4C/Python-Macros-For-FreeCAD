import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_of_the_voltage_intensifier_circuit"


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

# part_squelette_primaire_d80_l80
cylinder_1 = Part.makeCylinder(40, 80)

cylinder_2 = Part.makeCylinder(6, 80)

# cylinder_1 cut by cylinder_2
cylinder_1 = cylinder_1.cut(cylinder_2)

cylinder_3 = Part.makeCylinder(40, 33.5)

cylinder_4 = Part.makeCylinder(8, 33.5)

# cylinder_3 cut by cylinder_4
cylinder_3 = cylinder_3.cut(cylinder_4)

# cylinder_1 cut by cylinder_3 in 2 times
cylinder_3_vector = FreeCAD.Vector(0, 0, 2)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)
cylinder_3_vector = FreeCAD.Vector(0, 0, 42.5)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

cylinder_5 = Part.makeCylinder(40, 5)

cylinder_6 = Part.makeCylinder(8, 5)

# cylinder_5 cut by cylinder_6
cylinder_5 = cylinder_5.cut(cylinder_6)

# cylinder_1 cut by cylinder_5
cylinder_5_vector = FreeCAD.Vector(0, 0, 37.5)
cylinder_5.translate(cylinder_5_vector)
cylinder_1 = cylinder_1.cut(cylinder_5)

Part.show(cylinder_1)

DOC.recompute()

# change color of assembly_of_the_voltage_intensifier_circuit
FreeCADGui.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("Shape").ShapeColor = (0.67,0.00,0.00)

# insertion part_squelette_secondaire_d80_l80
Mesh.insert(u"part_squelette_secondaire_d80_l80.stl", "assembly_of_the_voltage_intensifier_circuit")
FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_squelette_secondaire_d80_l80").Placement = App.Placement(App.Vector(84, 0, 0), App.Rotation(App.Vector(1,0,0), 0))
FreeCADGui.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_squelette_secondaire_d80_l80").ShapeColor = (0.33,1.00,1.00)

# insertion equerre_assemblage_plat_l100 - 1
Mesh.insert(u"equerre_assemblage_plat_l100.stl", "assembly_of_the_voltage_intensifier_circuit")
FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("equerre_assemblage_plat_l100").Placement = App.Placement(App.Vector(-8, -8, -2), App.Rotation(App.Vector(1,0,0), 0))
FreeCADGui.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("equerre_assemblage_plat_l100").ShapeColor = (1.00,1.00,0.50)

# insertion equerre_assemblage_plat_l100 - 2
Mesh.insert(u"equerre_assemblage_plat_l100.stl", "assembly_of_the_voltage_intensifier_circuit")
FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("equerre_assemblage_plat_l100001").Placement = App.Placement(App.Vector(-8, -8, -4), App.Rotation(App.Vector(1,0,0), 0))
FreeCADGui.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("equerre_assemblage_plat_l100001").ShapeColor = (1.00,0.33,1.00)

# insertion equerre_assemblage_plat_l100 - 3
Mesh.insert(u"equerre_assemblage_plat_l100.stl", "assembly_of_the_voltage_intensifier_circuit")
FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("equerre_assemblage_plat_l100002").Placement = App.Placement(App.Vector(-8, -8, 80), App.Rotation(App.Vector(1,0,0), 0))
FreeCADGui.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("equerre_assemblage_plat_l100002").ShapeColor = (1.00,1.00,0.50)

# insertion equerre_assemblage_plat_l100 - 4
Mesh.insert(u"equerre_assemblage_plat_l100.stl", "assembly_of_the_voltage_intensifier_circuit")
FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("equerre_assemblage_plat_l100003").Placement = App.Placement(App.Vector(-8, -8, 82), App.Rotation(App.Vector(1,0,0), 0))
FreeCADGui.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("equerre_assemblage_plat_l100003").ShapeColor = (1.00,0.33,1.00)

# insertion part_equerre_assemblage_angle_droit_l42 - 1
Mesh.insert(u"part_equerre_assemblage_angle_droit_l42.stl", "assembly_of_the_voltage_intensifier_circuit")
FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_equerre_assemblage_angle_droit_l42").Placement = App.Placement(App.Vector(-8, -32.5, -4), App.Rotation(App.Vector(0,1,0), 90))
FreeCADGui.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_equerre_assemblage_angle_droit_l42").ShapeColor = (1.00,0.33,0.00)

# insertion part_equerre_assemblage_angle_droit_l42 - 2
Mesh.insert(u"part_equerre_assemblage_angle_droit_l42.stl", "assembly_of_the_voltage_intensifier_circuit")
FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_equerre_assemblage_angle_droit_l42001").Placement = App.Placement(App.Vector(78, -32.5, -4), App.Rotation(App.Vector(0,1,0), 90))
FreeCADGui.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_equerre_assemblage_angle_droit_l42001").ShapeColor = (1.00,0.33,0.00)

# insertion part_equerre_assemblage_angle_droit_l42 - 3
Mesh.insert(u"part_equerre_assemblage_angle_droit_l42.stl", "assembly_of_the_voltage_intensifier_circuit")
FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_equerre_assemblage_angle_droit_l42002").Placement = App.Placement(App.Vector(8, -32.5, 84), App.Rotation(App.Vector(0,1,0), -90))
FreeCADGui.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_equerre_assemblage_angle_droit_l42002").ShapeColor = (1.00,0.33,0.00)

# insertion part_equerre_assemblage_angle_droit_l42 - 4
Mesh.insert(u"part_equerre_assemblage_angle_droit_l42.stl", "assembly_of_the_voltage_intensifier_circuit")
FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_equerre_assemblage_angle_droit_l42003").Placement = App.Placement(App.Vector(90, -32.5, 84), App.Rotation(App.Vector(0,1,0), -90))
FreeCADGui.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_equerre_assemblage_angle_droit_l42003").ShapeColor = (1.00,0.33,0.00)

# insertion part_vis_metal_m12_l100 - 1
Mesh.insert(u"part_vis_metal_m12_l100.stl", "assembly_of_the_voltage_intensifier_circuit")
FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_vis_metal_m12_l100").Placement = App.Placement(App.Vector(0, 0, -14), App.Rotation(App.Vector(0,1,0), 0))
FreeCADGui.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_vis_metal_m12_l100").ShapeColor = (0.67,0.67,0.00)

# insertion part_vis_metal_m12_l100 - 2
Mesh.insert(u"part_vis_metal_m12_l100.stl", "assembly_of_the_voltage_intensifier_circuit")
FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_vis_metal_m12_l100001").Placement = App.Placement(App.Vector(84, 0, -14), App.Rotation(App.Vector(0,1,0), 0))
FreeCADGui.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_vis_metal_m12_l100001").ShapeColor = (0.67,0.67,0.00)

# insertion part_ecrou_m12 - 1
Mesh.insert(u"part_ecrou_m12.stl", "assembly_of_the_voltage_intensifier_circuit")
FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_ecrou_m12").Placement = App.Placement(App.Vector(0, 0, 86), App.Rotation(App.Vector(0,1,0), 0))
FreeCADGui.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_ecrou_m12").ShapeColor = (0.67,0.33,0.50)

# insertion part_ecrou_m12 - 2
Mesh.insert(u"part_ecrou_m12.stl", "assembly_of_the_voltage_intensifier_circuit")
FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_ecrou_m12001").Placement = App.Placement(App.Vector(84, 0, 86), App.Rotation(App.Vector(0,1,0), 0))
FreeCADGui.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_ecrou_m12001").ShapeColor = (0.67,0.33,0.50)

__objs__=[]
__objs__.append(FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("Shape"))
__objs__.append(FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_squelette_secondaire_d80_l80"))
__objs__.append(FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("equerre_assemblage_plat_l100"))
__objs__.append(FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("equerre_assemblage_plat_l100001"))
__objs__.append(FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("equerre_assemblage_plat_l100002"))
__objs__.append(FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("equerre_assemblage_plat_l100003"))
__objs__.append(FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_equerre_assemblage_angle_droit_l42"))
__objs__.append(FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_equerre_assemblage_angle_droit_l42001"))
__objs__.append(FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_equerre_assemblage_angle_droit_l42002"))
__objs__.append(FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_equerre_assemblage_angle_droit_l42003"))
__objs__.append(FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_vis_metal_m12_l100"))
__objs__.append(FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_vis_metal_m12_l100001"))
__objs__.append(FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_ecrou_m12"))
__objs__.append(FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_ecrou_m12001"))

Mesh.export(__objs__,u"assembly_of_the_voltage_intensifier_circuit.stl")
 
del __objs__

setview()
         