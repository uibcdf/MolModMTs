form_name = 'file:h5'
form_type = 'file'
form_info = ["", ""]

piped_topological_attribute = None
piped_structural_attribute = None
piped_any_attribute = None

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

from .to_mdtraj_HDF5TrajectoryFile import to_mdtraj_HDF5TrajectoryFile
from .to_molsysmt_MolSysOld import to_molsysmt_MolSysOld
from .to_molsysmt_TopologyOld import to_molsysmt_TopologyOld
from .to_molsysmt_StructuresOld import to_molsysmt_StructuresOld
from .to_nglview_NGLWidget import to_nglview_NGLWidget
from .to_openmm_Topology import to_openmm_Topology
from .to_mdtraj_Topology import to_mdtraj_Topology
from .to_mdtraj_Trajectory import to_mdtraj_Trajectory
from .to_file_pdb import to_file_pdb

_convert_to={
        'file:h5': extract,
        'mdtraj.HDF5TrajectoryFile': to_mdtraj_HDF5TrajectoryFile,
        'molsysmt.MolSysOld': to_molsysmt_MolSysOld,
        'molsysmt.TopologyOld': to_molsysmt_TopologyOld,
        'molsysmt.StructuresOld': to_molsysmt_StructuresOld,
        'nglview.NGLWidget': to_nglview_NGLWidget,
        'openmm.Topology': to_openmm_Topology,
        'mdtraj.Topology': to_mdtraj_Topology,
        'mdtraj.Trajectory': to_mdtraj_Trajectory,
        'file:pdb': to_file_pdb,
        }
