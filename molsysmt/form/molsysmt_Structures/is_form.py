def is_form(item):

    item_fullname = item.__class__.__module__+'.'+item.__class__.__name__
    output = (item_fullname == 'molsysmt.native.structures_new.StructuresNEW')

    return output

