def to_molsysmt_MolSys(item, selection='all', structure_indices='all', syntaxis='MolSysMT'):

    from molsysmt.tools.aminoacids3 import is_string_aminoacids3
    from molsysmt.basic import convert

    if not is_string_aminoacids3(item):
        raise ValueError

    tmp_item = convert(item, to_form='molsysmt.MolSys', selection=selection,
            structure_indices=structure_indices, syntaxis=syntaxis)

    return tmp_item

