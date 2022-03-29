from .is_string_pdb_id import is_string_pdb_id
from molsysmt._private.exceptions import *
from molsysmt._private.digestion import *

def add(to_item, item, check=True):

    if check:

        try:
            is_string_pdb_id(item)
        except:
            raise WrongFormError('string:pdb_id')

        try:
            is_string_pdb_id(to_item)
        except:
            raise WrongFormError('string:pdb_id')

    raise NotImplementedMethodError()
    pass

