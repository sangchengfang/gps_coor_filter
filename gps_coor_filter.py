# !/usr/bin/env python3
# used, abandoned in 2021.10.12, please do not use, please use GPS_Coordinate_Select.py

# Select the GPS sites for interseismic coupling calculation
import sys
import os
from CoordinateSelect import rectangle_coor_select

# print(sys.path)

# /home/scf/master/research/scripts/gps_coor_flter
# rectangle_coor_select(70.0, 100.0, 22.5, 32.5, 'pan_gps.txt', 'interseismic_coupling.dat')
# rectangle_coor_select(80.0, 100.0, 60.0, 80.0, 'ex_gps.dat', 'ex_output.dat')
# print(os.path.dirname('/home/scf/master/research/scripts/gps_coor_flter/pan_gps.txt'))
# print(os.path.split(os.path.abspath('/home/scf/master/research/scripts/gps_coor_flter/pan_gps.txt')))
# print(os.path.split(os.path.abspath('pan_gps.txt')))

if len(sys.argv) == 1:
    print('Correct usage: gps_coor_filter.py input_file_name output_file_name')
    sys.exit()
else:
    Ginput_file = sys.argv[1]
    Goutput_file = sys.argv[2]

# check if the file exists
if not os.path.isfile(Ginput_file):
    print("Cannot find input file in your system")
    sys.exit()

file_path = os.path.split(Ginput_file)
# print(file_path)

if not os.path.exists(file_path[0] + '/' + Goutput_file):
    print("Cannot find output file in your system, now create it")
    cmd = 'touch ' + file_path[0] + '/' + Goutput_file
    print(cmd)
    os.system(cmd)

rectangle_coor_select(73.0, 96.0, 25.0, 32.0, 0, 1, 2, Ginput_file, Goutput_file)