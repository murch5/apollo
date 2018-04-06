import logging
import logging.config
import sys, os
import getopt as getopt
import yaml
import xml.etree.ElementTree as et

sys.path.insert(0, "/home/murch/projects/factory_managerPY")
sys.path.insert(1, "/home/murch/projects/hermes")
sys.path.insert(3, "/home/murch/projects/apollo")
sys.path.insert(2, "/home/murch/projects/athena")

import data_manager as dm
import process as process

loggerconfig_stream = open("logger.ini", "r")
log_config = yaml.safe_load(loggerconfig_stream)
logging.config.dictConfig(log_config)

logger = logging.getLogger(__name__)

def main(argv):
    # Default argvs
    directory = "./"
    viewset = "./views/"
    input = ["/media/murch/DATA/project/ARPC1B/Mx_track_analysis/fish5.tif"]
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

    logger.info("apollo - Analyze Data")
    logger.info("........................................")
    logger.info("............../ssss\......................")
    logger.info("............./sSSSSs\.....APOLLO..........")
    logger.info(".............\sSSSSs/.....................")
    logger.info("..............\ssss/......v0.0.0..........")
    logger.info("........................................")

    logger.debug("args: " + str(argv))

    data = dm.DataCollection()

    process_stack = process.ProcessManager(process)

    xml_temp = et.parse("/media/murch/DATA/project/ARPC1B/Mx_track_analysis/ARPC1B_Mx.xml")

    data.load_data(xml_temp,input)

    process_stack.populate_from_xml(xml_temp.find(".//processing"))

    data_dict = data.get_data_dict()

    data_final = process_stack.pass_thru_stack(data.data_handler.get_obj_list()[0].get("data"))

    print(data_final)

if __name__ == "__main__":
    main(sys.argv[1:])