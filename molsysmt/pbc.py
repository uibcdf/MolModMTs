from .utils.engines import digest as _digest_engines
from .utils.frame_indices import digest as _digest_frame_indices
from .utils.forms import digest as _digest_forms
from molsysmt.lib import box as _libbox
import numpy as _np

def minimum_image_convention(item, selection='all', reference_selection=None,
                             reference_coordinates=None, center_of_selection='geometrical_center',
                             center_of_reference_selection='geometrical_center', frame_indices='all',
                             syntaxis='MDTraj', engine='MolSysMT'):

    from molsysmt import convert, select, get, duplicate
    from molsysmt import set as _set
    from molsysmt.utils.math import serialized_lists
    from molsysmt.centers import geometrical_center

    n_atoms, n_frames = get(item, n_atoms=True, n_frames=True)
    atom_indices = select(item, selection=selection, syntaxis=syntaxis)
    n_atom_indices = len(atom_indices)
    frame_indices = _digest_frame_indices(item, frame_indices)
    n_frame_indices = len(frame_indices)

    engine = _digest_engines(engine)
    form_in, _ = _digest_forms(item, engine)
    tmp_item = duplicate(item)

    if engine=='MolSysMT':

        if reference_coordinates is None:
            if center_of_reference_selection == 'geometrical_center':
                reference_coordinates = geometrical_center(tmp_item, selection=reference_selection,
                                                        frame_indices=frame_indices, syntaxis=syntaxis, engine=engine)

        molecules = get(tmp_item, molecules=True)

        if selection not in [None, 'all']:
            working_molecules = []
            for molecule in molecules:
                if len(_np.intersect1d(molecule, atom_indices)):
                    working_molecules.append(molecule)
            molecules=working_molecules

        molecules_serialized = serialized_lists(molecules, dtype='int64')

        if center_of_selection == 'geometrical_center':
            centers_molecules = geometrical_center(tmp_item, selection_groups=molecules,
                    frame_indices=frame_indices, syntaxis=syntaxis, engine=engine)

        coordinates, box, box_shape = get(tmp_item, coordinates=True, box=True, box_shape=True, frame_indices='all')

        length_units = coordinates.unit
        coordinates = _np.asfortranarray(coordinates._value, dtype='float64')
        reference_coordinates = _np.asfortranarray(reference_coordinates._value, dtype='float64')
        box = _np.asfortranarray(box._value, dtype='float64')
        orthogonal = 0
        if box_shape=='cubic': orthogonal = 1

        _libbox.minimum_image_convention(coordinates, reference_coordinates, centers_molecules,
                molecules_serialized.indices, molecules_serialized.values,
                molecules_serialized.starts, frame_indices, box, orthogonal,
                n_frames, n_atoms, molecules_serialized.n_indices, molecules_serialized.n_values,
                n_frame_indices)

        coordinates=_np.ascontiguousarray(coordinates)*length_units

        _set(tmp_item, coordinates=coordinates)

        del(coordinates, box, length_units)
        del(molecules, molecules_serialized)

        return tmp_item

    else:

        raise NotImplementedError

def unwrap_molecules_from_pbc_cell(item, selection='all', frame_indices='all', syntaxis='MDTraj', engine='MolSysMT'):

    from molsysmt import convert, select, get, duplicate
    from molsysmt import set as _set
    from molsysmt.utils.math import serialized_lists

    n_atoms, n_frames = get(item, n_atoms=True, n_frames=True)
    atom_indices = select(item, selection=selection, syntaxis=syntaxis)
    n_atom_indices = len(atom_indices)
    frame_indices = _digest_frame_indices(item, frame_indices)
    n_frame_indices = len(frame_indices)

    engine = _digest_engines(engine)
    form_in, _ = _digest_forms(item, engine)
    tmp_item = duplicate(item)

    if engine=='MolSysMT':

        molecules = get(tmp_item, molecules=True)

        if selection not in [None, 'all']:
            working_molecules = []
            for molecule in molecules:
                if len(_np.intersect1d(molecule, atom_indices)):
                    working_molecules.append(molecule)
            molecules=working_molecules

        molecules_serialized = serialized_lists(molecules, dtype='int64')

        bonded_atoms = get(tmp_item, target='atom', indices=atom_indices, bonded_atoms=True)
        bonded_atoms_serialized = serialized_lists(bonded_atoms, dtype='int64')

        coordinates, box, box_shape = get(tmp_item, coordinates=True, box=True, box_shape=True, frame_indices='all')

        length_units = coordinates.unit
        coordinates = _np.asfortranarray(coordinates._value, dtype='float64')
        box = _np.asfortranarray(box._value, dtype='float64')
        orthogonal = 0
        if box_shape=='cubic': orthogonal = 1

        _libbox.unwrap(coordinates, molecules_serialized.indices, molecules_serialized.values, molecules_serialized.starts,
                       bonded_atoms_serialized.indices, bonded_atoms_serialized.values, bonded_atoms_serialized.starts,
                       frame_indices, box, orthogonal, n_frames, n_atoms,
                       molecules_serialized.n_indices, molecules_serialized.n_values,
                       bonded_atoms_serialized.n_indices, bonded_atoms_serialized.n_values,
                       n_frame_indices)

        coordinates=_np.ascontiguousarray(coordinates)*length_units

        _set(tmp_item, coordinates=coordinates)

        del(coordinates, box, length_units)
        del(molecules, molecules_serialized, bonded_atoms, bonded_atoms_serialized)

        return tmp_item

    else:

        raise NotImplementedError

def wrap_molecules_to_pbc_cell(self):
    #self.coors=asfortran_np.array(self.coors)
    #libbox.wrap_all_inplace(self.coors,self.box,self.invbox,self.orthogonal,self.coors.shape[0])
    #self.coors=ascontiguous_np.array(self.coors)
    raise NotImplementedError
