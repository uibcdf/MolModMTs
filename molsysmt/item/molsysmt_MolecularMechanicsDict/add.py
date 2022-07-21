from molsysm._private.exception import NotImplementedMethodError
from molsysmt._private.digestion import digest

@digest(form='molsysmt.MolecularMechanicsDict', to_form='molsysmt.MolecularMechanicsDict')
def add(to_item, item):

    raise NotImplementedMethodError()

