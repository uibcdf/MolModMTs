from molsysm._private.exception import NotImplementedMethodError
from molsysmt._private.digestion import digest

@digest(form='openmm.AmberPrmtopFile', to_form='openmm.AmberPrmtopFile')
def add(to_item, item):

    raise NotImplementedMethodError()

