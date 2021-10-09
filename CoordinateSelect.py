# !/usr/bin/env python3

# Select the coordinates based on thee given longitude abd latitude ranges, ie a "rectangle" on earth surface.

import os
import sys
from IsNumber import is_number


def rectangle_coor_select(lon_min, lon_max, lat_min, lat_max, filename, out_filename):
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

    with open(filename, 'r') as all_coor:
        for line in all_coor.readlines():
            # print(line)
            data = line.split()
            if data[0] != '#': # ignore all the comment lines
                if isinstance(data[0], str) and is_number(data[1]) and is_number(data[2]):
                    # verify the data type, the site name should be string and logitude and latitude should be float
                    pass
                else:
                    print('wrong input, the correct input should be site_name(str) longitude(float) and latitude(float)')
                if lon_min < float(data[1]) < lon_max and 90 - lat_max < 90 - float(data[2]) < 90 - lat_min:
                    out_site.append(data[0]) # save all selected site names
                    out_lon.append(data[1]) # save all selected logitude
                    out_lat.append(data[2]) # ave all selected latitude
                file_path = os.path.split(os.path.abspath(filename))
                # print(file_path)
                with open(file_path[0] + '/' + out_filename, 'w') as fop:
                    for i in range(len(out_site)):
                        fop.write(out_site[i] + ' ' + out_lon[i] + ' ' + out_lat[i] + '\n')

def main():
    pass

# main()


if __name__ == "__main__":
    main()