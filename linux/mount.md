# Mounting Drives on Boot
```commandline
sudo vim /etc/fstab

# /etc/fstab: static file system information.
#
# Use 'blkid' to print the universally unique identifier for a
# device; this may be used with UUID= as a more robust way to name devices
# that works even if disks are added and removed. See fstab(5).
#
# <file system> <mount point>   <type>  <options>       <dump>  <pass>
# / was on /dev/nvme0n1p6 during installation
UUID=3aa8c7f3-f8ca-4d68-8747-ef164c58a0db /               ext4    errors=remount-ro 0       1
# /boot/efi was on /dev/nvme0n1p2 during installation
UUID=28DD-B2DC  /boot/efi       vfat    umask=0077      0       1
# /tmp was on /dev/nvme0n1p9 during installation
UUID=c83a79dd-637b-4912-a1b3-157a7132b3d4 /tmp            ext4    defaults        0       2
# /var was on /dev/nvme0n1p10 during installation
UUID=8dfc7965-2e68-4001-af3e-13562548febf /var            ext4    defaults        0       2
# swap was on /dev/nvme0n1p7 during installation
UUID=2b812a2d-796e-4285-b815-046960063665 none            swap    sw              0       0
# projects
UUID=72c62460-b2bd-4725-a860-10fa1de163c1 /home/nathan/projects ext4 defaults 0 	0
# data
UUID=1d430361-0599-4641-a156-66b66bde7a49 /home/nathan/data ext4 defaults 0	0
```

List UUID for block devices
```commandline
sudo blkid -o full -s PARTLABEL -s UUID

/dev/nvme0n1p1: UUID="FAAADBD1AADB8891" PARTLABEL="Basic data partition"
/dev/nvme0n1p2: UUID="28DD-B2DC" PARTLABEL="EFI system partition"
/dev/nvme0n1p4: UUID="A220BA1320B9EE83" PARTLABEL="Basic data partition"
/dev/nvme0n1p5: UUID="8C16C50E16C4F9EA"
/dev/nvme0n1p6: UUID="3aa8c7f3-f8ca-4d68-8747-ef164c58a0db"
/dev/nvme0n1p7: UUID="2b812a2d-796e-4285-b815-046960063665" PARTLABEL="swap"
/dev/nvme0n1p8: UUID="72c62460-b2bd-4725-a860-10fa1de163c1" PARTLABEL="projects"
/dev/nvme0n1p9: UUID="c83a79dd-637b-4912-a1b3-157a7132b3d4" PARTLABEL="tmp"
/dev/nvme0n1p10: UUID="8dfc7965-2e68-4001-af3e-13562548febf" PARTLABEL="var"
/dev/nvme0n1p11: UUID="1d430361-0599-4641-a156-66b66bde7a49" PARTLABEL="data"
/dev/nvme0n1p3: PARTLABEL="Microsoft reserved partition"
```

XPS
EFI: p1
? : p2
16.04: p3
tmp: p5
var: p6
home: p7
projects: p8
data: p9
swap: p4

nathan-admin
