from __init__ import *


def continue_check(check: str):
    """From Command prompt, continue or terminate based on input
    instead of a 'No' value, anything that isn't a derivative of 'Yes is considered
    to be a signal to terminate the program.
    """
    if (check == "yes") or (check == "y") or (check == "Y"):
        pass
    else:
        print("\n  Exiting ...")
        quit()


def endswith_walk_filter(path: str, keyword: str) -> List[str]:
    """This function take in a folder path and keyword and looks within the
    folder to find any files that end with the keyword [keyphrase]. All matches
    are then added to a list and returned to the caller
    """
    filter_list = []
    for root, dirs, files in os.walk(path):
        for filename in files:
            if filename.endswith(keyword):
                filter_list.append(os.path.join(root, filename))
    return filter_list


def trashbin(working_dir: str):
    pass


def path_check(path: str):
    """ some docstring """

    # check to ensure provided path exists
    if os.path.isdir(path):
        print("\n  Checking for data folder ... found. \n")
    else:
        print("\n Error: Provided path argument: ", path)
        print(
            "        Could not open directory specified in path argument. Exiting...\n"
        )
        quit()


def file_check(band_list: List[str], file_list: List[str], duplicates: List[str]):
    pass
