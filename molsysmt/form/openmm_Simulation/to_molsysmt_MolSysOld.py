from molsysmt._private.digestion import digest

@digest(form='openmm.Simulation')
def to_molsysmt_MolSysOld(item, atom_indices='all', structure_indices='all', skip_digestion=False):

    from molsysmt.native.molsys_old import MolSysOld
    from . import to_molsysmt_Topology as openmm_Simulation_to_molsysmt_TopologyOld
    from . import to_molsysmt_Structures as openmm_Simulation_to_molsysmt_StructuresOld

    tmp_item = MolSysOld()
    tmp_item.topology = openmm_Simulation_to_molsysmt_TopologyOld(item, atom_indices=atom_indices,
                                                                  skip_digestion=True)
    tmp_item.structures = openmm_Simulation_to_molsysmt_StructuresOld(item, atom_indices=atom_indices,
                                                                      structure_indices=structure_indices,
                                                                      skip_digestion=True)

    return tmp_item

