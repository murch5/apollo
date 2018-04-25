import sys, os
import xml.etree.ElementTree as et


sys.path.insert(0, "/home/murch/projects/hermes")
sys.path.insert(2, "/home/murch/projects/athena")
sys.path.insert(1, "/home/murch/projects/factory_managerPY")

import cmd_interface as cmd_interface
import process
import data_manager as dm
import io_util



def radiate(**kwargs):

    data = dm.DataCollection()

    process_stack = process.ProcessManager(process)

    input = kwargs.get("input")

    if input is None:
        input = "stdin"

    if len(input) == 1:
        input = input[0]

    process_xml = kwargs.get("process_xml")

    data.load_data(input)

    process_stack.populate_from_xml(et.parse(process_xml).find("processing"))

    data_dict = data.get_data_dict()

    data_final = process_stack.pass_thru_stack(data.data_handler.get_obj_list()[0].get("data"))

    io_util.file_util.send_data_to_stdout(data_final)

    pass


forge_interface = cmd_interface.CmdInterface(radiate, os.path.split(__file__)[0] + "/settings_radiate.yml")


if __name__ == "__main__":
    forge_interface.run(sys.argv[1:])