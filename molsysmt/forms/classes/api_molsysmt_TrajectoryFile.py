from os.path import basename as _basename
from molsysmt.utils.exceptions import *
from molsysmt.native.trajectory_file import TrajectoryFile as _molsysmt_TrajectoryFile

form_name=_basename(__file__).split('.')[0].replace('api_','').replace('_','.')

is_form={
    _molsysmt_TrajectoryFile : form_name,
    'molsysmt.TrajectoryFile': form_name
}

info=["",""]

def extract_subsystem(item, atom_indices='all', frame_indices='all'):

    if (atom_indices is 'all') and (frame_indices is 'all'):
        return item
    else:
        raise NotImplementedError

def duplicate(item):

    return item.duplicate()

###### Get

## system

def get_form_from_system(item, indices='all', frame_indices='all'):

    return form_name
