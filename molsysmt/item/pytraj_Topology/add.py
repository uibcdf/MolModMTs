from molsysm._private.exception import NotImplementedMethodError
from molsysmt._private.digestion import digest

@digest(form='pytraj.Topology', to_form='pytraj.Topology')
def add(to_item, item):

    raise NotImplementedMethodError()

