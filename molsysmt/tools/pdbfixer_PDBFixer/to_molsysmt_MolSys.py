def to_molsysmt_MolSys(item, selection='all', frame_indices='all', syntaxis='MolSysMT'):

    from molsysmt.tools.pdbfixer_PDBFixer import is_pdbfixer_PDBFixer
    from molsysmt.basic import convert

    if not is_pdbfixer_PDBFixer(item):
        raise ValueError

    tmp_item = convert(item, to_form='molsysmt.MolSys', selection=selection,
            frame_indices=frame_indices, syntaxis=syntaxis)

    return tmp_item
