def to_molsysmt_Trajectory(item, selection='all', structure_indices='all', syntaxis='MolSysMT'):

    from molsysmt.tools.file_msmpk import is_file_msmpk
    from molsysmt.basic import convert

    if not is_file_msmpk(item):
        raise ValueError

    tmp_item = convert(item, 'molsysmt.Trajectory', selection=selection, structure_indices=structure_indices, syntaxis=syntaxis)

    return tmp_item

