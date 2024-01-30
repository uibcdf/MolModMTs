from molsysmt._private.digestion import digest

@digest(form='mdtraj.HDF5TrajectoryFile')
def to_openmm_Topology(item, atom_indices='all', skip_digestion=False):

    from . import to_mdtraj_Topology
    from ..mdtraj_Topology import to_openmm_Topology as mdtraj_Topology_to_openmm_Topology

    tmp_item = to_mdtraj_Topology(item, atom_indices=atom_indices, skip_digestion=True)
    tmp_item = mdtraj_Topology_to_openmm_Topology(item, skip_digestion=True)

    return tmp_item

