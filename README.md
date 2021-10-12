# gps_coor_filter

Select the coordinates based on thee given longitude abd latitude ranges, ie a "rectangle" on earth surface.


# Attention!!!
# the scripts gps_coor_filter.py and CoordinateSelect.py
# were abandoned in 2021.10.12.
# please use GPS_Coordinate_Select.py

# usage and example

example 1
```
comments, in_rec_dict, out_rec_dict = rec_coor_select(80.0, 100.0, 60.0, 80.0, 0, 1, 2, Ginput_file, Gin_rec_file, Gout_rec_file)
```
example 2
```
comments, in_rec_dict, out_rec_dict = rec_coor_select(80.0, 100.0, 60.0, 80.0, 1, 0, 3, Ginput_file, Gin_rec_file, Gout_rec_file)
```
example 3
```
comments, in_rec_dict, out_rec_dict = rec_coor_select(80.0, 100.0, 60.0, 80.0, 2, 0, 1, Ginput_file, Gin_rec_file, Gout_rec_file)
```

uncomment these example lines in the scripts or write your own command to use this script. 