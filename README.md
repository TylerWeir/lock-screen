# lock-screen
Creates a blurred screenshot of your desktop for use as a i3lock image.

### Usage
Paste this command into your i3 config file:

`bindsym Control+$mod+l exec "python [PATH TO lock-screen.py] $HOME/Pictures/lock.png ; i3lock -u --image $HOME/Pictures/lock.png"`

