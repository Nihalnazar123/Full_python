# packages and modules
# packages are collection of modules
# modules are collection of functions
# eg:
#    package       modules       functions
#     scipy   -    integration - single_integ
#                              - double_integ
#                              - triple_integ

# for calling a function from an other module or other directory we use
# format for calling

# from packagename.modulename import function
# eg:

from Basic__python.basic_programs.import_for_packages import add,sub
add(1,2)
sub(6,3)

# for import whole
from Basic__python.basic_programs.import_for_packages import *
add(2,5)
sub(6,2)
