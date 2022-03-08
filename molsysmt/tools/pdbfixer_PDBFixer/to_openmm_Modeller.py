from molsysmt.tools.pdbfixer_PDBFixer.is_pdbfixer_PDBFixer import is_pdbfixer_PDBFixer
from molsysmt._private_tools.exceptions import WrongFormError, WrongAtomIndicesError
from molsysmt._private_tools.exceptions import LibraryNotFoundError
from molsysmt._private_tools.atom_indices import digest_atom_indices

def to_openmm_Modeller(item, atom_indices='all', check=True):

    if check:

        try:
            is_pdbfixer_PDBFixer(item)
        except:
            raise WrongFormError('pdbfixer.PDBFixer')

        try:
            atom_indices = digest_atom_indices(atom_indices)
        except:
            raise WrongAtomIndicesError()

        try:
            structure_indices = digest_structure_indices(structure_indices)
        except:
            raise WrongStructureIndicesError()

    from molsysmt import puw
    from molsysmt.tools.pdbfixer_PDBFixer import to_openmm_Topology as pdbfixer_PDBFixer_to_openmm_Topology

    tmp_item = pdbfixer_PDBFixer_to_openmm_Topology(item, atom_indices=atom_indices, check=False)
    coordinates = get_coordinates_from_atom(tmp_item, indices=atom_indices, check=False)
    coordinates = puw.convert(coordinates, to_units='nanometer', to_form='openmm.unit')
    tmp_item = openmm_Modeller(tmp_item, coordinates)

    return tmp_item

