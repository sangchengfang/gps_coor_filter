# !/usr/bin/env python3

# Select the coordinates based on thee given longitude abd latitude ranges, ie a "rectangle" on earth surface.

import os
import sys
import copy
from IsNumber import is_number


def rec_coor_select(lon_min, lon_max, lat_min, lat_max, site_col, lon_col, lat_col, filename, in_rec_filename,
                    out_rec_filename):
    """
    the latitude will be converted to colatitude when do filtering,
    the colatitude will be converted back to latitude in the output file
    :param in_rec_filename:
    :param site_col: which column is the site name
    :param lon_col: which column is the longitude
    :param lat_col: which column is the latitude
    :param lon_min: minimum longitude, [0:360]
    :param lon_max: maximum latitude, [-90,90], the colatitude will be used to do the filtering
    :param lat_min: minimum longitude, [0:360]
    :param lat_max: maximum latitude, [-90,90], the colatitude will be used to do the filtering
    :param filename: the file that contains all the gps coordinates, the first column is the site name,
    the second ane the third columns are the longitude and latitude. Use absolute path.
    :param in_rec_filename: the filename of the output file that saves the seclected coordinates
    :param out_rec_filename: the filename of the output file that saves the coordinates outside the selected area
    :return: return a output file named filename_filtered.dat
    """

    # parameters initiation
    lon_min = float(lon_min)
    lon_max = float(lon_max)
    lat_min = float(lat_min)
    lat_max = float(lat_max)
    site_col = int(site_col)
    lon_col = int(lon_col)
    lat_col = int(lat_col)
    filename = str(filename)
    in_rec_filename = str(in_rec_filename)
    out_rec_filename = str(out_rec_filename)

    comments = []
    data_dict = {}
    in_rec_dict = {}
    out_rec_dict = {}

    # col_index = []
    # info_col = [site_col, lon_col, lat_col]

    with open(filename, 'r') as all_coor:
        for line in all_coor.readlines():
            # print(line)
            # print(line[0])
            data = line.split()
            # print(data)

            if data[0] == '#':
                comments.append(line)
                # print(comments)
                # ignore all the comment lines
            else:
                if not (isinstance(data[site_col], str) and is_number(data[lon_col]) and is_number(data[lat_col])):
                    # verify the input data types.
                    print('wrong format, the input should be site_name(str) longitude(float) and latitude(float)')
                else:
                    data_copy = copy.copy(data)
                    data_copy.pop(site_col)
                    data_dict[data[site_col]] = data_copy
                    # if len(data) != col_index:
                    #     col_index = list(range(0, len(data)))

        # print(col_index)
        # print(data_dict)
        # other_col = [index for index in col_index if index not in info_col]
        # print(other_col)
        # print(lon_col)
        # print(lat_col)
        # print(lat_col)
        # for key, value in data_dict.items():
        if site_col > lon_col and site_col > lat_col:
            pass
            # print(str(lon_col) + '1')
            # print(str(lat_col) + '1')
        elif lon_col < site_col < lat_col:
            lat_col = lat_col - 1
            # print(str(lon_col) + '2')
            # print(str(lat_col) + '2')
        elif lat_col < site_col < lon_col:
            lon_col = lon_col - 1
            # print(str(lon_col) + '3')
            # print(str(lat_col) + '3')
        elif site_col < lon_col and site_col < lat_col:
            lat_col = lat_col - 1
            lon_col = lon_col - 1
            # print(str(lon_col) + '4')
            # print(str(lat_col) + '4')

        for key, value in data_dict.items():
            # print(value[lon_col])
            # print(value[lat_col])
            if lon_min < float(value[lon_col]) < lon_max and 90 - lat_max < 90 - float(value[lat_col]) < 90 - lat_min:
                in_rec_dict[key] = value
            else:
                out_rec_dict[key] = value

        # print(in_rec_dict)
        # print(out_rec_dict)
        return comments, in_rec_dict, out_rec_dict


# main()
def main():
    if len(sys.argv) <= 2:
        print('Correct usage: gps_coor_filter.py input_file_name output_file_name')
        sys.exit()
    else:
        Ginput_file = sys.argv[1]
        Gin_rec_file = sys.argv[2]
        Gout_rec_file = sys.argv[3]

    # check if the file exists
    if not os.path.isfile(Ginput_file):
        print("Cannot find input file in your system")
        sys.exit()

    file_path = os.path.split(Ginput_file)
    # print(file_path)
    for item in [Gin_rec_file, Gout_rec_file]:
        if not os.path.exists(file_path[0] + '/' + item):
            print("Cannot find output file in your system, now create it")
            cmd = 'touch ' + file_path[0] + '/' + item
            print(cmd)
            os.system(cmd)

    # example 1
    # comments, in_rec_dict, out_rec_dict = rec_coor_select(80.0, 100.0, 60.0, 80.0, 0, 1, 2, Ginput_file,
    #                                                       Gin_rec_file, Gout_rec_file)
    # example 2
    # comments, in_rec_dict, out_rec_dict = rec_coor_select(80.0, 100.0, 60.0, 80.0, 1, 0, 3, Ginput_file,
    #                                                       Gin_rec_file, Gout_rec_file)
    # example 3
    # comments, in_rec_dict, out_rec_dict = rec_coor_select(80.0, 100.0, 60.0, 80.0, 2, 0, 1, Ginput_file,
    #                                                       Gin_rec_file, Gout_rec_file)

    file_path = os.path.split(os.path.abspath(Ginput_file))
    # print(file_path)
    with open(file_path[0] + '/' + Gin_rec_file, 'w') as fop:
        for comment in comments:
            fop.write(comment)

        for key, value in in_rec_dict.items():
            fop.write(key.ljust(8))
            for i in range(len(value)):
                fop.write(value[i].ljust(8))
            fop.write('\n')

    with open(file_path[0] + '/' + Gout_rec_file, 'w') as fop:
        for comment in comments:
            fop.write(comment)

        for key, value in out_rec_dict.items():
            fop.write(key.ljust(8))
            for i in range(len(value)):
                fop.write(value[i].ljust(8))
            fop.write('\n')


if __name__ == "__main__":
    main()
