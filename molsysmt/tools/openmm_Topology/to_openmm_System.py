def to_openmm_System(item, selection='all', structure_indices='all', syntaxis='MolSysMT'):

    from molsysmt.tools.openmm_Topology import is_openmm_Topology
    from molsysmt.basic import convert

    if not is_openmm_Topology(item):
        raise ValueError

    tmp_item = convert(item, to_form='openmm.System', selection=selection,
            structure_indices=structure_indices, syntaxis=syntaxis)

    return tmp_item

