## Python-Macros-For-FreeCAD

This repository contain Python scripts to design Parts on FreeCAD, an opensource computer aided design (CAD) software. Instead of using a mouse to create 3D parts, Python scripts are used to autogenerate 3D parts instantly utilizing FreeCAD.

## Background

This repository's aim is to publish free energy devices in CAD to bring free energy devices to the world in order to escape poverty globally, maintain all eco-systems and escape censorship.

This repository publishes free energy devices invented by inventors like Stanley Meyer, Nikola Tesla, John Bedini, Viktor Schauberger, Chas Campbell, Edwin Gray, Thomas Henry Moray and others inventors who worked on free energy devices.

## Requirements

1. Visual Studio Code: https://code.visualstudio.com/
1. FreeCAD: https://www.freecad.org/ version 0.19 or higher
1. Python: https://www.python.org/ version ??

## Usage

1. Open FreeCAD.
1. Select the [Part Workbench](https://wiki.freecad.org/Part_Workbench) via the "Switch between workbenches" drop down.
1. Click on `View` button.
1. Click on Panels.
1. Click on [Python Console](https://wiki.freecad.org/Python_console).
1. Click on the "Create a new empty document" button.
1. Type the following in to the command-line: 
    ```python
    exec(open("the_path_of_your_file").read())
    ```
1. Click on the right button on your mouse to open a context menu
1. Click on `Fit all`

Result: The part is created by the script.

**Note:** All parts can be seen on Holomorphe's website (https://www.holomorphe.com - Computer aided designed) with BabylonJS viewer (https://doc.babylonjs.com/extensions/babylonViewer) with .stl format.

