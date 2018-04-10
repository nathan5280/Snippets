# Remove Libre Office

```commandline
sudo apt-get remove --purge libreoffice*
sudo apt-get clean
sudo apt-get autoremove
```

# Install OpenOffice
Download package for linux 64-bit (DEB)

```commandline
https://www.openoffice.org/download/index.html

tar -xf <Apache...>
cd en-US/DEBS


sudo dpkg -i *.deb    
cd desktop-integration    
sudo dpkg -i *.deb
```

Application is located at:
```commandline
/opt/openoffice4/program/soffice
```

Start it and pin it to the launch bar.