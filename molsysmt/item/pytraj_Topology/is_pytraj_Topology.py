
def is_pytraj_Topology(item):

    item_fullname = item.__class__.__module__+'.'+item.__class__.__name__
    output = (item_fullname == 'pytraj.topology.topology.Topology')

    return output

