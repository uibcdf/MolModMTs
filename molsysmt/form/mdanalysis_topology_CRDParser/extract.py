from molsysmt._private.exceptions import NotImplementedMethodError
from molsysmt._private.digestion import digest
from molsysmt._private.variables import is_all

@digest(form='mdanalysis.topology_CRDParser')
def extract(item, atom_indices='all', copy_if_all=True):

    if is_all(atom_indices):

        if copy_if_all:
            from copy import deepcopy
            tmp_item = deepcopy(item)
        else:
            tmp_item = item
    else:
        NotImplementedMethodError

    return tmp_item
