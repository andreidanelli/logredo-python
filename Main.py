# Configs data base
from Database     import load
# Import archive log
from CheckLogRedo import checkLogRedo


def main():
   load()
   checkLogRedo()


if __name__ == '__main__':
    load()
    checkLogRedo()