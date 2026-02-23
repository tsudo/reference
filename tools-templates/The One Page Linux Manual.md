---
title: "The One Page Linux Manual"
organization: "multiple"
content_type: tool-template
year: 2010
tags: ["linux;cheatsheet;command-reference"]
source_url: ""
license: "© multiple. Reproduced for research and educational purposes per 17 U.S.C. § 107 (fair use)."
date_ingested: 2026-02-22
original_format: pdf
---

THE ONE    PAGE LINUX MANUAL

A summary of useful Linux commands

Version 3.0

May 1999

squadron@powerup.com.au

Starting & Stopping

shutdown -h now

halt

shutdown -r 5

shutdown -r now
reboot

Shutdown the system now and do not
reboot

Stop all processes - same as above

Shutdown the system in 5 minutes and
reboot

Shutdown the system now and reboot

Stop all processes and then reboot - same
as above

startx

Start the X system

Accessing & mounting file systems

mount -t iso9660 /dev/cdrom
/mnt/cdrom

mount -t msdos /dev/hdd
/mnt/ddrive

mount -t vfat /dev/hda1
/mnt/cdrive

Mount the device cdrom
and call it cdrom under the
/mnt directory

Mount hard disk “d” as a
msdos file system and call
it ddrive under the /mnt
directory

Mount hard disk “a” as a
VFAT file system and call it
cdrive under the /mnt
directory

umount /mnt/cdrom

Unmount the cdrom

Finding files and text within files

find / -name  fname

find / -name ”*fname*”

locate missingfilename

updatedb

which missingfilename

grep textstringtofind
/dir

Starting with the root directory, look
for the file called fname

Starting with the root directory, look
for the file containing the string fname

Find a file called missingfilename
using the locate command - this
assumes you have already used the
command updatedb (see next)

Create or update the database of files
on all file systems attached to the linux
root directory

Show the subdirectory containing the
executable file  called missingfilename

Starting with the directory called dir ,
look for and list all files containing
textstringtofind

rm name

rm -rf name

cp filename
/home/dirname

Remove a file or directory called
name

Kill off an entire directory and all it’s
includes files and subdirectories

Copy the file called filename to the
/home/dirname directory

mv filename
/home/dirname

Move the file called filename to the
/home/dirname directory

cat filetoview

man -k keyword

more filetoview

head filetoview

head -20 filetoview

tail filetoview

tail -20 filetoview

Display the file called filetoview

Display man pages containing
keyword

Display the file called filetoview one
page at a time, proceed to next page
using the spacebar

Display the first 10 lines of the file
called filetoview

Display the first 20 lines of the file
called filetoview

Display the last 10 lines of the file
called filetoview

Display the last 20 lines of the file
called filetoview

Installing software for Linux

rpm -ihv name.rpm

rpm -Uhv name.rpm

rpm -e package

rpm -l package

rpm -ql package

rpm -i --force package

tar -zxvf archive.tar.gz or
tar -zxvf archive.tgz

./configure

Install the rpm package called name

Upgrade the rpm package called
name

Delete the rpm package called
package

List the files in the package called
package

List the files and state the installed
version of the package called
package

Reinstall the rpm package called
name having deleted parts of it (not
deleting using rpm -e)

Decompress the files contained in
the zipped and tarred archive called
archive

Execute the script preparing the
installed files for compiling

The X Window System

User Administration

xvidtune

XF86Setup

Xconfigurator

Run the X graphics tuning utility

Run the X configuration menu with
automatic probing of graphics cards

Run another X configuration menu with
automatic probing of graphics cards

xf86config

Run a text based X configuration menu

adduser accountname

Create a new user call accountname

passwd accountname

Give accountname a new password

su

exit

Log in as superuser from current login

Stop being superuser and revert to
normal user

Moving, copying, deleting & viewing files

Little known tips and tricks

ls -l

ls -F

ls -laC

List files in current directory using
long format

List files in current directory and
indicate the file type

List all files in current directory in
long format and display in columns

ifconfig

List ip addresses for all devices on
the machine

apropos subject

List manual pages for subject

usermount

Executes graphical application for
mounting and unmounting file
systems

/sbin/e2fsck hda5

Execute the filesystem check utility
on partition hda5

File permissions

fdformat /dev/fd0H1440

Format the floppy disk in device fd0

tar -cMf /dev/fd0

tail -f /var/log/messages

cat /var/log/dmesg

*

?

[xyz]

linux single

ps

kill 123

Backup the contents of the current
directory and subdirectories to
multiple floppy disks

Display the last 10 lines of the system
log.

Display the file containing the boot
time messages - useful for locating
problems. Alternatively, use the
dmesg command.

wildcard - represents everything. eg.

cp from/* to  will copy all files in the
from directory to the to directory

Single character wildcard. eg.

cp config.? /configs will copy all files
beginning with the name config. in
the current directory to the directory
named configs.

Choice of character wildcards. eg.

ls [xyz]* will list all files in the current
directory starting with the letter x, y,
or z.

At the lilo prompt, start in single user
mode. This is useful if you have
forgotten your password. Boot in
single user mode, then run the
passwd command.

List current processes

Kill a specific process eg. kill 123

If the command ls -l is given, a long list of file names is
displayed. The first column in this list details the permissions
applying to the file. If a permission is missing for a owner,
group of other, it is represented by - eg.  drwxr-x—x
Read = 4

File permissions are altered by giving the
chmod command and the appropriate
octal code for each user type. eg

Write = 2

Execute = 1

chmod 7 5 5

chmod +x filename

chmod 7 6 4 filename will make the file
called filename R+W+X for the owner,
R+W for the group and R for others.

Full permission for the owner, read and
execute access for the group and others.

Make the file called filename executable
to all users.

Configuration files and what they do

X Shortcuts - (mainly for Redhat)

/etc/profile

/etc/fstab

/etc/motd

etc/rc.d/rc.local

System wide environment variables for
all users.

List of devices and their associated mount
points. Edit this file to add cdroms, DOS
partitions and floppy drives at startup.

Message of the day broadcast to all users
at login.

Bash script that is executed at the end of
login process. Similar to autoexec.bat in
DOS.

/etc/HOSTNAME

Conatins full hostname including domain.

/etc/cron.*

/etc/hosts

There are 4 directories that automatically
execute all scripts within the directory at
intervals of hour, day, week or month.

A list of all know host names and IP
addresses on the machine.

/etc/httpd/conf

Paramters for the Apache web server

/etc/inittab

Specifies the run level that the machine
should boot into.

/etc/resolv.conf

Defines IP addresses of DNS servers.

/etc/smb.conf

~/.Xdefaults

/etc/X11/XF86Confi
g

~/.xinitrc

Config file for the SAMBA server. Allows
file and print sharing with Microsoft
clients.

Define configuration for some X-
applications. ~ refers to user’s home
directory.

Config file for X-Windows.

Defines the windows manager loaded by
X. ~ refers to user’s home directory.

Control|Alt  + or -

Alt | escape

Shift|Control F8

Right click on desktop
background

Shift|Control Altr

Shift|Control Altx

Printing

Increase or decrease the screen
resolution. eg. from 640x480 to
800x600

Display list of active windows

Resize the selected window

Display menu

Refresh the screen

Start an xterm session

/etc/rc.d/init.d/lpd start

Start the print daemon

/etc/rc.d/init.d/lpd stop

Stop the print daemon

/etc/rc.d/init.d/lpd
status

Display status of the print daemon

lpq

lprm

lpr

lpc

Display jobs in print queue

Remove jobs from queue

Print a file

Printer control tool

man subject | lpr

man -t subject | lpr

Print the manual page called subject
as plain text

Print the manual page called subject
as Postscript output

printtool

Start X printer setup interface

Get your own Official Linux Pocket Protector - includes
handy command summary. Visit:
www.powerup.com.au/~squadron

