@echo off
title Mo phong Gazebo - Dot 1 Concentric Clasp
echo ========================================================
echo  KHOI DONG GAZEBO 11 MO PHONG KHOP DOT NGON TAY (WSLg)
echo ========================================================
wsl -d Ubuntu-22.04 -- bash -c "export DISPLAY=:0; export WAYLAND_DISPLAY=wayland-0; gazebo /home/nhatv/exo_phalanx1_sim/phalanx1_simulation.world"
pause
