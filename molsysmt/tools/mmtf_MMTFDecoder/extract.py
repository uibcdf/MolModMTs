def extract(item, atom_indices='all', structure_indices='all', copy_if_all=True, check_form=True):

    if check_form:
        from molsysmt.tools.mmtf_MMTFDecoder.is_mmtf_MMTFDecoder import _checking_form
        _checking_form(item, check_form=check_form)

    if (atom_indices is 'all') and (structure_indices is 'all'):
        if copy_if_all:
            from copy import deepcopy
            tmp_item = deepcopy(item)
        else:
            tmp_item = item
    else:
        raise NotImplementedError()

    return tmp_item

