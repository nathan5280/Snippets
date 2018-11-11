Notes on tweaking things in the virtual console so that you can read it on a 4K monitor.

# Tweaking the Font
When you can't figure out how to change the resolution just change the font.

```commandline
sudo dpkg-reconfigure console-setup
```

Choose:
* UTF-8
* Guess optimal character set
* Let the system select a suitable font
* 16x32

If this doesn't take effect then run this command to force it.
```commandline
setupcon
```
# Virtual Console (18.04)
Don't use ctrl+alt+F1 as this is now connected to X11

Access Virtual Console:
- ctrl+alt+F[2-6]

Return to X11:
- ctrl+alt+F1


