form_name = 'molsysmt.Topology'
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
from .get_topological_attributes import *
from .set import *
from .iterators import TopologyIterator

from .to_file_h5msm import to_file_h5msm
from .to_networkx_Graph import to_networkx_Graph
from .to_openmm_Topology import to_openmm_Topology

_convert_to={
        'molsysmt.Topology': extract,
        'file:h5msm': to_file_h5msm,
        'networkx.Graph': to_networkx_Graph,
        'openmm.Topology': to_openmm_Topology,
        }
