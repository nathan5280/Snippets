Notes on tweaking things in the virtual console so that you can read it on a 4K monitor.

# Tweaking the Font
When you can't figure out how to change the resolution just change the font.

```commandline
sudo dpkg-reconfigure console-setup
```

Choose:
* UTF-8
* Guess optimale character set
* Let the system select a suitable font
* 16x32

If this doesn't take effect then run this command to force it.
```commandline
setupcon
```



