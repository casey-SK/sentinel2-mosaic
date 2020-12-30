from __init__ import *
from globals import *


from helpers import endswith_walk_filter


def get_bands(requests: List[str], path: str) -> List[str]:
    """ Some Docstring """

    tmp_list: List[str] = []  # create a temporary list that will contain duplicates

    for key, value in output_options.items():
        if key in requests:
            tmp_list.extend(value)

    requested_bands: List[str] = []  # create final list and strip out duplicates
    [requested_bands.append(item) for item in tmp_list if item not in requested_bands]

    return requested_bands


def get_files(band_list: List[str], path: str, extension: str) -> List[str]:
    """ Some Docstring """

    file_list: List[str] = []

    for item in band_list:
        file_list.extend(endswith_walk_filter(path, str(item + extension)))

    return file_list


def get_tiles(file_list: List[str]) -> List[str]:
    """ some docstring """

    tmp_list: List[str] = []
    tile_list: List[str] = []

    for item in file_list:
        tmp_list.append(
            str(
                os.path.basename(item).split("_")[0]
                + "_"
                + os.path.basename(item).split("_")[1]
            )
        )

    [tile_list.append(item) for item in tmp_list if item not in tile_list]

    return tile_list


def duplicate_tiles(tile_list: List[str]) -> List[str]:
    duplicates = [
        tile_list[item]
        for item in range(len(tile_list))
        if tile_list[item] in tile_list[:item]
    ][1:]

    if len(duplicates) > 0:
        return duplicates
    else:
        return None
