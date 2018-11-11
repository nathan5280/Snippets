# FastAI setup on NVidia GTX 1060

See the https://github.com/nathan5280/Snippets/blob/master/linux/deep-learning.md for setting up Nvidia driver, cuda, cudnn

On Ubuntu 18.04 pipenv breaks pip3.  pip3 paths can be recovered with:
```commandline
sudo python3 -m pip uninstall pip && sudo apt install python3-pip --reinstall
```
## FastAI Notebooks
Clone the FastAI repository with all the notebooks.
```commandline
git clone https://github.com/fastai/fastai.git
```

## Install Packages
```commandline
pipenv --python 3.6

pipenv install jupyter ipython
pipenv install torch
pipenv install torchvision
pipenv install fastai
pipenv install matplotlib pandas
pipenv install bcolz graphviz 
pipenv install sklearn sklearn_pandas
pipenv install opencv-python
