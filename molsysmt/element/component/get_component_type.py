from molsysmt._private.digestion import digest
import numpy as np


@digest()
def get_component_type(molecular_system, element='atom', selection='all', redefine_indices=False,
                       redefine_types=False, syntax='MolSysMT', skip_digestion=False):

    from molsysmt.basic import get

    if redefine_indices or redefine_types:

        from molsysmt.basic import select
        from .get_component_index import get_component_index

        if redefine_indices:

            atom_indices = select(molecular_system, element=element, selection=selection,
                                  syntax=syntax, skip_digestion=True, atom_indices=True)

            if element!='atom':
                aux_atom_indices = []
                for aux in atom_indices:
                    aux_atom_indices += aux
                atom_indices = aux_atom_indices

            component_indices = get_component_index(molecular_system, element='atom',
                                                    selection='all', redefine_indices=redefine_indices,
                                                    skip_digestion=True)

            unique_component_indices, first_atoms, n_atoms = np.unique(component_indices, return_index=True,
                                                                      return_count=True)

            component_types={}

            for component_index, first_atom, aux_n_atoms in zip(unique_component_indices, first_atoms, n_atoms):

                atom_indices_component = list(arange(aux_n_atoms))+first_atom
                aux_group_names, aux_group_types = get(molecular_system, element='group',
                                                       selection='atom_indices in @atom_indices_component',
                                                       syntax='molsysmt.MolSys', skip_digestion=True)


        else:

            component_indices = get_component_index(molecular_system, element=element,
                                                    selection=selection, redefine_indices=redefine_indices,
                                                    skip_digestion=True)

            unique_component_indices = np.unique(component_indices)

            group_names_from_component, group_types_from_component = get(molecular_system, element='component',
                                                                         selection=unique_component_indices,
                                                                         group_name=True, group_type=True,
                                                                         skip_digestion=True)


        component_types = []
        component_type_per_atom = []

        _, n_atoms_per_component = np.unique(component_indices, return_counts=True)
        _, first_atom_per_group = np.unique(group_indices, return_index=True)

        kk=0
        for n_atoms in n_atoms_per_component:
            ll = kk+n_atoms-1
            first_group_name = group_names[kk]
            first_group_type = group_types[kk]
            last_group_type = group_types[ll]
            n_groups = group_indices[ll]-group_indices[kk]+1
            component_type = _get_component_type(first_group_name, first_group_type, last_group_type, n_groups)
            component_type_per_atom += [component_type]*n_atoms
            component_types.append(component_type)
            kk=ll

        component_types = np.array(component_types, dtype=object)
        component_type_per_atom = np.array(component_type_per_atom, dtype=object)

        if element == 'atom':
            output = component_type_per_atom
        elif element == 'group':
            output = component_type_per_atom[first_atom_per_group]
        elif element == 'component':
            output = component_types
        else:
            raise NotImplementedError

        del atom_indices, group_indices, group_names, group_types, n_atoms_per_component
        del component_indices, component_type_per_atom, component_types

    else:

        from molsysmt.basic import get
        output = get(molecular_system, element=element, selection=selection, syntax=syntax,
                     component_type=True, skip_digestion=True)

    return output


def _get_component_type(first_group_name, first_group_type, last_group_type, n_groups):

    from molsysmt.config import min_length_protein

    if first_group_type in ['water', 'ion', 'small molecule', 'lipid']:
        tmp_type = first_group_type
    elif (first_group_type == 'amino acid') or (first_group_type == 'terminal capping'):
        if first_group_type == 'terminal capping':
            n_groups -= 1
        if last_group_type == 'terminal capping':
            n_groups -= 1
        if n_groups >= min_length_protein:
            tmp_type = 'protein'
        else:
            tmp_type = 'peptide'
    elif first_group_type == 'nucleotide':
        if first_group_name in rna_names:
            tmp_type = 'rna'
        elif first_group_name in dna_names:
            tmp_type = 'dna'
    else:
        tmp_type = 'unknown'

    return tmp_type
def _get_component_type_from_group_names_and_types(group_names, group_types):

    from molsysmt.config import min_length_protein

    n_groups = len(group_types)
    first_group_type = group_types[0]
    last_group_type = group_types[-1]
    first_group_name = group_names[0]

    return _get_component_type(first_group_name, first_group_type, last_group_type, n_groups)
