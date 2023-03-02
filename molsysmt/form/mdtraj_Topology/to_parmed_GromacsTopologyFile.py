from molsysmt._private.digestion import digest

@digest(form='mdtraj.Topology')
def to_parmed_GromacsTopologyFile(item, atom_indices='all'):

    from . import to_parmed_Structure
    from .parmed_Structure import to_parmed_GromacsTopologyFile as parmed_Structure_to_parmed_GromacsTopologyFile

    tmp_item = to_parmed_Structure(item, atom_indices=atom_indices)
    tmp_item = parmed_Structure_to_parmed_GromacsTopologyFile(tmp_item)

    return tmp_item

def _to_parmed_GromacsTopologyFile(item, molecular_system, atom_indices='all', structure_indices='all'):

    return to_parmed_Structure(item, atom_indices=atom_indices)


