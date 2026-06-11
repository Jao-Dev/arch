#!/bin/bash

#essenciais
pacman -S xdg-desktop-portal xdg-desktop-portal-hyprland hyprland hyprpaper
pacman -S gst-libav gst-plugins-bad gst-plugins-good gst-plugins-ugly gst-plugin-pipewire
pacman -S xorg-server xorg-server-common xorg-xwayland xorg-xinit
pacman -S ttf-0xproto-nerd ttf-dejavu ttf-liberation
pacman -S wiremix ufw udisks2 udiskie networkmanager power-profiles-daemon ffmpeg btop

#Não tenho certeza se já vem instalado
pacman -S bluez bluez-utils man-db

#
pacman -S slurp kitty bluetui vlc vlc-plugins-all pix grim neovim nwg-look flatpak mpv waybar speedtest-cli rofi localsend qutebrowser evince fastfetch
pacman -S 7zip zip unzip unrar
pacman -S gsettings-qt6 gsettings-qt5 cliphist wl-clipboard polkit-kde-agent

pacman -S --needed git base-devel

#####
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si

yay -Y --gendb
yay -Sy brave-origin-bin
