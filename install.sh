#!/bin/bash
sudo mkdir /usr/share/icons/knifegtk/
sudo dd if="knifegtk.png" of="/usr/share/icons/knifegtk/knifegtk.png"
sudo dd if="knife.desktop" of="/usr/share/applications/knife.desktop"
sudo dd if="knifegtk.py" of="/usr/bin/knifegtk.py"
sudo chmod +x /usr/bin/knifegtk.py
