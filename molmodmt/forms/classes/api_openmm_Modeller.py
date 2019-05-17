from os.path import basename as _basename
from simtk.openmm.app.modeller import Modeller as _openmm_Modeller

form_name=_basename(__file__).split('.')[0].replace('api_','').replace('_','.')

is_form={
    _openmm_Modeller : form_name,
    'openmm.Modeller' : form_name
}

def to_nglview(item):

    from .api_mdtraj_Trajectory import to_nglview as _mdtraj_to_nglview
    tmp_item = to_mdtraj(item)
    return _mdtraj_to_nglview(tmp_item)

def to_mdtraj(item, selection=None, syntaxis='mdtraj'):

    return to_mdtraj_Trajectory(item, selection=selection, syntaxis=syntaxis)

def to_mdtraj_Trajectory(item, selection=None, syntaxis='mdtraj'):

    from molmodmt import extract as _extract
    import simtk.unit as _unit
    from mdtraj.core.trajectory import Trajectory as _mdtraj_Trajectory

    tmp_topology = to_mdtraj_Topology(item)
    tmp_item = _mdtraj_Trajectory(item.positions/_unit.nanometers, tmp_topology)
    tmp_item = _extract(tmp_item, selection=selection, syntaxis=syntaxis)

    return tmp_item

def to_mdtraj_Topology(item, selection=None, syntaxis='mdtraj'):

    from .api_openmm_Topology import to_mdtraj_Topology as _to_mdtraj_Topology

    tmp_item = to_openmm_Topology(item)
    tmp_item = _to_mdtraj_Topology(tmp_item, selection=selection, syntaxis=syntaxis)
    return tmp_item

def to_openmm_System(item, selection=None, syntaxis='mdtraj'):
    pass

def to_openmm_Topology(item, selection=None, syntaxis='mdtraj'):
    return item.getTopology()

def to_molmodmt_MolMod(item, selection=None, syntaxis='mdtraj'):
    from molmodmt.native.io_molmod import from_openmm_Modeller as MolMod_from_openmm_Modeller
    return MolMod_from_openmm_Modeller(item, selection=selection, syntaxis=syntaxis)

def to_pdb(item, filename = None, selection=None, syntaxis='mdtraj'):

    from simtk.openmm.app import PDBFile as _openmm_app_PDBFILE
    return _openmm_app_PDBFILE.writeFile(item.topology, item.positions, open(filename, 'w'))

def get(item, atom_indices='all', **kwargs):

    tmp_item = extract_atom_indices(item,atom_indices)

    result=[]
    for option in kwargs:
        if option=='n_atoms' and kwargs[option]==True:
            result.append(tmp_item.topology.getNumAtoms())
        if option=='n_frames' and kwargs[option]==True:
            raise NotImplementedError
        if option=='n_residues' and kwargs[option]==True:
            result.append(tmp_item.topology.getNumResidues())
        if option=='n_chains' and kwargs[option]==True:
            result.append(tmp_item.topology.getNumChains())
        if option=='n_molecules' and kwargs[option]==True:
            raise NotImplementedError
        if option=='n_aminoacids' and kwargs[option]==True:
            from molmodmt.topology import is_aminoacid
            n_aminoacids=0
            for residue in tmp_item.topology.residues():
                if is_aminoacid(residue.name): n_aminoacids+=1
            result.append(n_aminoacids)
        if option=='n_nucleotides' and kwargs[option]==True:
            from molmodmt.topology import is_nucleotide
            n_nucleotides=0
            for residue in tmp_item.topology.residues():
                if is_nucleotide(residue.name): n_nucleotides+=1
            result.append(n_nucleotides)
        if option=='n_waters' and kwargs[option]==True:
            from molmodmt.topology import is_water
            n_waters=0
            for residue in tmp_item.topology.residues():
                if is_water(residue.name): n_water+=1
            result.append(n_waters)
        if option=='n_ions' and kwargs[option]==True:
            from molmodmt.topology import is_ion
            n_ions=0
            for residue in tmp_item.topology.residues():
                if is_ion(residue.name): n_ions+=1
            result.append(n_ions)
        if option=='masses' and kwargs[option]==True:
            raise NotImplementedError
        if option=='charge' and kwargs[option]==True:
            from molmodmt.utils.openmm import get_net_charge
            result.append(get_net_charge(item, atom_indices))
        if option=='bonded_atoms' and kwargs[option]==True:
            raise NotImplementedError
        if option=='bonds' and kwargs[option]==True:
            raise NotImplementedError
        if option=='graph' and kwargs[option]==True:
            raise NotImplementedError
        if option=='molecules' and kwargs[option]==True:
            raise NotImplementedError
        if option=='molecule_type' and kwargs[option]==True:
            raise NotImplementedError
        if option=='residue_type' and kwargs[option]==True:
            raise NotImplementedError
        if option=='atom_type' and kwargs[option]==True:
            raise NotImplementedError
        if option=='coordinates' and kwargs[option]==True:
            result.append(item.getPositions())

    del(tmp_item)

    if len(result)==1:
        return result[0]
    else:
        return result

def select_with_mdtraj(item, selection):

    tmp_item = to_mdtraj_Topology(item)
    return tmp_item.select(selection)

def duplicate(item):

    from copy import deepcopy as _deepcopy
    return _deepcopy(item)

def get_total_n_atoms(item):
    return item.topology.getNumAtoms()

def extract_atom_indices(item, atom_indices):

    if len(atom_indices)==get_total_n_atoms(item):
        tmp_item=item
    else:
        from molmodmt.utils.atoms_list import complementary_atom_indices
        tmp_item = duplicate(item)
        atoms = list(tmp_item.topology.atoms())
        atoms_to_remove = [ atoms[ii] for ii in complementary_atom_indices(item, atom_indices) ]
        tmp_item.delete(atoms_to_remove)

    return tmp_item

def trim_atom_indices(item, atom_indices):

    atoms = list(item.topology.atoms())
    atoms_to_remove = [ atoms[ii] for ii in atom_indices ]
    return item.delete(atoms_to_remove)

def add(item, atoms):

    pass


def merge_two_items(item1, item2):

    from .api_mdtraj_Trajectory import to_openmm_Modeller as _from_mdtraj_Trajectory
    tmp_item1 = to_mdtraj(item1)
    tmp_item2 = to_mdtraj(item2)
    tmp_item = tmp_item1.stack(tmp_item2)
    tmp_item = _from_mdtraj_Trajectory(tmp_item)

    #from molmodmt import duplicate as _duplicate, get as _get
    #tmp_item = duplicate(item1)
    #topology2 = to_openmm_Topology(item2)
    #positions2 = _get(item2, coordinates=True)
    #tmp_item = tmp_item.add(topology2, positions2)

    return tmp_item
