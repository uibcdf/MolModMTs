from molsysmt._private.digestion import digest

@digest(form='molsysmt.PDBFileHandler')
def to_nglview_NGLWidget(item, atom_indices='all', structure_indices='all', skip_digestion=False):

    from .to_molsysmt_MolSys import to_molsysmt_MolSys
    from ..molsysmt_MolSys import to_nglview_NGLWidget as molsysmt_MolSys_to_nglview_NGLWidget

    tmp_item = to_molsysmt_MolSys(item, atom_indices=atom_indices, structure_indices=structure_indices,
                                  skip_digestion=True)
    tmp_item = molsysmt_MolSys_to_nglview_NGLWidget(tmp_item, skip_digestion=True)

    return tmp_item

