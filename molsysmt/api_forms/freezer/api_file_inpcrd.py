from molsysmt._private_tools.exceptions import *
from molsysmt.api_forms.common_gets import *
import numpy as np
import sys
import importlib
from molsysmt.native.molecular_system import molecular_system_components
from molsysmt._private_tools.files_and_directories import temp_filename

form_name='file:inpcrd'
from_type='file'

is_form = {
        'file:inpcrd':form_name
    }

info = ["AMBER ASCII restart/inpcrd file format","https://ambermd.org/FileFormats.php#trajectory"]

has = molecular_system_components.copy()
for ii in ['coordinates', 'box']:
    has[ii]=True

def to_file_inpcrd(item, molecular_system=None, atom_indices='all', structure_indices='all', output_filename=None, copy_if_all=True):

    tmp_molecular_system = None

    if (atom_indices is 'all') and (structure_indices is 'all'):
        if copy_if_all:
            tmp_item = extract(item, output_filename=output_filename)
            if molecular_system is not None:
                tmp_molecular_system = molecular_system.combine_with_items(tmp_item)
        else:
            tmp_item = item
            if molecular_system is not None:
                tmp_molecular_system = molecular_system
    else:
        tmp_item = extract(item, atom_indices=atom_indices, structure_indices=structure_indices, output_filename=output_filename)
        if molecular_system is not None:
            tmp_molecular_system = molecular_system.combine_with_items(tmp_item, atom_indices=atom_indices, structure_indices=structure_indices)

    return tmp_item, tmp_molecular_system

def to_molsysmt_MolSys(item, molecular_system=None, atom_indices='all', structure_indices='all'):

    from molsysmt.native.io.molsys import from_file_inpcrd as file_inpcrd_to_molsysmt_MolSys

    tmp_item, tmp_molecular_system = file_inpcrd_to_molsysmt_MolSys(item,
            molecular_system=molecular_system, atom_indices=atom_indices, structure_indices=structure_indices)

    return tmp_item, tmp_molecular_system

def to_molsysmt_Topology(item, molecular_system=None, atom_indices='all', structure_indices='all'):

    from molsysmt.native.io.topology import from_file_inpcrd as file_inpcrd_to_molsysmt_Topology

    tmp_item, tmp_molecular_system = file_inpcrd_to_molsysmt_Topology(item, molecular_system=molecular_system, atom_indices=atom_indices, structure_indices=structure_indices)

    return tmp_item, tmp_molecular_system

def to_molsysmt_Trajectory(item, molecular_system=None, atom_indices='all', structure_indices='all'):

    from molsysmt.native.io.trajectory import from_file_inpcrd as file_inpcrd_to_molsysmt_Trajectory

    tmp_item, tmp_molecular_system = file_inpcrd_to_molsysmt_Trajectory(item, molecular_system=molecular_system, atom_indices=atom_indices, structure_indices=structure_indices)

    return tmp_item, tmp_molecular_system

def to_mdtraj_AmberRestartFile(item, molecular_system=None, atom_indices='all', structure_indices='all'):

    from mdtraj.formats import AmberRestartFile

    tmp_item = AmberRestartFile(item)
    if molecular_system is not None:
        tmp_molecular_system = molecular_system.combine_with_items(tmp_item)
    else:
        tmp_molecular_system = None

    return tmp_item, tmp_molecular_system

def to_openmm_AmberInpcrdFile(item, molecular_system=None, atom_indices='all', structure_indices='all'):

    from openmm.app import AmberInpcrdFile

    tmp_item = AmberInpcrdFile(item)
    if molecular_system is not None:
        tmp_molecular_system = molecular_system.combine_with_items(tmp_item)
    else:
        tmp_molecular_system = None

    return tmp_item, tmp_molecular_system

def extract(item, atom_indices='all', structure_indices='all', output_filename=None):

    if output_filename is None:
        output_filename = temp_filename(extension='inpcrd')

    tmp_item = None

    if (atom_indices is 'all') and (structure_indices is 'all'):

        from shutil import copy as copy_file
        from molsysmt._private_tools.files_and_directories import temp_filename

        copy_file(item, output_filename)

        tmp_item = output_filename

    else:
        raise NotImplementedError()

    return tmp_item


def merge(item_1, item_2):

    raise NotImplementedError

def add(to_item, item):

    raise NotImplementedError

def append_frames(item, step=None, time=None, coordinates=None, box=None):

    raise NotImplementedError()

def concatenate_frames(item, step=None, time=None, coordinates=None, box=None):

    raise NotImplementedError

###### Get

def aux_get(item, indices='all', structure_indices='all'):

    from molsysmt.api_forms import forms

    method_name = sys._getframe(1).f_code.co_name

    if 'openmm.AmberInpcrdFile' in forms:

        tmp_item, _ = to_openmm_AmberInpcrdFile(item)
        module = importlib.import_module('molsysmt.api_forms.api_openmm_AmberInpcrdFile')
        _get = getattr(module, method_name)
        output = _get(tmp_item, indices=indices, structure_indices=structure_indices)

    elif 'mdtraj.AmberRestartFile' in forms:

        tmp_item, _ = to_mdtraj_AmberRestartFile(item)
        module = importlib.import_module('molsysmt.api_forms.api_mdtraj_AmberRestartFile')
        _get = getattr(module, method_name)
        output = _get(tmp_item, indices=indices, structure_indices=structure_indices)

    else:

        raise NotImplementedError

    return output

# Atom

def get_atom_index_from_atom(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_atom_id_from_atom(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_atom_name_from_atom(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_atom_type_from_atom(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_group_index_from_atom (item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_component_index_from_atom (item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_chain_index_from_atom (item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_molecule_index_from_atom (item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_entity_index_from_atom (item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_inner_bonded_atoms_from_atom (item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_n_inner_bonds_from_atom (item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_coordinates_from_atom(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_frame_from_atom(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

## group

def get_group_id_from_group(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_group_name_from_group(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_group_type_from_group(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

## component

def get_component_id_from_component (item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_component_name_from_component (item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_component_type_from_component (item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)


## molecule

def get_molecule_id_from_molecule (item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_molecule_name_from_molecule (item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_molecule_type_from_molecule (item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

## chain

def get_chain_id_from_chain (item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_chain_name_from_chain (item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_chain_type_from_chain (item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

## entity

def get_entity_id_from_entity (item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_entity_name_from_entity (item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_entity_type_from_entity (item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

# System

def get_n_atoms_from_system(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_n_groups_from_system(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_n_components_from_system(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_n_chains_from_system(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_n_molecules_from_system(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_n_entities_from_system(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_n_bonds_from_system(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_coordinates_from_system(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_box_from_system(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_box_shape_from_system(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_box_lengths_from_system(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_box_angles_from_system(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_box_volume_from_system(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_time_from_system(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_step_from_system(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_n_frames_from_system(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_bonded_atoms_from_system(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_has_bonds_from_system(item, indices='all', structure_indices='all'):

    output = False

    if with_topology:
        if get_n_bonds_from_system(item, indices=indices, structure_indices=structure_indices):
            output = True

    return output

## bond

def get_bond_order_from_bond(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_bond_type_from_bond(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_atom_index_from_bond(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

###### Set

def set_box_to_system(item, indices='all', structure_indices='all', value=None):

    raise NotImplementedError

def set_coordinates_to_system(item, indices='all', structure_indices='all', value=None):

    raise NotImplementedError


# System

def get_coordinates_from_system (item, indices='all', structure_indices='all'):

    from molsysmt.api_forms.api_mdtraj_AmberRestartFile import get_coordinates_from_system as _get
    tmp_item = to_mdtraj_AmberRestartFile(item)
    return _get(tmp_item, indices=indices, structure_indices=structure_indices)

def get_n_frames_from_system (item, indices='all', structure_indices='all'):

    from molsysmt.api_forms.api_mdtraj_AmberRestartFile import get_n_frames_from_system as _get
    tmp_item = to_mdtraj_AmberRestartFile(item)
    return _get(tmp_item, indices=indices, structure_indices=structure_indices)

def get_n_atoms_from_system (item, indices='all', structure_indices='all'):

    from molsysmt.api_forms.api_mdtraj_AmberRestartFile import get_n_atoms_from_system as _get
    tmp_item, _ = to_mdtraj_AmberRestartFile(item)
    return _get(tmp_item, indices=indices, structure_indices=structure_indices)


