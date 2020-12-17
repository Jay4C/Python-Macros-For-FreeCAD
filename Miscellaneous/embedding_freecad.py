# https://wiki.freecadweb.org/Scripting_examples
# https://wiki.freecadweb.org/Embedding_FreeCAD

FREECADPATH = '/opt/FreeCAD/lib' # path to your FreeCAD.so or FreeCAD.dll file
import Blender, sys
sys.path.append(FREECADPATH)
 
def import_fcstd(filename):
   try:
       import FreeCAD
   except ValueError:
       Blender.Draw.PupMenu('Error%t|FreeCAD library not found. Please check the FREECADPATH variable in the import script is correct')
   else:
       scene = Blender.Scene.GetCurrent()
       import Part
       doc = FreeCAD.open(filename)
       objects = doc.Objects
       for ob in objects:
           if ob.Type[:4] == 'Part':
               shape = ob.Shape
               if shape.Faces:
                   mesh = Blender.Mesh.New()
                   rawdata = shape.tessellate(1)
                   for v in rawdata[0]:
                       mesh.verts.append((v.x,v.y,v.z))
                   for f in rawdata[1]:
                       mesh.faces.append.append(f)
                   scene.objects.new(mesh,ob.Name)
       Blender.Redraw()

def main():
   Blender.Window.FileSelector(import_fcstd, 'IMPORT FCSTD', 
                        Blender.sys.makename(ext='.fcstd'))    
 
# This lets you import the script without running it
if __name__=='__main__':
   main()

import FreeCADGui 
FreeCADGui.showMainWindow()
