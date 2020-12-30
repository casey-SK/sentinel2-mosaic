import os
import typing
from typing import List
from typing import Tuple
from typing import Set

from command_line_args import cli_parser
from list_creator import get_bands, get_files, get_tiles, duplicate_tiles
from helpers import (
    continue_check,
    endswith_walk_filter,
    trashbin,
    path_check,
    file_check,
)
