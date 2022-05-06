from molsysmt._private.digestion import digest_item, digest_atom_indices, digest_structure_indices

def to_mdtraj_Topology(item, atom_indices='all', structure_indices='all', check=True):

    if check:

        digest_item(item, 'file:gro')
        atom_indices = digest_atom_indices(atom_indices)
        structure_indices = digest_structure_indices(structure_indices)

    from . import to_mdtraj_Trajectory
    from ..mdtraj_Trajectory import to_mdtraj_Topology as mdtraj_Trajectory_to_mdtraj_Topology

    tmp_item = to_mdtraj_Trajectory(item, atom_indices=atom_indices,
            structure_indices=structure_indices, check=False)
    tmp_item = mdtraj_Trajectory_to_mdtraj_Topology(tmp_item, check=False)

    return tmp_item

