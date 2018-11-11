# Fix suspend when lid closes and restores

Edit /etc/default/grub
- backup: /etc/default/grub
- edit: GRUB_CMDLINE_LINUX_DEFAULT="quiet splash button.lid_init_state=open"
- rebuild grub: grub-mkconfig -o /boot/grub/grub.cfg .
