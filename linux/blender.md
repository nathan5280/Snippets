# Blender

Download from blender.org

Extract
```commandline
tar -vxjf <file.tar.bz2>
```

Rename and install
```commandline
mv blender... blender
sudo mv blender /usr/lib/blender
```

Add an alias to .bashrc

```commandline
alias blender=/usr/lib/blender/blender
```

##Blender as a Module (bpy)
###General Process for building latest blender.
```
https://wiki.blender.org/index.php/Dev:Doc/Building_Blender/Linux/Ubuntu/CMake
```

If you want a specific version to match the prebuilt executable make these changes.
Get the snapshot from git.blender.org for the version you are interested in.
For 2.79b it is here:
```commandline
https://git.blender.org/gitweb/gitweb.cgi/blender.git/tree/f4dc9f9d68bddaa206b692e1d077d1a1f2bb1528
```

Unzip, untar, move the snapshot.
```commandline
gunzip <blender...>
tar -xf <blender...>
mv <blender...> blender-git
```
Get tools to build.
```commandline
sudo apt update
sudo apt install build-essential
```

Install the dependencies.
```commandline
cd blender-git
./build_files/build_environment/install_dep.sh
```

Install Cmake
```commandline
sudo apt install cmake cmake-curses-gui, cmake-qt-gui
```

Make the module using the bpy target.
```commandline
sudo make bpy
```


Fake module for code completion ni PyCharm
```commandline
https://github.com/nutti/fake-bpy-module
```

https://gist.github.com/alexlee-gk/3790bf5916649082d9d6

# Installing site-packages
With Conda / ipython load module and see where it loads from.  Make sure the virtual environment
interpreter matches blender's.

Virtual Env
python --version
... 3.5.3 ...


Blender
import sys
sys.version

... 3.5.3

import module_name
module_name.__file__

It should be loading from somewhere in site-packages under the conda virtual environment.

In script:

import sys
sys.path.append("<virtual-env>.site-packages")

or 

set PYTHONPATH to include <virtual-env>.sit-packages
