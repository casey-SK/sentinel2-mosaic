#!/usr/bin/env python3

""" command line program to build mosiac(s) from Sentinel 2 satellite imagery """

# Authors: Casey McMahon
# Created: November 14, 2020
# Last Modified: December 27, 2020
# License: CC0 [only for code written within, not added librarys]
# Python Version: 3.8.5 [MUST HAVE 3.7+]
# Required Dependencies:
#     - GDAL [verion 3.1.3]
#     - Whitebox [version 1.4]
#     - OSSIM [version ]

from __init__ import *


def main():

    # parse out the cli arguments into a tuple {[requests] , 'path/to/data'}
    provided_args = cli_parser()  #

    # a list of all requested outputs
    requests: Tuple[List[str], str] = provided_args[0]
    # a string pointing to data folder
    path: str = provided_args[1]
    # a list of bands that need to be processed (ex. 'B03_10m)
    band_list: List[str] = get_bands(requests, path)

    # setup a directory path for future functions to utilize
    working_dir = path
    os.chdir(path)

    # check to make sure all files need in next steps are able to be found
    # also tells user how much disk space will be needed to complete program
    input_validator(requests, path, band_list)

    # convert all images to tif and place into new working directory
    # uses GDAL translate
    batch_jp2_to_tif(band_list, working_dir)

    # change working dir
    os.chdir(path)
    working_dir = os.path.join(path, "tmp/converted")

    # histogram match each band using OSSIM,
    # first image in list is used as reference
    hist_match(band_list, working_dir)

    # delete converted images to free up space
    trashbin(working_dir)
    # change working dir
    os.chdir(path)
    working_dir = os.path.join(path, "tmp/hist_matched")

    # mosaic together each band with blending, via OSSIM
    mosaic(band_list, working_dir)

    # delete histogram matched images to free up space
    trashbin(working_dir)
    # change working dir
    os.chdir(path)
    working_dir = os.path.join(path, "tmp/band_mosiacs")

    # create composite mosiac for requests that are combined into r,g,b bands
    # outputs into 'output' folder inside parent path and beside 'tmp' folder
    merge_bands(requests, working_dir)

    # perform raster calculations for requests that are single band outputs
    # outputs into 'output' folder inside parent path and beside 'tmp' folder
    raster_calculator(requests, working_dir)

    # delete band mosaic images to free up space
    trashbin(working_dir)

    # perform final clean up (of tmp folder) and exit


if __name__ == "__main__":
    main()
