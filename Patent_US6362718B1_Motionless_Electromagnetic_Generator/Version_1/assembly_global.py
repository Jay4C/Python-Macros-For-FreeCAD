import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_global"


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

L_part_steel_box_for_core_8mm_8mm_200mm = 200

# Export assembly_global
__objs__ = []

# part_steel_box_for_core_8mm_8mm_200mm - 1
Mesh.insert(u"part_steel_box_for_core_8mm_8mm_200mm.stl","assembly_global")
FreeCADGui.getDocument("assembly_global").getObject("part_steel_box_for_core_8mm_8mm_200mm").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_global").getObject("part_steel_box_for_core_8mm_8mm_200mm").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_global").getObject("part_steel_box_for_core_8mm_8mm_200mm"))

number_of_permanent_magnet_neodyme_n40_8mm_3mm_per_output_coil = round(50/3)

# part_permanent_magnet_neodyme_n40_8mm_3mm
for i in range(0, number_of_permanent_magnet_neodyme_n40_8mm_3mm_per_output_coil):
    if i == 0:
        Mesh.insert(u"part_permanent_magnet_neodyme_n40_8mm_3mm.stl","assembly_global")
        FreeCADGui.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm").ShapeColor = (0.30,0.30,0.30)
        FreeCAD.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm").Placement = App.Placement(App.Vector(4,4,8 + 3*i),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm"))
    elif i >= 1 and i < 10:
        Mesh.insert(u"part_permanent_magnet_neodyme_n40_8mm_3mm.stl","assembly_global")
        FreeCADGui.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm00" + str(i)).ShapeColor = (0.30,0.30,0.30)
        FreeCAD.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm00" + str(i)).Placement = App.Placement(App.Vector(4,4,8 + 3*i),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm00" + str(i)))
    elif i >= 10 and i < 100:
        Mesh.insert(u"part_permanent_magnet_neodyme_n40_8mm_3mm.stl","assembly_global")
        FreeCADGui.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm0" + str(i)).ShapeColor = (0.30,0.30,0.30)
        FreeCAD.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm0" + str(i)).Placement = App.Placement(App.Vector(4,4,8 + 3*i),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm0" + str(i)))
    elif i >= 100 and i < 1000:
        Mesh.insert(u"part_permanent_magnet_neodyme_n40_8mm_3mm.stl","assembly_global")
        FreeCADGui.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm" + str(i)).ShapeColor = (0.30,0.30,0.30)
        FreeCAD.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm" + str(i)).Placement = App.Placement(App.Vector(4,4,8 + 3*i),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm" + str(i)))

for i in range(number_of_permanent_magnet_neodyme_n40_8mm_3mm_per_output_coil, number_of_permanent_magnet_neodyme_n40_8mm_3mm_per_output_coil*2):
    if i == 0:
        Mesh.insert(u"part_permanent_magnet_neodyme_n40_8mm_3mm.stl","assembly_global")
        FreeCADGui.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm").ShapeColor = (0.30,0.30,0.30)
        FreeCAD.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm").Placement = App.Placement(App.Vector(L_part_steel_box_for_core_8mm_8mm_200mm/2,4,8 + 3*(i-number_of_permanent_magnet_neodyme_n40_8mm_3mm_per_output_coil)),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm"))
    elif i >= 1 and i < 10:
        Mesh.insert(u"part_permanent_magnet_neodyme_n40_8mm_3mm.stl","assembly_global")
        FreeCADGui.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm00" + str(i)).ShapeColor = (0.30,0.30,0.30)
        FreeCAD.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm00" + str(i)).Placement = App.Placement(App.Vector(L_part_steel_box_for_core_8mm_8mm_200mm/2,4,8 + 3*(i-number_of_permanent_magnet_neodyme_n40_8mm_3mm_per_output_coil)),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm00" + str(i)))
    elif i >= 10 and i < 100:
        Mesh.insert(u"part_permanent_magnet_neodyme_n40_8mm_3mm.stl","assembly_global")
        FreeCADGui.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm0" + str(i)).ShapeColor = (0.30,0.30,0.30)
        FreeCAD.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm0" + str(i)).Placement = App.Placement(App.Vector(L_part_steel_box_for_core_8mm_8mm_200mm/2,4,8 + 3*(i-number_of_permanent_magnet_neodyme_n40_8mm_3mm_per_output_coil)),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm0" + str(i)))
    elif i >= 100 and i < 1000:
        Mesh.insert(u"part_permanent_magnet_neodyme_n40_8mm_3mm.stl","assembly_global")
        FreeCADGui.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm" + str(i)).ShapeColor = (0.30,0.30,0.30)
        FreeCAD.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm" + str(i)).Placement = App.Placement(App.Vector(L_part_steel_box_for_core_8mm_8mm_200mm/2,4,8 + 3*(i-number_of_permanent_magnet_neodyme_n40_8mm_3mm_per_output_coil)),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm" + str(i)))
        
for i in range(number_of_permanent_magnet_neodyme_n40_8mm_3mm_per_output_coil*2, number_of_permanent_magnet_neodyme_n40_8mm_3mm_per_output_coil*3):
    if i == 0:
        Mesh.insert(u"part_permanent_magnet_neodyme_n40_8mm_3mm.stl","assembly_global")
        FreeCADGui.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm").ShapeColor = (0.30,0.30,0.30)
        FreeCAD.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm").Placement = App.Placement(App.Vector(L_part_steel_box_for_core_8mm_8mm_200mm - 4,4,8 + 3*(i-number_of_permanent_magnet_neodyme_n40_8mm_3mm_per_output_coil*2)),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm"))
    elif i >= 1 and i < 10:
        Mesh.insert(u"part_permanent_magnet_neodyme_n40_8mm_3mm.stl","assembly_global")
        FreeCADGui.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm00" + str(i)).ShapeColor = (0.30,0.30,0.30)
        FreeCAD.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm00" + str(i)).Placement = App.Placement(App.Vector(L_part_steel_box_for_core_8mm_8mm_200mm - 4,4,8 + 3*(i-number_of_permanent_magnet_neodyme_n40_8mm_3mm_per_output_coil*2)),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm00" + str(i)))
    elif i >= 10 and i < 100:
        Mesh.insert(u"part_permanent_magnet_neodyme_n40_8mm_3mm.stl","assembly_global")
        FreeCADGui.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm0" + str(i)).ShapeColor = (0.30,0.30,0.30)
        FreeCAD.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm0" + str(i)).Placement = App.Placement(App.Vector(L_part_steel_box_for_core_8mm_8mm_200mm - 4,4,8 + 3*(i-number_of_permanent_magnet_neodyme_n40_8mm_3mm_per_output_coil*2)),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm0" + str(i)))
    elif i >= 100 and i < 1000:
        Mesh.insert(u"part_permanent_magnet_neodyme_n40_8mm_3mm.stl","assembly_global")
        FreeCADGui.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm" + str(i)).ShapeColor = (0.30,0.30,0.30)
        FreeCAD.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm" + str(i)).Placement = App.Placement(App.Vector(L_part_steel_box_for_core_8mm_8mm_200mm - 4,4,8 + 3*(i-number_of_permanent_magnet_neodyme_n40_8mm_3mm_per_output_coil*2)),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm" + str(i)))

# part_steel_box_for_core_8mm_8mm_200mm - 2
Mesh.insert(u"part_steel_box_for_core_8mm_8mm_200mm.stl","assembly_global")
FreeCADGui.getDocument("assembly_global").getObject("part_steel_box_for_core_8mm_8mm_200mm001").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_global").getObject("part_steel_box_for_core_8mm_8mm_200mm001").Placement = App.Placement(App.Vector(0,0,8 + 3*number_of_permanent_magnet_neodyme_n40_8mm_3mm_per_output_coil),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_global").getObject("part_steel_box_for_core_8mm_8mm_200mm001"))

# part_output_coil_without_windings_di8mm_dc26mm_de40mm_hc50mm - 1
Mesh.insert(u"part_output_coil_without_windings_di8mm_dc26mm_de40mm_hc50mm.stl","assembly_global")
FreeCADGui.getDocument("assembly_global").getObject("part_output_coil_without_windings_di8mm_dc26mm_de40mm_hc50mm").ShapeColor = (0.90,0.60,0.30)
FreeCAD.getDocument("assembly_global").getObject("part_output_coil_without_windings_di8mm_dc26mm_de40mm_hc50mm").Placement = App.Placement(App.Vector(4,4,8),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_global").getObject("part_output_coil_without_windings_di8mm_dc26mm_de40mm_hc50mm"))

# part_output_coil_without_windings_di8mm_dc26mm_de40mm_hc50mm - 2
Mesh.insert(u"part_output_coil_without_windings_di8mm_dc26mm_de40mm_hc50mm.stl","assembly_global")
FreeCADGui.getDocument("assembly_global").getObject("part_output_coil_without_windings_di8mm_dc26mm_de40mm_hc50mm001").ShapeColor = (0.90,0.60,0.30)
FreeCAD.getDocument("assembly_global").getObject("part_output_coil_without_windings_di8mm_dc26mm_de40mm_hc50mm001").Placement = App.Placement(App.Vector(L_part_steel_box_for_core_8mm_8mm_200mm/2,4,8),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_global").getObject("part_output_coil_without_windings_di8mm_dc26mm_de40mm_hc50mm001"))

# part_output_coil_without_windings_di8mm_dc26mm_de40mm_hc50mm - 3
Mesh.insert(u"part_output_coil_without_windings_di8mm_dc26mm_de40mm_hc50mm.stl","assembly_global")
FreeCADGui.getDocument("assembly_global").getObject("part_output_coil_without_windings_di8mm_dc26mm_de40mm_hc50mm002").ShapeColor = (0.90,0.60,0.30)
FreeCAD.getDocument("assembly_global").getObject("part_output_coil_without_windings_di8mm_dc26mm_de40mm_hc50mm002").Placement = App.Placement(App.Vector(L_part_steel_box_for_core_8mm_8mm_200mm - 4,4,8),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_global").getObject("part_output_coil_without_windings_di8mm_dc26mm_de40mm_hc50mm002"))

# part_input_coil_without_windings_htube8mm_de40mm - 1
Mesh.insert(u"part_input_coil_without_windings_htube8mm_de40mm.stl","assembly_global")
FreeCADGui.getDocument("assembly_global").getObject("part_input_coil_without_windings_htube8mm_de40mm").ShapeColor = (0.30,0.60,0.60)
FreeCAD.getDocument("assembly_global").getObject("part_input_coil_without_windings_htube8mm_de40mm").Placement = App.Placement(App.Vector(L_part_steel_box_for_core_8mm_8mm_200mm/4,4,4),App.Rotation(App.Vector(0,1,0),90))
__objs__.append(FreeCAD.getDocument("assembly_global").getObject("part_input_coil_without_windings_htube8mm_de40mm"))

# part_input_coil_without_windings_htube8mm_de40mm - 2
Mesh.insert(u"part_input_coil_without_windings_htube8mm_de40mm.stl","assembly_global")
FreeCADGui.getDocument("assembly_global").getObject("part_input_coil_without_windings_htube8mm_de40mm001").ShapeColor = (0.30,0.60,0.60)
FreeCAD.getDocument("assembly_global").getObject("part_input_coil_without_windings_htube8mm_de40mm001").Placement = App.Placement(App.Vector(3*(L_part_steel_box_for_core_8mm_8mm_200mm/4),4,4),App.Rotation(App.Vector(0,1,0),90))
__objs__.append(FreeCAD.getDocument("assembly_global").getObject("part_input_coil_without_windings_htube8mm_de40mm001"))

# part_input_coil_without_windings_htube8mm_de40mm - 3
Mesh.insert(u"part_input_coil_without_windings_htube8mm_de40mm.stl","assembly_global")
FreeCADGui.getDocument("assembly_global").getObject("part_input_coil_without_windings_htube8mm_de40mm002").ShapeColor = (0.30,0.60,0.60)
FreeCAD.getDocument("assembly_global").getObject("part_input_coil_without_windings_htube8mm_de40mm002").Placement = App.Placement(App.Vector(L_part_steel_box_for_core_8mm_8mm_200mm/4,4,4 + 8 + 3*number_of_permanent_magnet_neodyme_n40_8mm_3mm_per_output_coil),App.Rotation(App.Vector(0,1,0),90))
__objs__.append(FreeCAD.getDocument("assembly_global").getObject("part_input_coil_without_windings_htube8mm_de40mm002"))

# part_input_coil_without_windings_htube8mm_de40mm - 4
Mesh.insert(u"part_input_coil_without_windings_htube8mm_de40mm.stl","assembly_global")
FreeCADGui.getDocument("assembly_global").getObject("part_input_coil_without_windings_htube8mm_de40mm003").ShapeColor = (0.30,0.60,0.60)
FreeCAD.getDocument("assembly_global").getObject("part_input_coil_without_windings_htube8mm_de40mm003").Placement = App.Placement(App.Vector(3*(L_part_steel_box_for_core_8mm_8mm_200mm/4),4,4 + 8 + 3*number_of_permanent_magnet_neodyme_n40_8mm_3mm_per_output_coil),App.Rotation(App.Vector(0,1,0),90))
__objs__.append(FreeCAD.getDocument("assembly_global").getObject("part_input_coil_without_windings_htube8mm_de40mm003"))

setview()

Mesh.export(__objs__,u"assembly_global.stl")

del __objs__

# Generate PNG files
file = 'assembly_global_'
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
