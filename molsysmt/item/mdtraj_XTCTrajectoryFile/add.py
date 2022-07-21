from molsysm._private.exception import NotImplementedMethodError
from molsysmt._private.digestion import digest

@digest(form='mdtraj.XTCTrajectoryFile', to_form='mdtraj.XTCTrajectoryFile')
def add(to_item, item):

    raise NotImplementedMethodError()

