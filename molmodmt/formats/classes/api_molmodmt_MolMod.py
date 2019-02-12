from os.path import basename as _basename
from molmodmt.utils.exceptions import *
from molmodmt.native.molmod import MolMod as _molmodmt_MolMod

form_name=_basename(__file__).split('.')[0].replace('api_','').replace('_','.')

is_form={
    _molmodmt_MolMod : form_name
}

def get_shape(item):
    raise NotImplementedError(NotImplementedMessage)

def select_with_mdtraj(item, selection):
    raise NotImplementedError(NotImplementedMessage)

def extract_atoms_list(item, atoms_list):
    raise NotImplementedError(NotImplementedMessage)
