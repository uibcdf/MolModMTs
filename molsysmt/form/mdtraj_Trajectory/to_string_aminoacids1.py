from molsysmt._private.digestion import digest
import numpy as np

@digest(form='mdtraj.Trajectory')
def to_string_aminoacids1(item, group_indices='all'):

    from . import to_mdtraj_Topology
    from ..mdtraj_Topology import to_string_aminoacids1 as mdtraj_Topology_to_string_aminoacids1

    tmp_item = to_mdtraj_Topology(item)
    tmp_item = mdtraj_Topology_to_string_aminoacids1(tmp_item, group_indices=group_indices)

    return tmp_item

def _to_string_aminoacids1(item, molecular_system, atom_indices='all', structure_indices='all'):

    from . import get_group_index_from_atom

    group_indices = get_group_index_from_atom(item, indices=atom_indices)
    group_indices = np.unique(group_indices)

    return to_string_aminoacids1(item, group_indices=group_indices)

