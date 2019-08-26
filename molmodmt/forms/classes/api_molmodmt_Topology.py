from os.path import basename as _basename
from molmodmt.utils.exceptions import *
from molmodmt.native.topology import Topology as _molmodmt_Topology

form_name=_basename(__file__).split('.')[0].replace('api_','').replace('_','.')

is_form={
    _molmodmt_Topology : form_name,
    'molmodmt.Topology': form_name
}


###### Get

## atom

## residue

## chain

## system

def get_n_atoms_from_system(item, indices=None, frame_indices=None):

    from .api_mdtraj_Topology import get_n_atoms_from_system as _get
    return _get(item, indices=indices)

def get_n_residues_from_system(item, indices=None, frame_indices=None):

    from .api_mdtraj_Topology import get_n_residues_from_system as _get
    return _get(item, indices=indices)

def get_n_chains_from_system(item, indices=None, frame_indices=None):

    from .api_mdtraj_Topology import get_n_chains_from_system as _get
    return _get(item, indices=indices)

def get_n_molecules_from_system(item, indices=None, frame_indices=None):

    from .api_mdtraj_Topology import get_n_molecules_from_system as _get
    return _get(item, indices=indices)

def get_n_bonds_from_system(item, indices=None, frame_indices=None):

    from .api_mdtraj_Topology import get_n_bonds_from_system as _get
    return _get(item, indices=indices)


def get_n_frames_from_system(item, indices=None, frame_indices=None):

    from .api_mdtraj_Trayectory import get_n_frames_from_system as _get
    return _get(item, indices=indices)

def get_masses_from_system(item, indices=None, frame_indices=None):

    from .api_mdtraj_Topology import get_masses_from_system as _get
    return _get(item, indices=indices)

def get_bonded_atoms_from_system(item, indices=None, frame_indices=None):

    from .api_mdtraj_Topology import get_bonded_atoms_from_system as _get
    return _get(item, indices=indices)

def get_bonds_from_system(item, indices=None, frame_indices=None):

    from .api_mdtraj_Topology import get_bonds_from_system as _get
    return _get(item, indices=indices)

def get_graph_from_system(item, indices=None, frame_indices=None):

    from .api_mdtraj_Topology import get_graph_from_system as _get
    return _get(item, indices=indices)

def get_molecules_from_system(item, indices=None, frame_indices=None):

    from .api_mdtraj_Topology import get_molecules_from_system as _get
    return _get(item, indices=indices)

def get_box_from_system(item, indices=None, frame_indices=None):

    from .api_mdtraj_Trajectory import get_box_from_system as _get
    return _get(item, indices=indices)

def get_cell_from_system(item, indices=None, frame_indices=None):

    from .api_mdtraj_Trajectory import get_cell_from_system as _get
    return _get(item, indices=indices)


