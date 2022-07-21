from molsysm._private.exception import NotImplementedMethodError
from molsysmt._private.digestion import digest

@digest(form='molsysmt.MolecularMechanics', to_form='molsysmt.MolecularMechanics')
def add(to_item, item):

    raise NotImplementedMethodError()

