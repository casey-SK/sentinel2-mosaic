import typing
from typing import List


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


def trashbin():
    pass


def input_validator():
    pass
