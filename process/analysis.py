import logging
import sys, os
import getopt as getopt

sys.path.insert(0, "/home/murch/projects/factory_managerPY")
sys.path.insert(1, "/home/murch/projects/ioPY")

#loggerconfig_stream = open("logger.ini", "r")
#log_config = yaml.safe_load(loggerconfig_stream)
#logging.config.dictConfig(log_config)

logger = logging.getLogger(__name__)

def main(argv):
    # Default argvs
    directory = "./"
    viewset = "./views/"
    input = "./input/"
    output = "./output/"
    silent = False

    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["dir=", "view="])
    except getopt.GetoptError:
        print("plotanalyze.py -i <input> -o <output> -v <viewdir> -s <silent>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("test.py -i <inputfile>")
            sys.exit()
        elif opt in ("-i", "--input"):
            input = arg
        elif opt in ("-o", "--output"):
            output = arg
        elif opt in ("-v", "--view"):
            viewset = arg
        elif opt in ("-s", "--silent"):
            silent = True

    logger.info("Apollo")
    logger.info("**********************************")

    logger.debug("args: " + str(argv))




if __name__ == "__main__":
    main(sys.argv[1:])