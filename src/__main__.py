import getopt
import sys

from .app import Application

ERROR_MESSAGE = "Type python -m src --help for help"

USSAGE_MESSAGE = "Usage"

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "he:s:", ["help", "env=", "soln="])
    except getopt.GetoptError as err:
        print(err)
        print(ERROR_MESSAGE)
        sys.exit(2)

    env = None
    soln = None

    for o, a in opts:
        if o in ("-h", "--help"):
            print(USSAGE_MESSAGE)
            sys.exit()
        elif o in ("-e", "--env"):
            env = a
        elif o in ("-s", "--soln"):
            soln = a
        else:
            assert False, "unhandeled option"

    Application(env=env, soln=soln)

if __name__ == "__main__":
    main()