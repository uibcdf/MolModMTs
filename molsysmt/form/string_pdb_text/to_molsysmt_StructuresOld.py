from molsysmt._private.digestion import digest

@digest(form='string:pdb_text')
def to_molsysmt_StructuresOld(item, atom_indices='all', structure_indices='all', skip_digestion=False):

    from molsysmt.native.structures_old import StructuresOld
    from . import get_time_from_system
    from . import get_box_from_system
    from . import get_coordinates_from_atom

    tmp_item = StructuresOld()
    coordinates = get_coordinates_from_atom(item, indices=atom_indices, structure_indices=structure_indices,
                                            skip_digestion=True)
    time = get_time_from_system(item, structure_indices=structure_indices, skip_digestion=True)
    box = get_box_from_system(item, structure_indices=structure_indices, skip_digestion=True)
    tmp_item.append_structures(coordinates=coordinates, box=box, time=time, skip_digestion=True)

    return tmp_item


