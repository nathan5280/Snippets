Blender can be run in three different modes.
1. Full GUI
1. Background
1. Module

In the Full GUI and Background modes scripts are executed in the Python environment within the 
Blender executable.  In the Module mode Blender runs inside of the Python environment.  
The same script will run in either environment assuming all of the correct libraries 
are installed in both environments.

*Note:* The Python interpreter in Blender is 3.5 and the one supported by the build for the 
module mode is 3.6.

**Building Blender Module**
1. Building the module basically follows these instructions.  
https://wiki.blender.org/index.php/User%3aIdeasman42/BlenderAsPyModule
1. Which point to these instructions. https://wiki.blender.org/index.php/Dev:Doc/Building_Blender/Linux/Ubuntu/CMake

When you get the dependencies taken care of:
1. Run the make command at the bottom of the BUILD_NOTES.txt file by adding the bpy target.
```commandline
$ make -j8 bpy BUILD_CMAKE_ARGS ...
```
1. After it builds the first time there will be a new directory blender-git/build_linux_bpy.
1. Edit CMakeCache.txt
```commandline
WIIH_PYTHON_INSTALL=OFF
WITH_PLAYER=OFF
WITH_PYTHON_MODULE=ON
```
1. Test that the build was successful:
* Set and export PYTHON_PATH to blender-git/build_linux_bpy/bin/.  
This is the location of bpy.so the blender library that is imported into Python.
* Start ipython
* import bpy

**Install Blender Module**
1. Copy bpy.so to lib/python3.6
2. Copy blender-git/build_linux_bpy/bin/2.79 to lib/python3.6/2.79
3. In a new terminal that doesn't have the above PYTHON_PATH set perform the test to
insure that bpy can be imported.


