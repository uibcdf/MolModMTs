from molsysmt._private.exceptions import NotImplementedMethodError
from molsysmt._private.digestion import digest

@digest(form='string:amino_acids_1')
def append_structures(item, structure_id=None, time=None, coordinates=None, box=None, skip_digestion=False):

    raise NotImplementedMethodError()

