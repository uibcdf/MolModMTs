from molsysmt._private.digestion import digest

@digest(form='nglview.NGLWidget')
def to_molsysmt_Structures(item, atom_indices='all', structure_indices='all', skip_digestion=False):

    from molsysmt.native.structures import Structures
    from . import get_coordinates_from_atom, get_box_from_system, get_structure_id_from_system, get_time_from_system

    tmp_item = Structures()
    coordinates = get_coordinates_from_atom(item, indices=atom_indices, structure_indices=structure_indices,
                                            skip_digestion=True)
    box = get_box_from_system(item, structure_indices=structure_indices, skip_digestion=True)
    structure_id = get_structure_id_from_system(item, structure_indices=structure_indices, skip_digestion=True)
    time = get_time_from_system(item, structure_indices=structure_indices, skip_digestion=True)
    tmp_item.append(coordinates=coordinates, box=box, structure_id=structure_id, time=time, skip_digestion=True)

    return tmp_item

