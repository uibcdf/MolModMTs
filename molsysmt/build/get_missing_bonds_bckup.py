from molsysmt._private.digestion import digest
from molsysmt._private.exceptions import NotImplementedMethodError
from molsysmt._private.variables import is_all
import numpy as np
import warnings

_sorted=sorted

@digest()
def get_missing_bonds(molecular_system, threshold='2 angstroms', selection='all',
                      structure_indices=0, syntax='MolSysMT', engine='MolSysMT',
                      with_templates=True, with_distances=True, sorted=True, skip_digestion=False):
    """
    To be written soon...
    """

    if engine=="MolSysMT":

        from molsysmt._private.atom_indices import complementary_atom_indices
        from molsysmt.basic import get, select, get_form
        from molsysmt.structure import get_contacts
        from molsysmt.element.group.amino_acid import get_bonded_atom_pairs as _bonds_in_amino_acid
        from molsysmt.element.group.terminal_capping import get_bonded_atom_pairs as _bonds_in_terminal_capping
        from molsysmt.element.group.terminal_capping import is_n_terminal_capping, is_c_terminal_capping
        from molsysmt.element.group.small_molecule import get_bonded_atom_pairs as _bonds_in_small_molecule

        if is_all(selection):

            bonds = []
            bonds_templates = []
            bonds_distances = []

            n_atoms = get(molecular_system, n_atoms=True, skip_digestion=True)
            atoms_water = select(molecular_system, selection='group_type=="water"', skip_digestion=True)
            atoms_not_water = complementary_atom_indices(molecular_system, atoms_water)
            heavy_atoms_not_water = select(molecular_system, selection='atom_type!="H"', mask=atoms_not_water,
                                           skip_digestion=True)
            o_atoms_water = select(molecular_system, selection='atom_type!="H"', mask=atoms_water,
                                   skip_digestion=True)
            h_atoms_not_water = [ii for ii in atoms_not_water if ii not in heavy_atoms_not_water] 
            h_atoms_water = [ii for ii in atoms_water if ii not in o_atoms_water] 


            # bonds in water molecules are defined by template and independently
            if len(atoms_water):
                if len(h_atoms_water):
                    print('System with hydrogens and waters... to be implemented')
                    raise NotImplementedError()

                pass

            if with_distances:

                # Protein:
                # Enlace C-N: aproximadamente 1.33 Å
                # Enlace C-C: aproximadamente 1.54 Å
                # Enlace C-S: aproximadamente 1.82 Å
                # Small molecule:
                # Enlace C-H: aproximadamente 1.09 Å
                # Enlace C-C: aproximadamente 1.54 Å
                # Enlace C-O: aproximadamente 1.43 Å
                # Enlace C-N: aproximadamente 1.47 Å
                # Water molecule:
                # Enlace O-H: aproximadamente 0.96 Å
                # Lipid:
                # Enlace C-H: aproximadamente 1.09 Å
                # Enlace C-C: aproximadamente 1.54 Å
                # Enlace P-O: aproximadamente 1.61 Å

                contacts_heavy_atoms = get_contacts(molecular_system, selection=heavy_atoms_not_water,
                                                    threshold=threshold, output_type='pairs',
                                                    output_indices='atom', pbc=True, skip_digestion=True)

                bonds_distances += contacts_heavy_atoms[0]

                if len(h_atoms_not_water):

                    aux_contacts = get_contacts(molecular_system, selection=heavy_atoms_not_water,
                                                selection_2=h_atoms_not_water, threshold=threshold,
                                                output_type='pairs', output_indices='atom',
                                                pbc=True, skip_digestion=True)

                    # Hydrogen bonds need to be removed: let's work with those bonds intra group only.
                    contacts_heavy_atoms_with_h_atoms = []
                    group_indices = get(molecular_system, element='atom', group_index=True)
                    for ii,jj in aux_contacts[0]:
                        if group_indices[ii]==group_indices[jj]:
                            contacts_heavy_atoms_with_h_atoms.append([ii,jj])

                    bonds_distances += contacts_heavy_atoms_with_h_atoms

            if with_templates:

                aux_peptidic_bonds_C={}
                aux_peptidic_bonds_N={}

                form = get_form(molecular_system)

                if form in ['molsysmt.MolSys', 'molsysmt.Topology']:

                    if form == 'molsysmt.MolSys':
                        aux_item = molecular_system.topology
                    else:
                        aux_item = molecular_system

                    aux_output = [np.arange(aux_item.groups.shape[0]).tolist(),
                                  aux_item.groups.group_name.tolist(),
                                  aux_item.groups.group_type.tolist()]

                    former_group_index = -1

                    atom_indices = []
                    atom_names = []
                    atom_types = []

                    aux_atom_indices = []
                    aux_atom_names = []
                    aux_atom_types = []

                    for atom in aux_item.atoms.itertuples():
                        if former_group_index != atom.group_index:
                            if former_group_index != -1:
                                atom_indices.append(aux_atom_indices)
                                atom_names.append(aux_atom_names)
                                atom_types.append(aux_atom_types)
                                aux_atom_indices = []
                                aux_atom_names = []
                                aux_atom_types = []
                            former_group_index = atom.group_index
                        aux_atom_indices.append(atom.Index)
                        aux_atom_names.append(atom.atom_name)
                        aux_atom_types.append(atom.atom_type)

                    atom_indices.append(aux_atom_indices)
                    atom_names.append(aux_atom_names)
                    atom_types.append(aux_atom_types)

                    aux_output += [atom_indices, atom_names, atom_types]

                    del atom_indices, atom_names, atom_types, aux_atom_indices, aux_atom_names, aux_atom_types

                else:

                    aux_output = get(molecular_system, element='group', group_index=True, group_name=True,
                                     group_type=True, atom_index=True, atom_name=True, atom_type=True,
                                     skip_digestion=True)

                indices_no_template = []

                for group_index, group_name, group_type, atom_indices, atom_names, atom_types in zip(*aux_output):

                    if group_type=='water':

                        aux_bonds = _bonds_in_water(atom_indices, atom_names, atom_types, sorted=False)
                        bonds_templates += aux_bonds

                    elif group_type=='ion':

                        aux_bonds = _bonds_in_ion(group_name, atom_indices, atom_names, sorted=False)
                        bonds_templates += aux_bonds

                    elif group_type=='amino acid':

                        aux_bonds = _bonds_in_amino_acid(group_name, atom_names, atom_indices, sorted=False)
                        bonds_templates += aux_bonds

                        aux_peptidic_bonds_C[group_index]=atom_indices[atom_names.index('C')]
                        aux_peptidic_bonds_N[group_index]=atom_indices[atom_names.index('N')]

                    elif group_type=='terminal capping':

                        aux_bonds = _bonds_in_terminal_capping(group_name, atom_names, atom_indices, sorted=False)
                        bonds_templates += aux_bonds

                        if is_c_terminal_capping(group_name):
                            aux_peptidic_bonds_C[group_index]=atom_indices[atom_names.index('C')]
                        else:
                            aux_peptidic_bonds_N[group_index]=atom_indices[atom_names.index('N')]

                    elif group_type=='small molecule':

                        aux_bonds = _bonds_in_small_molecule(group_name, atom_names, atom_indices, sorted=False)
                        bonds_templates += aux_bonds

                    elif group_type=='saccharide':

                        raise NotImplementedError

                    elif group_type=='oligosaccharide':

                        raise NotImplementedError

                    elif group_type=='lipid':

                        raise NotImplementedError

                    elif group_type=='nucleotide':

                        raise NotImplementedError

                    else:

                        indices_no_template += atom_indices

                # peptidic bonds

                for group_index in aux_peptidic_bonds_C.keys():
                    if group_index+1 in aux_peptidic_bonds_N:
                        possible_bond = [aux_peptidic_bonds_C[group_index], aux_peptidic_bonds_N[group_index+1]]
                        if with_distances:
                            if possible_bond in bonds_distances:
                                bonds_templates += [[aux_peptidic_bonds_C[group_index],
                                                     aux_peptidic_bonds_N[group_index+1]]]

            else:

                raise NotImplementedError

            if with_distances and with_templates:

                distances_in_templates = True
                templates_in_distances = True

                for ii in bonds_distances:
                    if ii not in bonds_templates:
                        distances_in_templates = False
                        break

                for ii in bonds_distances:
                    if ii not in bonds_templates:
                        templates_in_distances = False
                        break

                if distances_in_templates and templates_in_distances:
                   output = bonds_distances
                else:
                    #raise ValueError('templates and distances do not match')
                    print('templates and distances do not match')
                    return bonds_distances, bonds_templates
            else:

                raise NotImplementedError
                

            if sorted:
                output = _sorted(output)
            else:
                output = bonds

            return output

        else:

            raise NotImplementedError


    elif engine=="pytraj":

        from molsysmt.basic import convert, get
        from os import remove
        from molsysmt._private.files_and_directories import temp_filename

        old_bonds = get(molecular_system, element='atom', selection=atom_indices, inner_bonded_atoms=True)

        for ii in range(old_bonds):
            if old_bonds[ii][0]>old_bonds[ii][1]:
                old_bonds[ii][0], old_bonds[ii][1] = old_bonds[ii][1], old_bonds[ii][0]


        temp_pdb_file = temp_filename(extension='pdb')
        temp_molecular_system = convert(molecular_system, to_form=temp_pdb_file)
        temp_molecular_system = convert(temp_molecular_system, to_form="pytraj.Topology", threshold=threshold)

        new_bonds = get(molecular_system, element='atom', selection=atom_indices, inner_bonded_atoms=True)

        for ii in range(old_bonds):
            if old_bonds[ii][0]>old_bonds[ii][1]:
                old_bonds[ii][0], old_bonds[ii][1] = old_bonds[ii][1], old_bonds[ii][0]

        for bond in new_bonds:
            if bond not in old_bonds:
                output.append(bond)

    else:

        raise NotImplementedMethodError

    return output

def _bonds_in_water(atom_indices, atom_names, atom_types, sorted=True):

    if len(atom_indices)>=3:

        O = None
        Hs = []

        for ii,jj in zip(atom_indices, atom_types):
            if jj=='O':
                O=ii
            else:
                Hs.append(ii)

        if sorted:
            return  sorted([[O,Hs[0]], [O,Hs[1]]])
        else:
            return  [[O,Hs[0]], [O,Hs[1]]]

    else:

        return []

def _bonds_in_ion(group_name, atom_indices, atom_names, sorted=True):

    n_atoms=len(atom_indices)

    if n_atoms==1:

        return []

    elif n_atoms==2:

        return [atom_indices]
    
    else:

        raise NotImplementedError

#                        if aux_bonds is None and with_distances:
#
#                            aux_bonds_unk_atoms = []
#
#                            neighbors, _ = get_neighbors(molecular_system, selection=atom_indices,
#                                                         selection_2=atom_indices, structure_indices=structure_indices,
#                                                         threshold=threshold, skip_digestion=True)
#                            for ii, nn in zip(atom_indices, neighbors[0]):
#                                mm = atom_indices.index(ii)
#                                ii_type = atom_types[mm]
#                                if ii_type == 'H':
#                                    for jj in nn:
#                                        if ii!=atom_indices[jj] and atom_types[jj]!='H':
#                                            iii = ii
#                                            jjj = atom_indices[jj]
#                                            if iii<jjj:
#                                                aux_bonds_unk_atoms.append([iii,jjj])
#                                            else:
#                                                aux_bonds_unk_atoms.append([jjj,iii])
#                                else:
#                                    for jj in nn:
#                                        if ii!=atom_indices[jj]:
#                                            iii = ii
#                                            jjj = atom_indices[jj]
#                                            if iii<jjj:
#                                                aux_bonds_unk_atoms.append([iii,jjj])
#                                            else:
#                                                aux_bonds_unk_atoms.append([jjj,iii])
#                            bonds_distances += aux_bonds_unk_atoms


