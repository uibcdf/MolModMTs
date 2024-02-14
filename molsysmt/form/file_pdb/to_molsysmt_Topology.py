from molsysmt._private.digestion import digest

@digest(form='file:pdb')
def to_molsysmt_Topology(item, atom_indices='all', skip_digestion=False):

    from . import to_openmm_PDBFile
    from ..openmm_PDBFile import to_molsysmt_Topology as openmm_PDBFile_to_molsysmt_Topology

    tmp_item = to_openmm_PDBFile(item, skip_digestion=True)
    tmp_item = openmm_PDBFile_to_molsysmt_Topology(tmp_item, atom_indices=atom_indices, skip_digestion=True)

    return tmp_item

