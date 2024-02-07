from molsysmt._private.digestion import digest

@digest(form='openmm.PDBFile')
def to_molsysmt_StructuresOld(item, atom_indices='all', structure_indices='all', skip_digestion=False):

    from molsysmt.native.structures_old import StructuresOld
    from .get import get_coordinates_from_atom, get_box_from_system, get_structure_id_from_system, get_time_from_system

    coordinates = get_coordinates_from_atom(item, indices=atom_indices, structure_indices=structure_indices,
                                            skip_digestion=True)
    box = get_box_from_system(item, structure_indices=structure_indices, skip_digestion=True)
    structure_id = get_structure_id_from_system(item, structure_indices=structure_indices, skip_digestion=True)
    time = get_time_from_system(item, structure_indices=structure_indices, skip_digestion=True)

    tmp_item = StructuresOld()
    tmp_item.append_structures(coordinates=coordinates, structure_id=structure_id, time=time, box=box,
                               skip_digestion=True)

    return tmp_item

