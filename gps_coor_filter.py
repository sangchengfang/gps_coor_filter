# !/usr/bin/env python3

# Select the GPS sites for interseismic coupling calculation

from CoordinateSelect import rectangle_coor_select

# print(sys.path)

# /home/scf/master/research/scripts/gps_coor_flter
# rectangle_coor_select(70.0, 100.0, 22.5, 32.5, 'pan_gps.txt', 'interseismic_coupling.dat')
rectangle_coor_select(80.0, 100.0, 60.0, 80.0, 'ex_gps.dat', 'ex_output.dat')
# print(os.path.dirname('/home/scf/master/research/scripts/gps_coor_flter/pan_gps.txt'))
# print(os.path.split(os.path.abspath('/home/scf/master/research/scripts/gps_coor_flter/pan_gps.txt')))
# print(os.path.split(os.path.abspath('pan_gps.txt')))


if 1 == 0:
    pass
    # def rec_cor_filter(lon_min, lon_max, lat_min, lat_max, filename):
    #     """
    #     the latitude will be converted to colatitude when do filtering,
    #     the colatitude will be converted back to latitude in the output file
    #     :param lon_min: minimum longitude, [0:360]
    #     :param lon_max: maximum latitude, [-90,90], the colatitude will be used to do the filtering
    #     :param lat_min: minimum longitude, [0:360]
    #     :param lat_max: maximum latitude, [-90,90], the colatitude will be used to do the filtering
    #     :param filename: the file that contains all the gps coordinates, the first column is the site name,
    #     the second ane the third columns are the longitude and latitude. Use absolute path.
    #     :return: return a output file named filename_filtered.dat
    #     """
    #
    #     filename = str(filename)
    #     lon_min = float(lon_min)
    #     lon_max = float(lon_max)
    #     lat_min = float(lat_min)
    #     lat_max = float(lat_max)
    #     out_site = []
    #     out_lon = []
    #     out_lat = []
    #
    #     with open(filename, 'r') as all_coor:
    #         for line in all_coor.readlines():
    #             # print(line)
    #             data = line.split()
    #             if data[0] != '#':
    #                 # print(data[1])
    #                 # print(data[2])
    #                 # print(data[3])
    #                 # print(is_number(data[0]))
    #                 # print(is_number(data[1]))
    #                 # print(is_number(data[2]))
    #                 if isinstance(data[0], str) and is_number(data[1]) and is_number(data[2]):
    #                     pass
    #                 else:
    #                     print('wrong input data, the correct input should be site_name(str),'
    #                           'longitude(float) and latitude(float)')
    #                 # print(data[0:3])
    #                 if lon_min < float(data[1]) < lon_max and 90 - lat_max < 90 - float(data[2]) < 90 - lat_min:
    #                     out_site.append(data[0])
    #                     out_lon.append(data[1])
    #                     out_lat.append(data[2])
    #                     # print(os.path.dirname(filename))
    #                     # print(os.path.abspath(filename))
    #                 file_path = os.path.split(os.path.abspath('pan_gps.txt'))
    #                 # print(file_path[0])
    #                 with open(file_path[0] + '/filtered_coor.dat', 'w') as fop:
    #                     for i in range(len(out_site)):
    #                         fop.write(out_site[i] + ' ' + out_lon[i] + ' ' + out_lat[i] + '\n')

