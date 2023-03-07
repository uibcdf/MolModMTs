form_name = 'openmm.Simulation'
form_type = 'class'
form_info = ["", ""]

from .is_openmm_Simulation import is_openmm_Simulation

from .attributes import attributes

from .extract import extract
from .add import add
from .append_structures import append_structures
from .get import *
from .set import *
from .iterators import StructuresIterator, TopologyIterator

from .to_file_pdb import to_file_pdb, _to_file_pdb
from .to_molsysmt_Topology import to_molsysmt_Topology, _to_molsysmt_Topology
from .to_openmm_Context import to_openmm_Context, _to_openmm_Context
from .to_openmm_Topology import to_openmm_Topology, _to_openmm_Topology
from .to_molsysmt_MolSys import to_molsysmt_MolSys, _to_molsysmt_MolSys
from .to_molsysmt_Structures import to_molsysmt_Structures, _to_molsysmt_Structures
from .to_openmm_Modeller import to_openmm_Modeller, _to_openmm_Modeller
from .to_pdbfixer_PDBFixer import to_pdbfixer_PDBFixer, _to_pdbfixer_PDBFixer

_convert_to={
        'file:pdb': _to_file_pdb,
        'molsysmt.Topology': _to_molsysmt_Topology,
        'openmm.Context': _to_openmm_Context,
        'openmm.Topology': _to_openmm_Topology,
        'molsysmt.MolSys': _to_molsysmt_MolSys,
        'molsysmt.Structures': _to_molsysmt_Structures,
        'openmm.Modeller': _to_openmm_Modeller,
        'pdbfixer.PDBFixer': _to_pdbfixer_PDBFixer,
        }
