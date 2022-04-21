import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_global_v2"


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

# Export assembly_global_v2
__objs__ = []

# part_permanent_magnet_neodyme_n40_10mm_40mm - 1
Mesh.insert(u"part_permanent_magnet_neodyme_n40_10mm_40mm.stl","assembly_global_v2")
FreeCADGui.getDocument("assembly_global_v2").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_global_v2").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm").Placement = App.Placement(App.Vector(40*0,0,0),App.Rotation(App.Vector(0,1,0),90))
__objs__.append(FreeCAD.getDocument("assembly_global_v2").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm"))

# part_permanent_magnet_neodyme_n40_10mm_40mm - 2
Mesh.insert(u"part_permanent_magnet_neodyme_n40_10mm_40mm.stl","assembly_global_v2")
FreeCADGui.getDocument("assembly_global_v2").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm001").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_global_v2").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm001").Placement = App.Placement(App.Vector(40*1,0,0),App.Rotation(App.Vector(0,1,0),90))
__objs__.append(FreeCAD.getDocument("assembly_global_v2").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm001"))

# part_permanent_magnet_neodyme_n40_10mm_40mm - 3
Mesh.insert(u"part_permanent_magnet_neodyme_n40_10mm_40mm.stl","assembly_global_v2")
FreeCADGui.getDocument("assembly_global_v2").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm002").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_global_v2").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm002").Placement = App.Placement(App.Vector(40*0,0,40 + 10),App.Rotation(App.Vector(0,1,0),90))
__objs__.append(FreeCAD.getDocument("assembly_global_v2").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm002"))

# part_permanent_magnet_neodyme_n40_10mm_40mm - 4
Mesh.insert(u"part_permanent_magnet_neodyme_n40_10mm_40mm.stl","assembly_global_v2")
FreeCADGui.getDocument("assembly_global_v2").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm003").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_global_v2").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm003").Placement = App.Placement(App.Vector(5,0,5),App.Rotation(App.Vector(0,1,0),0))
__objs__.append(FreeCAD.getDocument("assembly_global_v2").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm003"))

# part_permanent_magnet_neodyme_n40_10mm_40mm - 5
Mesh.insert(u"part_permanent_magnet_neodyme_n40_10mm_40mm.stl","assembly_global_v2")
FreeCADGui.getDocument("assembly_global_v2").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm004").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_global_v2").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm004").Placement = App.Placement(App.Vector(40*2 - 5,0,5),App.Rotation(App.Vector(0,1,0),0))
__objs__.append(FreeCAD.getDocument("assembly_global_v2").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm004"))

# part_permanent_magnet_neodyme_n40_10mm_40mm - 6
Mesh.insert(u"part_permanent_magnet_neodyme_n40_10mm_40mm.stl","assembly_global_v2")
FreeCADGui.getDocument("assembly_global_v2").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm005").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_global_v2").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm005").Placement = App.Placement(App.Vector(40*1,0,40 + 10),App.Rotation(App.Vector(0,1,0),90))
__objs__.append(FreeCAD.getDocument("assembly_global_v2").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm005"))

# part_output_coil_without_windings_di10mm_dw14mm_de40mm_hc36mm - 1
Mesh.insert(u"part_output_coil_without_windings_di10mm_dw14mm_de40mm_hc36mm.stl","assembly_global_v2")
FreeCADGui.getDocument("assembly_global_v2").getObject("part_output_coil_without_windings_di10mm_dw14mm_de40mm_hc36mm").ShapeColor = (0.60,0.60,0.60)
FreeCAD.getDocument("assembly_global_v2").getObject("part_output_coil_without_windings_di10mm_dw14mm_de40mm_hc36mm").Placement = App.Placement(App.Vector(5,0,7),App.Rotation(App.Vector(0,1,0),0))
__objs__.append(FreeCAD.getDocument("assembly_global_v2").getObject("part_output_coil_without_windings_di10mm_dw14mm_de40mm_hc36mm"))

# part_output_coil_without_windings_di10mm_dw14mm_de40mm_hc36mm - 2
Mesh.insert(u"part_output_coil_without_windings_di10mm_dw14mm_de40mm_hc36mm.stl","assembly_global_v2")
FreeCADGui.getDocument("assembly_global_v2").getObject("part_output_coil_without_windings_di10mm_dw14mm_de40mm_hc36mm001").ShapeColor = (0.60,0.60,0.60)
FreeCAD.getDocument("assembly_global_v2").getObject("part_output_coil_without_windings_di10mm_dw14mm_de40mm_hc36mm001").Placement = App.Placement(App.Vector(40*2 - 5,0,7),App.Rotation(App.Vector(0,1,0),0))
__objs__.append(FreeCAD.getDocument("assembly_global_v2").getObject("part_output_coil_without_windings_di10mm_dw14mm_de40mm_hc36mm001"))

# part_input_coil_without_windings_di10mm_dw14mm_de40mm_hc18mm - 1
Mesh.insert(u"part_input_coil_without_windings_di10mm_dw14mm_de40mm_hc18mm.stl","assembly_global_v2")
FreeCADGui.getDocument("assembly_global_v2").getObject("part_input_coil_without_windings_di10mm_dw14mm_de40mm_hc18mm").ShapeColor = (0.60,0.90,0.60)
FreeCAD.getDocument("assembly_global_v2").getObject("part_input_coil_without_windings_di10mm_dw14mm_de40mm_hc18mm").Placement = App.Placement(App.Vector((40*2 - 18)/2,0,0),App.Rotation(App.Vector(0,1,0),90))
__objs__.append(FreeCAD.getDocument("assembly_global_v2").getObject("part_input_coil_without_windings_di10mm_dw14mm_de40mm_hc18mm"))

# part_input_coil_without_windings_di10mm_dw14mm_de40mm_hc18mm - 2
Mesh.insert(u"part_input_coil_without_windings_di10mm_dw14mm_de40mm_hc18mm.stl","assembly_global_v2")
FreeCADGui.getDocument("assembly_global_v2").getObject("part_input_coil_without_windings_di10mm_dw14mm_de40mm_hc18mm001").ShapeColor = (0.60,0.90,0.60)
FreeCAD.getDocument("assembly_global_v2").getObject("part_input_coil_without_windings_di10mm_dw14mm_de40mm_hc18mm001").Placement = App.Placement(App.Vector((40*2 - 18)/2,0,40 + 10),App.Rotation(App.Vector(0,1,0),90))
__objs__.append(FreeCAD.getDocument("assembly_global_v2").getObject("part_input_coil_without_windings_di10mm_dw14mm_de40mm_hc18mm001"))

setview()

Mesh.export(__objs__,u"assembly_global_v2.stl")

del __objs__

# Generate PNG files
file = 'assembly_global_v2_'
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
