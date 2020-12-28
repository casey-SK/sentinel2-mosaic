# sentinel2-mosaic tool
*A command line program to build mosiac(s) from Sentinel 2
satellite imagery, using various band options.*

## Usage
Once installed, you can call the tool using the following
command line arguments:

```
>> sentinel2-mosiac [options] [/path/to/parent/data/folder]
```
where ``` [options] ``` can be any of the following:

| Command    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Description |
| --------------- | ---------------------------------------------------------------------------------------------- |
| -h, --help      | Prints help information.                                                                       |
| -truecolor      | create a true color image. Based on bands 4,3,2 for r,g,b                                      |
| -falsecolor     | create a false color image. Based on bands 8,4,3 for r,g,b                                     |
| -urban          | create a false color (urban) image. Based on bands 12,11,4 for r,g,b                           |
| -swir           | create a short-wave infrared (SWIR) image. Based on bands 12,8A,4 for r,g,b                    |
| -nvdi           | create a normalized difference vegetation index (NVDI) image. Based on bands (B8-B4) / (B8+B4) |
| -moisture       | create a moisture index image. Based on bands (B8A-B11) / (B8A+B11)                            |
| -ndwi           | create a normalized difference water index (NDWI) image. Based on bands (B3-B8) / (B3+B8)      |
| -ndsi           | create a normalized difference snow index (NDSI) image. Based on bands (B3-B11) / (B3+B11)     |
| -greyscale      | create a singleband greyscale image [B02, B03, B04, B05, B06, B07, B0', B08A, B09, B11, B12]   |
| --version       | Prints the version information.                                                                |

## How it Works

This tool uses [*GDAL_Translate*](https://gdal.org/programs/gdal_translate.html) to convert the intial .jp2 image
files into .tif files so that they are easier to work with.

Next, each band of imagery is histogram matched using the _____
tool. The histograms are matched to the first image in a list,
which is generally alphabetical, although not guranteed to be.

Then a mosaic is created using _____ for each band needed, using the
histogram-matched images.

Depending on the options requested, some raster calculations
may be performed at this step, or the bands are combined into
an *rgb* image and returned as output *beside* the parent
directory.

## Installation

This project is deployed as a .appimage executable. On windows,
you may be able to use Windows Subsystem for Linux (WSL) to run
this program.

To run the .appimage file, _____

## Expected Data Folder Structure

To use this tool, you should download data from the [*copernicus scihub*](https://scihub.copernicus.eu/).
