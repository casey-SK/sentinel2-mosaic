import os
import typing
from typing import List
from typing import Tuple

from command_line_args import cli_parser
from band_lister import get_bands
from jp2_to_tif import batch_jp2_to_tif
from helpers import input_validator, trashbin, continue_check
from blend_mosaic import mosaic
from raster_builder import merge_bands, raster_calculator

global output_options
output_options = {'truecolor': ['B04', 'B03', 'B02'],
                  'falsecolor': ['B08', 'B04', 'B03'],
                  'urban': ['B12', 'B11', 'B04'],
                  'swir': ['B12', 'B8A', 'B04'],
                  'ndvi': ['B08', 'B04'],
                  'moisture': ['B8A', 'B11'],
                  'ndwi': ['B03', 'B08'],
                  'ndsi': [''],
                  'B02': ['B02_10m'],
                  'B03': ['B03_10m'],
                  'B04': ['B04_10m'],
                  'B08': ['B08_10m'],
                  'B05': ['B05_20m'],
                  'B06': ['B06_20m'],
                  'B07': ['B07_20m'],
                  'B8A': ['B8A_20m'],
                  'B11': ['B11_20m'],
                  'B12': ['B12_20m'],
                  'B01': ['B01_60m'],
                  'B09': ['B09_60m'],
                  }
