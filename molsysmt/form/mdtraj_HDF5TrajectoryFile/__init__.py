form_name = 'mdtraj.HDF5TrajectoryFile'
form_type = 'class'
form_info = ["", ""]

from .is_form import is_form

from .attributes import attributes
from .has_attribute import has_attribute

from .extract import extract
from .copy import copy
from .add import add
from .merge import merge
from .append_structures import append_structures
from .get import *
from .set import *
from .iterators import StructuresIterator, TopologyIterator

from .to_mdtraj_Topology import to_mdtraj_Topology
from .to_openmm_Topology import to_openmm_Topology
from .to_molsysmt_TopologyOld import to_molsysmt_TopologyOld
from .to_molsysmt_StructuresOld import to_molsysmt_StructuresOld
from .to_molsysmt_MolSysOld import to_molsysmt_MolSysOld

_convert_to={
        'mdtraj.HDF5TrajectoryFile': extract,
        'mdtraj.Topology': to_mdtraj_Topology,
        'openmm.Topology': to_openmm_Topology,
        'molsysmt.TopologyOld': to_molsysmt_TopologyOld,
        'molsysmt.StructuresOld': to_molsysmt_StructuresOld,
        'molsysmt.MolSysOld': to_molsysmt_MolSysOld,
        }
