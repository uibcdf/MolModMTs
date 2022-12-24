from molsysmt._private.digestion import digest

@digest(form='pdbfixer.PDBFixer')
def to_file_pdb(item, atom_indices='all', output_filename=None, digest=True):

    from . import to_openmm_Topology
    from . import get_coordinates_from_atom, get_box_from_atom
    from ..openmm_Topology import to_file_pdb as openmm_Topology_to_file_pdb

    tmp_item = to_openmm_Topology(item, atom_indices=atom_indices, digest=False)
    coordinates = get_coordinates_from_atom(tmp_item, atom_indices=atom_indices, digest=False)
    box = get_box_from_atom(tmp_item, digest=False)
    tmp_item = openmm_Topology_to_file_pdb(tmp_item, coordinates=coordinates, box=box,
                                           output_filename=output_filename, digest=False)

    return tmp_item


