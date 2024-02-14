from molsysmt._private.digestion import digest

@digest(form='parmed.Structure')
def to_parmed_GromacsTopologyFile(item, atom_indices='all', skip_digestion=False):

    from . import extract
    from parmed.gromacs import GromacsTopologyFile as GromacsTopologyFile

    tmp_item = extract(item, atom_indices=atom_indices, copy_if_all=False, skip_digestion=True)
    tmp_item = GromacsTopologyFile.from_structure(tmp_item)

    return tmp_item

