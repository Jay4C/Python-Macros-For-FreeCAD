# https://wiki.freecadweb.org/Scripting_examples
# https://wiki.freecadweb.org/Scripted_objects_with_attachment

import FreeCAD as App

import Part



class Box():

    """

    Simple Custom Box Object

    See Also:

        https://wiki.freecadweb.org/FeaturePython_Objects

    """


    def __init__(self, obj):

        """

        Constructor

        Arguments

        ---------

        - obj: an existing document object or an object created with FreeCAD.Document.addObject('Part::FeaturePython', '{name}').

        """


        self.Type = 'Box'


        obj.Proxy = self

        obj.addProperty('App::PropertyLength', 'Length',

                        'Dimensions', 'Box length').Length = 10.0

        obj.addProperty('App::PropertyLength', 'Width',

                        'Dimensions', 'Box width').Width = 10.0

        obj.addProperty('App::PropertyLength', 'Height',

                        'Dimensions', 'Box height').Height = 10.0


        # Needed to make this object "attachable",

        # or able to attach parameterically to other objects

        obj.addExtension('Part::AttachExtensionPython', obj)


    def execute(self, obj):

        """

        Called on document recompute

        """

        # Needed to update position when attached-to object changes position.

        # Reposition object based on Support, MapMode and MapPathParameter properties.

        # Returns True if attachment calculation was successful, False if object is not attached and Placement wasn't updated,

        obj.positionBySupport()


        obj.Shape = Part.makeBox(obj.Length, obj.Width, obj.Height)



def create_box(obj_name, document):

    """

    Create a Box.

    """

    obj = document.addObject('Part::FeaturePython', obj_name)

    Box(obj)

    obj.ViewObject.Proxy = 0  # Mandatory unless ViewProvider is coded

    return obj



document = App.ActiveDocument

if document is None:

    document = App.newDocument('Part Attachment Example')


box = create_box('CustomBox', document)

document.recompute()
