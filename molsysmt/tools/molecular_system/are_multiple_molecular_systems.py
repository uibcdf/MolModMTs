from molsysmt._private_tools.exceptions import *
from molsysmt._private_tools.lists_and_tuples import is_list_or_tuple
from molsysmt.tools.molecular_system import is_molecular_system
import numpy as np

def are_multiple_molecular_systems(items):

    output = False

    aux_list = []
    if is_list_or_tuple(items):

        for item in items:
            aux_list.append(is_molecular_system(item))

        output = np.all(aux_list)

    return output

