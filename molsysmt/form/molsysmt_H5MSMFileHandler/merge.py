from molsysmt._private.exceptions import NotImplementedMethodError
from molsysmt._private.digestion import digest

@digest(form='molsysmt.H5MSMFileHandler')
def merge(items, atom_indices='all', structure_indices='all'):

    raise NotImplementedMethodError()
