import Part
doc = App.activeDocument()
c = Part.Circle()
c.Radius = 20.0
# create a document with a circle feature
f = doc.addObject("Part::Feature", "Circle")
f.Shape = c.toShape()  # Assign the circle shape to the shape property
doc.recompute()
