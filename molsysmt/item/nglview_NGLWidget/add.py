from molsysm._private.exception import NotImplementedMethodError
from molsysmt._private.digestion import digest

@digest(form='nglview.NGLWidget', to_form='nglview.NGLWidget')
def add(to_item, item):

    raise NotImplementedMethodError()

