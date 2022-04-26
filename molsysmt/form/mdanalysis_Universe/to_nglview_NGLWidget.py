from molsysmt._private.digestion import digest_item, digest_atom_indices, digest_structure_indices

def to_nglview_NGLWidget(item, atom_indices='all', structure_indices='all', check=True):

    if check:

        digest_item(item, 'mdanalysis.Universe')
        atom_indices = digest_atom_indices(atom_indices)
        structure_indices = digest_structure_indices(structure_indices)

    from . import extract
    from nglview import show_mdanalysis

    tmp_item = extract(item, atom_indices=atom_indices, structure_indices=structure_indices,
            copy_if_all=False, check=False)
    tmp_item = show_mdanalysis(tmp_item)

    return tmp_item

