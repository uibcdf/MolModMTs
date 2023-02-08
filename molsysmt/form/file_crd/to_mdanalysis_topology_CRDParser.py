from molsysmt._private.digestion import digest

@digest(form='file:crd')
def to_mdanalysis_topology_CRDParser(item, atom_indices='all', structure_indices='all'):

    from MDAnalysis.topology import CRDParser
    from ..mdanalysis_topology_CRDParser import extract as extract_mdanalysis_topology_CRDParser

    tmp_item = CRDParser(item)
    tmp_item = extract_mdanalysis_topology_CRDParser(tmp_item, atom_indices=atom_indices,
            structure_indices=structure_indices, copy_if_all=False)

    return tmp_item
