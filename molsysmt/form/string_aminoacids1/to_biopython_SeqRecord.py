from molsysmt._private.digestion import digest

@digest(form='string:aminoacids1')
def to_biopython_SeqRecord(item, group_indices='all', digest=True):

    from . import to_biopython_Seq
    from ..biopython_Seq import to_biopython_SeqRecord as biopython_Seq_to_biopython_SeqRecord

    tmp_item = to_biopython_Seq(item, atom_indices=atom_indices, structure_indices=structure_indices, digest=False)
    tmp_item = biopython_Seq_to_biopython_SeqRecord(tmp_item, digest=False)

    return tmp_item

