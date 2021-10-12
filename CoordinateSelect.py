# !/usr/bin/env python3
# used, abandoned in 2021.10.12, please do not use, please use GPS_Coordinate_Select.py
# Select the coordinates based on thee given longitude abd latitude ranges, ie a "rectangle" on earth surface.

import os
import sys
from IsNumber import is_number

def rectangle_coor_select(lon_min, lon_max, lat_min, lat_max, site_col, lon_col, lat_col, filename, out_filename):
    """
    the latitude will be converted to colatitude when do filtering,
    the colatitude will be converted back to latitude in the output file
    :param lon_min: minimum longitude, [0:360]
    :param lon_max: maximum latitude, [-90,90], the colatitude will be used to do the filtering
    :param lat_min: minimum longitude, [0:360]
    :param lat_max: maximum latitude, [-90,90], the colatitude will be used to do the filtering
    :param filename: the file that contains all the gps coordinates, the first column is the site name,
    the second ane the third columns are the longitude and latitude. Use absolute path.
    :param out_filename: the filename of the output file that saves the seclected coordinates 
    :return: return a output file named filename_filtered.dat
    """

    lon_min = float(lon_min)
    lon_max = float(lon_max)
    lat_min = float(lat_min)
    lat_max = float(lat_max)
    filename = str(filename)
    out_filename = str(out_filename)
    out_site = []
    out_lon = []
    out_lat = []
    out_other = []
    del_site = []
    del_lon = []
    del_lat = []
    del_other = []

    with open(filename, 'r') as all_coor:
        for line in all_coor.readlines():
            # print(line)
            data = line.split()
            if data[0] != '#': # ignore all the comment lines
                if isinstance(data[site_col], str) and is_number(data[lon_col]) and is_number(data[lat_col]):
                    # verify the data type, the site name should be string and logitude and latitude should be float
                    pass
                else:
                    print('wrong input, the correct input should be site_name(str) longitude(float) and latitude(float)')
                if lon_min < float(data[lon_col]) < lon_max and 90 - lat_max < 90 - float(data[lat_col]) < 90 - lat_min:
                    out_site.append(data[site_col])
                    # save all selected site names
                    out_lon.append(data[lon_col])
                    # save all selected longitude
                    out_lat.append(data[lat_col])
                    # ave all selected latitude
                    # print((data[max(site_col, lon_col, lat_col)+1:]))
                    out_other.append(data[max(site_col, lon_col, lat_col)+1:])
                else:
                    del_site.append(data[site_col])
                    del_lon.append(data[lon_col])
                    del_lat.append(data[lat_col])
                    # print((data[max(site_col, lon_col, lat_col) + 1:]))
                    del_other.append(data[max(site_col, lon_col, lat_col)+1:])

                file_path = os.path.split(os.path.abspath(filename))
                # print(file_path)
                with open(file_path[0] + '/' + out_filename, 'w') as fop:
                    for i in range(len(out_site)):
                        fop.write(out_site[i] + 6*' ' + out_lon[i] + 6*' ' + out_lat[i] + 6*' ' + (8*' ').join(out_other[i]) + '\n')
                        # for j in range(len(out_other[i])):
                        #     print(out_other[i][j])
                        #     print(j)
                        #     fop.write(out_site[i][j])

                with open(file_path[0] + '/' + 'out_rec_' + out_filename, 'w') as fop:
                    for i in range(len(del_site)):
                        fop.write(del_site[i] + 6*' ' + del_lon[i] + 6*' ' + del_lat[i] + 6*' ' + (8*' ').join(del_other[i]) + '\n')


# main()
def main():
    sys.exit()
    # rectangle_coor_select(80.0, 100.0, 60.0, 80.0, 'ex_gps.dat', 'ex_output.dat')
    # rectangle_coor_select(80.0, 100.0, 60.0, 80.0, '../pan_gps.txt', 'int_coupling.dat')


if __name__ == "__main__":
    main()