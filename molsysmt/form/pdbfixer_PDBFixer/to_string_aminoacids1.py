from molsysmt._private.digestion import digest

@digest(form='pdbfixer.PDBFixer')
def to_string_aminoacids1(item, atom_indices='all', digest=True):

    from . import to_string_aminoacids3
    from ..string_aminoacids3 import to_string_aminoacids1 as string_aminoacids3_to_string_aminoacids1

    tmp_item = to_string_aminoacids3(item, atom_indices=atom_indices, digest=False)
    tmp_item = string_aminoacids3_to_string_aminoacids1(tmp_item, digest=False)

    return tmp_item

