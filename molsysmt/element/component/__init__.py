from . import water
from . import ion
from . import small_molecule
from . import peptide
from . import protein
from . import dna
from . import rna
from . import lipid
from . import oligosaccharide

from .get_component_index_from_atom import get_component_index_from_atom
from .get_component_index_from_bonded_atoms import get_component_index_from_bonded_atoms
from .get_component_id_from_component import get_component_id_from_component
from .get_component_name_from_component import get_component_name_from_component
from .get_component_type_from_group_names import get_component_type_from_group_names
from .get_component_type_from_component import get_component_type_from_component
from .get_n_components_from_system import get_n_components_from_system

from .is_component_type import is_component_type

_component_types = [
        'water',
        'ion',
        'small molecule',
        'peptide',
        'protein',
        'dna',
        'rna',
        'lipid',
        'oligosaccharide'
        ]

_singular_component_type_to_plural = {
    'water': 'waters',
    'ion': 'ions',
    'small molecule': 'small molecules',
    'peptide': 'peptides',
    'protein': 'proteins',
    'lipid': 'lipids',
    'oligosaccharide': 'oligosaccharides',
}

_plural_component_types_to_singular = {
    'waters': 'water',
    'ions': 'ion',
    'small molecules': 'small molecule',
    'peptides': 'peptide',
    'proteins': 'protein',
    'lipids': 'lipid',
    'oligosaccharides': 'oligosaccharide',
}

