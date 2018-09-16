import Part
doc = App.activeDocument()
c = Part.Circle() 
c.Radius=20.0 
f = doc.addObject("Part::Feature", "Circle") # create a document with a circle feature 
f.Shape = c.toShape() # Assign the circle shape to the shape property 
doc.recompute() 