# https://wiki.freecadweb.org/Scripting_examples
# https://wiki.freecadweb.org/Scenegraph

#Inventor V2.0 ascii
 
Separator { 
    RotationXYZ {	
       axis Z
       angle 0
    }
    Transform {
       translation 0 0 0.5
    }
    Separator {	
       Material {
          diffuseColor 0.05 0.05 0.05
       }
       Transform {
          rotation 1 0 0 1.5708
          scaleFactor 0.2 0.5 0.2
       }
       Cylinder {
       }
    }
}

obj = FreeCAD.ActiveDocument.ActiveObject
viewprovider = obj.ViewObject
print viewprovider.toString()
