
def to_string_pdb_text(item, selection='all', frame_indices='all', syntaxis='MolSysMT'):

    from molsysmt.tools.molsysmt_MolSys import is_molsymst_MolSys
    from molsysmt.basic import convert

    if not is_molsysmt_MolSys(item):
        raise ValueError

    tmp_item = convert(item, to_form='string:pdb_text', selection=selection,
            frame_indices=frame_indices, syntaxis=syntaxis)

    return tmp_item
