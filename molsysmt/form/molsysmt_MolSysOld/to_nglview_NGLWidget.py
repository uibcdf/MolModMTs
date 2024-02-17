from molsysmt._private.digestion import digest
from molsysmt._private.variables import is_all

@digest(form='molsysmt.MolSysOld')
def to_nglview_NGLWidget(item, atom_indices='all', structure_indices='all', skip_digestion=False):

    from nglview import show_molsysmt
    from molsysmt.basic import extract

    if not (is_all(atom_indices) and is_all(structure_indices)):
        tmp_item = extract(item, selection=atom_indices, structure_indices=structure_indices, skip_digestion=True)
    else:
        tmp_item = item


    tmp_item = show_molsysmt(tmp_item)

    return tmp_item

