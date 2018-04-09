Install a version of Ubuntu that is supported by Nvidia.  
This includes the graphics driver, cuda and cudnn.  
Also, make sure that the version of Tensorflow to install 
also is supported by these versions of Nvidia.  
If this isn't all right then the models all have to be compiled from scratch and that is a bit messy.

#Dependencies
For this build in depencency order:
* Tensorflow-gpu 1.5
* Tensorflow 1.5
* Cuda 9.0
* Cudnn 7.x
* Nvidia graphics driver 390
* Ubuntu 16.04

# Table of Contents
1. [Update and Upgrade](#update-and-upgrade)
1. [Google Chrome](#google-chrome)
1. [Nvidia Graphics Driver](#nvidia-graphics-driver)
1. [PyCharm](#pycharm)
1. [Nvidia CUDA](#nvidia-cuda)
1. [Nvidia CUDA Toolkit](#nvidia-cuda-toolkit)
1. [Nvidia CUDA DNN](#nvidia-cuda-dnn)
1. [Python 3.6](#python-3.6)
1. [PIP](#pip)
1. [Virtual Environment](#virtual-environment)
1. [Tensorflow](#tensorflow)
1. [Monitor GPU Usage](#monitor-gpu-usage)
1. [OpenCv](#opencv)

#Update and Upgrade
Update the list of available versions of applications with update and then 
apply them all with upgrade.
```commandline
sudo apt update
sudo apt upgrade
```

#Google Chrome
Add chrome repository to APT. Create /etc/apt/sources.list.d/google.list and add this line.
```commandline 
deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main
```
	
Get the signing key and install it.
```commandline
wget https://dl.google.com/linux/linux_signing_key.pub
sudo apt-key add linux_signing_key.pub
```

Update and install
```commandline
sudo apt update
sudo apt install google-chrome-stable
```

Run chrome and pin it to tool bar
```commandline
google-chrome-stable
```

Clean up the list files in /etc/apt/sources.list.d.  
Apt update will create a new wont for google-chrome.list.  It has some comments at the front of it.


#Nvidia Graphics Driver
Add the repository to APT
```commandline
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt update
```

Install the driver
* Open Software & Updates with super-a
* Select the Additional Drivers tab
* Select the driver.  In this case 390.25

Notes: 
1. This takes a bit of time for the install.  It is compiling the shim code between the downloaded binary and the current kernal API.
1. If you ever have problems with the graphics after any upgrades, come back and reinstall the driver.   This will recompile it if necessary as a result of the upgrades.
1. This also somehow disables the nouveau drivers.  It isn't blacklisted in /etc/modprobe.d so it me be done in grub.
1. If you install the graphics driver from the runfile, don't let it update the X11/XOrg configuration.  It seems to trash that and it is a pain to get it fixed without copying it from somewhere else.

Install nvidia-prime
```commandline
sudo apt install nvidia-prime
```

Enable Nvidia
```commandline
prime-select nvidia
```

Reboot and set up display(s).

Check that the right driver is running.
```commandline
nvidia-smi
```

```
  +-----------------------------------------------------------------------------+
  | NVIDIA-SMI 390.25                 Driver Version: 390.25                    |
  |-------------------------------+----------------------+----------------------+
  | GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
  | Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
  |===============================+======================+======================|
  |   0  GeForce GTX 1060    Off  | 00000000:01:00.0  On |                  N/A |
  | N/A   61C    P2    23W /  N/A |   1197MiB /  6078MiB |      0%      Default |
  +-------------------------------+----------------------+----------------------+
                                                                               
  +-----------------------------------------------------------------------------+
  | Processes:                                                       GPU Memory |
  |  GPU       PID   Type   Process name                             Usage      |
  |=============================================================================|
  |    0      1085      G   /usr/lib/xorg/Xorg                           668MiB |
  |    0      1883      G   compiz                                       409MiB |
  |    0      2535      G   ...-token=AA7D3026C185E0BA4D241B47E9210727   117MiB |
  +-----------------------------------------------------------------------------+
```

#PyCharm
There is no reason to do this so early in the install.  
It is helpful to have it to edit this document in markdown format.

Download the installer and version you prefer and extract into /opt
```commandline
sudo tar xf <pycharm-download-name> -C /opt/
```

Run and pin to the tool bar.  
```commandline
./opt/<pycharm>/bin/pycharm.sh
```
This will also give you a chance to add charm to the path.

#Nvidia CUDA

Search "nvidia cuda <version>" to find the download page.
Download the runfile (local) version by OS, architecture and OS version.

Run the installer
```commandline
chmod +x cuda_<version>_linux.run
sudo ./cuda_<version>_linux.run
```

Notes:
1. **no** to install the graphics driver.

Check that the correct version of CUDA is installed.

```commandline
cat /usr/local/cuda/version.txt
```

```commandline
CUDA Version 9.<minor version>
```

Add these lines to .bashrc
```commandline
export PATH-/usr/local/cuda-9.0/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-9.0/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
```

Note:
1. If you get the following error when you import Tensorflow it is probably because you are missing these entries in .bashrc.
```commandline
ImportError: libcublas.so.9.0: cannot open shared object file: No such file or directory
```

#Nvidia CUDA Toolkit
Install the toolkit that matches the version of CUDA.  
You won't need to use the CUDA toolkit and compiler for Tensorflow, but you do need some of the libraries.

```commandline
sudo apt install nvidia-cuda-toolkit
```

Check the version.
```commandline
nvcc --version
```

```commandline
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2015 NVIDIA Corporation
Built on Tue_Aug_11_14:27:32_CDT_2015
Cuda compilation tools, release 7.5, V7.5.17
```

#Nvidia CUDA DNN
Register for an Nvidia developer account here: https://developer.nvidia.com/cudnn and download cuDNN.
Get the runtime library for the version of CUDA that was installed.

Get gdebi to install local packages.
```commandline
sudo apt install gdebi-core
```

Install the local cuDNN deb file that downloaded above.
```commandline
sudo gdebi libcudnn<verson>.deb
``` 

Note: 
1. If you get an error like this when you import tensorflow it probably has to do with this install.
```commandline
ImportError: libcudnn.so.7: cannot open shared object file: No such file or directory
```

#Python 3.6
Add the apt repository and install

```commandline
sudo add-apt-repository ppa:jonathonf/python-3.6
sudo apt update
sudo apt install python3.6
```

Check that it was installed and make a note of where it is located.
```commandline
/usr/bin/python3.6
which python3.6
```

#PIP
```commandline
sudo apt install python3-pip
```

Notes:
1. There are two versions of PIP.  PIP which works with Python2 and PIP3 which works with Python3.  If you only install python3-pip then you won't ever have to remember which one to run.

#Virtual Environment
```commandline
sudo apt install virtualenv virtualenvwrapper
mkdir ~/.virtualenvs
```

Export this directory by adding this line to .bashrc
```commandline
export WORKON_HOME=$HOME/.virtualenvs
```

Make sure to source .bashrc or just open a new terminal.

Create the deep learning virtual env with python 3.6.
Make sure you know where the python3.6 is installed.

```commandline
which python3.6

/usr/bin/python3.6

mkvirtualenv --python=/usr/bin/python3.6 dl
```

This should create and activate the new virtual environment.  
Make sure that it is running the right version of python
```commandline
python --verison

Python 3.6.3
```

Check that you can workon and deactivate the virtual env.
```commandline
deactivate
workon dl
```

# Tensorflow
With the dl virtual environment activated.
```commandline
pip install ipython tensorflow tensorflow-gpu
```

Look to see that it is installing the version that started the entire depencency chain at the top of this document.
In this case 1.5.0

Test it all out.  In iPython with the following commands

```commandline
import tensorflow as tf
tf.__version__
```

If this return 1.5.0 then you have gotten it all right.

# Monitor GPU Usage
You can monitor what is going on with the gpu using watch.
```commandline
watch nvidia-smi
```

# OpenCV
If you are going to work with OpenCV.
```commandline
pip install opencv-python opencv-contrib-python
```

You can test it in ipython
```commandline
import cv2
```




