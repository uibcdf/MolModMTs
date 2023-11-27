from molsysmt._private.digestion import digest

@digest(form='file:mmtf')
def to_molsysmt_StructuresOld(item, atom_indices='all', structure_indices='all'):

    from . import to_mmtf_MMTFDecoder
    from ..mmtf_MMTFDecoder import to_molsysmt_StructuresOld as mmtf_MMTFDecoder_to_molsysmt_StructuresOld

    tmp_item = to_mmtf_MMTFDecoder(item)
    tmp_item = mmtf_MMTFDecoder_to_molsysmt_StructuresOld(tmp_item, atom_indices=atom_indices, structure_indices=structure_indices)

    return tmp_item
