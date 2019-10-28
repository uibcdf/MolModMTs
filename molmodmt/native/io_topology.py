from .topology import Topology as _Topology

def from_mdtraj(item, atom_indices='all', frame_indices='all'):

    return from_mdtraj_Topology(item.topology, atom_indices='all', frame_indices='all')

def from_mdtraj_Topology(item, atom_indices='all', frame_indices='all'):

    from molmodmt import extract
    return extract(item, selection=atom_indices)

def to_mdtraj_Topology(item, atom_indices='all', frame_indices='all'):

    from molmodmt import extract
    return extract(item, selection=atom_indices)

def from_openmm_Topology(item, atom_indices='all', frame_indices='all'):
    from molmodmt import convert
    return convert(item, to_form='mdtraj.Topology', selection=atom_indices)

def from_openmm_Modeller(item, atom_indices='all', frame_indices='all'):
    from molmodmt import convert
    return convert(item, to_form='mdtraj.Topology', selection=atom_indices)

def from_openmm_Topology(item, atom_indices='all', frame_indices='all'):
    from molmodmt import convert
    return convert(item, to_form='mdtraj.Topology', selection=atom_indices)

def from_molmod_Structure(item, atom_indices='all', frame_indices='all'):
    from molmodmt import convert
    return convert(item, to_form='mdtraj.Topology', selection=atom_indices)

def from_pdb(item, atom_indices='all', frame_indices='all'):
    from molmodmt import convert
    return convert(item, to_form='mdtraj.Topology', selection=atom_indices)

def from_hdf5(item, atom_indices='all', frame_indices='all'):
    from molmodmt import convert
    return convert(item, to_form='mdtraj.Topology', selection=atom_indices)

def from_top(item, atom_indices='all', frame_indices='all'):
    from molmodmt import convert
    return convert(item, to_form='mdtraj.Topology', selection=atom_indices)
