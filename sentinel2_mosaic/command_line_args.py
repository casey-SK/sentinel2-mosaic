import argparse
from __init__ import *


def cli_parser() -> Tuple[List[str], str]:
    parser = argparse.ArgumentParser(
        prog="sentinel2-mosaic",
        description="A command line program to build a mosiac from Sentinel 2 satellite imagery. \
    program will output a truecolor mosaic if no other arguments are provided",
    )

    parser.add_argument(
        "-truecolor",
        action="store_const",
        const=True,
        default=False,
        dest="truecolor",
        help="create a true color image. Based on bands 4,3,2 for r,g,b",
    )

    parser.add_argument(
        "-falsecolor",
        action="store_const",
        const=True,
        default=False,
        dest="falsecolor",
        help="create a false color image. Based on bands 8,4,3 for r,g,b",
    )

    parser.add_argument(
        "-urban",
        action="store_const",
        const=True,
        default=False,
        dest="urban",
        help="create a false color (urban) image. Based on bands 12,11,4 for r,g,b",
    )

    parser.add_argument(
        "-swir",
        action="store_const",
        const=True,
        default=False,
        dest="swir",
        help="create a short-wave infrared (SWIR) image. Based on bands 12,8A,4 for r,g,b",
    )

    parser.add_argument(
        "-ndvi",
        action="store_const",
        const=True,
        default=False,
        dest="ndvi",
        help="create a normalized difference vegetation index (NDVI) image. Based on bands (B8-B4) / (B8+B4)",
    )

    parser.add_argument(
        "-moisture",
        action="store_const",
        const=True,
        default=False,
        dest="moisture",
        help="create a moisture index image. Based on bands (B8A-B11) / (B8A+B11)",
    )

    parser.add_argument(
        "-ndwi",
        action="store_const",
        const=True,
        default=False,
        dest="ndwi",
        help="create a normalized difference water index (NDWI) image. Based on bands (B3-B8) / (B3+B8)",
    )

    parser.add_argument(
        "-ndsi",
        action="store_const",
        const=True,
        default=False,
        dest="ndsi",
        help="create a normalized difference snow index (NDSI) image. Based on bands (B3-B11) / (B3+B11)",
    )

    available_bands = [
        "B02",
        "B03",
        "B04",
        "B05",
        "B06",
        "B07",
        "B08",
        "B8A",
        "B09",
        "B11",
        "B12",
    ]

    parser.add_argument(
        "-greyscale",
        choices=available_bands,
        default=False,
        dest="greyscale",
        help="create a single band greyscale image from the choosen band(s)",
    )

    parser.add_argument(
        "path",
        metavar="path",
        type=str,
        nargs=1,
        help="path to parent folder containing all unzipped tile image folders from copernicus scihub",
    )

    args = parser.parse_args()

    requests = []

    requests += ["truecolor"] if args.truecolor is True else []
    requests += ["falsecolor"] if args.falsecolor is True else []
    requests += ["urban"] if args.urban is True else []
    requests += ["swir"] if args.swir is True else []
    requests += ["ndvi"] if args.ndvi is True else []
    requests += ["moisture"] if args.moisture is True else []
    requests += ["ndwi"] if args.ndwi is True else []
    requests += ["ndsi"] if args.ndsi is True else []
    requests += [args.greyscale] if bool(args.greyscale) is True else []

    if not requests:
        print(
            "\n  CAUTION: No optional arguments provided, program will default to true color image mosaic..."
        )

        continue_prompt = input("\n  Do you wish to continue? [y/N] : ")
        continue_check(continue_prompt)

    else:
        pass

    path = "".join(args.path)  # Debugging
    print(path)

    print(output_options)
    return requests, path
