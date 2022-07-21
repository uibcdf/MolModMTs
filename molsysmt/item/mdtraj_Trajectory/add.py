from molsysm._private.exception import NotImplementedMethodError
from molsysmt._private.digestion import digest

@digest(form='mdtraj.Trajectory', to_form='mdtraj.Trajectory')
def add(to_item, item):

   raise NotImplementedMethodError()

