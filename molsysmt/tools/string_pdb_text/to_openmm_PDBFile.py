def to_openmm_PDBFile(item, selection='all', structure_indices='all', syntaxis='MolSysMT'):

    from molsysmt.tools.string_pdb_text import is_string_pdb_text
    from molsysmt.basic import convert

    if not is_string_pdb_text(item):
        raise ValueError

    tmp_item = convert(item, to_form='openmm.PDBFile', selection=selection, structure_indices=structure_indices, syntaxis=syntaxis)

    return tmp_item

