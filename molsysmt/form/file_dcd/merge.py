from molsysmt._private.exceptions import NotImplementedMethodError
from molsysmt._private.digestion import digest

@digest(form='file:dcd')
def merge(items, atom_indices='all', structure_indices='all'):

    raise NotImplementedMethodError()

