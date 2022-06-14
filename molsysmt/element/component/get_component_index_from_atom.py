from molsysmt._private.exceptions import *
from molsysmt._private.digestion import *
import numpy as np

def get_component_index_from_atom(molecular_system, indices='all', check=True):

    if check:

        digest_single_molecular_system(molecular_system)
        indices = digest_indices(indices)

    from molsysmt.basic import get
    from molsysmt.lib import bonds as _libbonds

    n_atoms, n_bonds = get(molecular_system, element='system', n_atoms=True, n_bonds=True)

    if n_bonds==0:

        output = np.full(n_atoms, None, dtype=object)

    else:

        atoms_indices = get(molecular_system, element='bond', indices='all', atom_index=True)

        output = _libbonds.component_indices(atoms_indices, n_atoms, n_bonds)
        output = np.ascontiguousarray(output, dtype=int)

    if indices is not 'all':

        output = output[indices]

    return output
