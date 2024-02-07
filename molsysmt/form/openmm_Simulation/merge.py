from molsysmt._private.exceptions import NotImplementedMethodError
from molsysmt._private.digestion import digest

@digest(form='openmm.Simulation')
def merge(items, atom_indices='all', structure_indices='all', skip_digestion=False):

    raise NotImplementedMethodError()

