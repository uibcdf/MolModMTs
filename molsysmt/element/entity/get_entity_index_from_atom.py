from molsysmt._private.exceptions import *
from molsysmt._private.digestion import *
from molsysmt._private.variables import is_all
import numpy as np

def get_entity_index_from_atom(molecular_system, indices='all', check=True):

    if check:

        digest_single_molecular_system(molecular_system)
        indices = digest_indices(indices)

    from .get_entity_all_from_atom import get_entity_all_from_atom

    output, _,  _ = get_entity_all_from_atom(molecular_system)

    if not is_all(indices):
        output = output[indices]

    return output


