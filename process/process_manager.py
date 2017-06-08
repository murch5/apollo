import inspect
import process

import factory_manager as fm

class ProcessManager(fm.FactoryManager):

    def set_module(self):
        return process
    pass


#t = ProcessManager()
#t.get_available_class_types()

#tt = {"a":"1","b":"2"}
#p = process.Export(**tt)

#t.add_class_object("Slice",tt)

#t.pass_thru_stack("dog")

