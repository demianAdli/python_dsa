"""
Return the total size of the immediate path.
"""
import os
from pathlib import Path


def disk_usage(path):
    all_files = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            all_files += disk_usage(childpath)

    print('{0:<7}'.format(all_files), path)
    return all_files


if __name__ == "__main__":
    total = disk_usage(Path())
    print()
    print("Total size of the path", Path().absolute(), "is: ")
    print(total/1024, "KB")
