from molsysmt._private.exceptions import NotImplementedMethodError
from molsysmt._private.digestion import digest

@digest(form='molsysmt.Topology', to_form='molsysmt.Topology', digest=True)
def add(to_item, item):

    raise NotImplementedMethodError()

