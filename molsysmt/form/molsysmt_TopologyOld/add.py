from molsysmt._private.exceptions import NotImplementedMethodError
from molsysmt._private.digestion import digest

@digest(form='molsysmt.TopologyOld', to_form='molsysmt.TopologyOld')
def add(to_item, item, skip_digestion=False):

    to_item.add(item)

    pass
