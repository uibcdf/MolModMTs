from molsysmt._private.digestion import digest
from molsysmt._private.variables import is_all
from molsysmt import pyunitwizard as puw
import numpy as np
from molsysmt._private.get import _auxiliary_getter

form = 'molsysmt.TopologyNEW'


#######################################################################
#                 To be customized for each form                      #
#######################################################################

# From atom


@digest(form=form)
def get_atom_id_from_atom(item, indices='all'):

    if is_all(indices):
        output = item.atoms['id'].to_list()
    else:
        output = item.atoms['id'][indices].to_list()

    return output


@digest(form=form)
def get_atom_name_from_atom(item, indices='all'):

    if is_all(indices):
        output = item.atoms['name'].to_list()
    else:
        output = item.atoms['name'][indices].to_list()

    return output


@digest(form=form)
def get_atom_type_from_atom(item, indices='all'):

    if is_all(indices):
        output = item.atoms['type'].to_list()
    else:
        output = item.atoms['type'][indices].to_list()

    return output


@digest(form=form)
def get_group_index_from_atom(item, indices='all'):

    if is_all(indices):
        output = item.atoms['group_index'].to_list()
    else:
        output = item.atoms['group_index'][indices].to_list()

    return output


@digest(form=form)
def get_component_index_from_atom(item, indices='all'):

    group_indices = get_group_index_from_atom(item, indices=indices)
    output = item.groups['component_index'][group_indices].to_list()
    del group_indices

    return output


@digest(form=form)
def get_molecule_index_from_atom(item, indices='all'):

    component_indices = get_component_index_from_atom(item, indices=indices)
    output = item.components['molecule_index'][component_indices].to_list()
    del component_indices

    return output


@digest(form=form)
def get_entity_index_from_atom(item, indices='all'):

    molecule_indices = get_molecule_index_from_atom(item, indices=indices)
    output = item.molecules['entity_index'][molecule_indices].to_list()
    del molecule_indices

    return output


@digest(form=form)
def get_chain_index_from_atom(item, indices='all'):

    if is_all(indices):
        output = item.atoms['chain_index'][:].to_numpy()
    else:
        output = item.atoms['chain_index'][indices].to_list()

    return output


@digest(form=form)
def get_occupancy_from_atom(item, indices='all'):

    tmp_indices = get_atom_index_from_atom(item, indices=indices)
    output = item.atoms['occupancy'][tmp_indices].to_list()
    return output


@digest(form=form)
def get_alternate_location_from_atom(item, indices='all'):

    tmp_indices = get_atom_index_from_atom(item, indices=indices)
    output = item.atoms['alternate_location'][tmp_indices].to_list()
    return output


@digest(form=form)
def get_b_factor_from_atom(item, indices='all'):

    tmp_indices = get_atom_index_from_atom(item, indices=indices)
    output = item.atoms['b_factor'][tmp_indices].to_list()
    unit = puw.get_standard_units(dimensionality={'[L]':2})
    output = puw.quantity(output, unit, standardized=True)
    return output


@digest(form=form)
def get_formal_charge_from_atom(item, indices='all'):

    tmp_indices = get_atom_index_from_atom(item, indices=indices)
    output = item.atoms['formal_charge'][tmp_indices].to_list()
    unit = puw.get_standard_units(dimensionality={'[T]':1, '[A]':1})
    output = puw.quantity(output, unit, standardized=True)
    return output


@digest(form=form)
def get_partial_charge_from_atom(item, indices='all'):

    tmp_indices = get_atom_index_from_atom(item, indices=indices)
    output = item.atoms['partial_charge'][tmp_indices].to_list()
    unit = puw.get_standard_units(dimensionality={'[T]':1, '[A]':1})
    output = puw.quantity(output, unit, standardized=True)
    return output


# group

@digest(form=form)
def get_group_id_from_group(item, indices='all'):

    if is_all(indices):
        output = item.groups['group_id'].to_list()
    else:
        output = item.groups['group_id'][indices].to_list()

    return output


@digest(form=form)
def get_group_name_from_group(item, indices='all'):

    if is_all(indices):
        output = item.groups['group_name'].to_list()
    else:
        output = item.groups['group_name'][indices].to_list()

    return output


@digest(form=form)
def get_group_type_from_group(item, indices='all'):

    if is_all(indices):
        output = item.groups['group_type'].to_list()
    else:
        output = item.groups['group_type'][indices].to_list()

    return output

## component

@digest(form=form)
def get_component_id_from_component(item, indices='all'):

    if is_all(indices):
        output = item.components['component_id'].to_list()
    else:
        output = item.components['component_id'][indices].to_list()

    return output

@digest(form=form)
def get_component_name_from_component(item, indices='all'):

    if is_all(indices):
        output = item.components['component_name'].to_list()
    else:
        output = item.components['component_name'][indices].to_list()

    return output

@digest(form=form)
def get_component_type_from_component(item, indices='all'):

    if is_all(indices):
        output = item.components['component_type'].to_list()
    else:
        output = item.components['component_type'][indices].to_list()

    return output


## molecule

@digest(form=form)
def get_molecule_id_from_molecule(item, indices='all'):

    if is_all(indices):
        output = item.molecules['molecule_id'].to_list()
    else:
        output = item.molecules['molecule_id'][indices].to_list()

    return output

@digest(form=form)
def get_molecule_name_from_molecule(item, indices='all'):

    if is_all(indices):
        output = item.molecules['molecule_name'].to_list()
    else:
        output = item.molecules['molecule_name'][indices].to_list()

    return output

@digest(form=form)
def get_molecule_type_from_molecule(item, indices='all'):

    if is_all(indices):
        output = item.molecules['molecule_type'].to_list()
    else:
        output = item.molecules['molecule_type'][indices].to_list()

    return output

## chain

@digest(form=form)
def get_chain_id_from_chain(item, indices='all'):

    if is_all(indices):
        output = item.chains['chain_id'].to_list()
    else:
        output = item.chains['chain_id'][indices].to_list()

    return output

@digest(form=form)
def get_chain_name_from_chain(item, indices='all'):

    if is_all(indices):
        output = item.chains['chain_name'].to_list()
    else:
        output = item.chains['chain_name'][indices].to_list()

    return output

@digest(form=form)
def get_chain_type_from_chain(item, indices='all'):

    if is_all(indices):
        output = item.chains['chain_type'].to_list()
    else:
        output = item.chains['chain_type'][indices].to_list()

    return output


## entity

@digest(form=form)
def get_entity_id_from_entity(item, indices='all'):

    if is_all(indices):
        output = item.entities['entity_id'].to_list()
    else:
        output = item.entities['entity_id'][indices].to_list()

    return output

@digest(form=form)
def get_entity_name_from_entity(item, indices='all'):

    if is_all(indices):
        output = item.entities['entity_name'].to_list()
    else:
        output = item.entities['entity_name'][indices].to_list()

    return output

@digest(form=form)
def get_entity_type_from_entity(item, indices='all'):

    if is_all(indices):
        output = item.entities['entity_name'].to_list()
    else:
        output = item.entities['entity_name'][indices].to_list()

    return output


## system

@digest(form=form)
def get_n_atoms_from_system(item):

    return item.atoms.shape[0]

@digest(form=form)
def get_n_groups_from_system(item):

    return item.groups.shape[0]

@digest(form=form)
def get_n_components_from_system(item):

    return item.components.shape[0]

@digest(form=form)
def get_n_chains_from_system(item):

    return item.chains.shape[0]

@digest(form=form)
def get_n_molecules_from_system(item):

    return item.molecules.shape[0]

@digest(form=form)
def get_n_entities_from_system(item):

    return item.entities.shape[0]

@digest(form=form)
def get_n_bonds_from_system(item):

    return item.bonds.shape[0]


## bond


@digest(form=form)
def get_bond_order_from_bond(item, indices='all'):

    if is_all(indices):
        output = item.bonds['order'].to_list()
    else:
        output = item.bonds['order'][indices].to_list()

    return output

@digest(form=form)
def get_bond_type_from_bond(item, indices='all'):

    if is_all(indices):
        output = item.bonds['order'].to_list()
    else:
        output = item.bonds['order'][indices].to_list()

    return output

@digest(form=form)
def get_bonded_atoms_from_bond(item, indices='all'):

    if is_all(indices):

        atom1_index = item.bonds['atom1_index'].to_numpy()
        atom2_index = item.bonds['atom2_index'].to_numpy()

    else:

        atom1_index = item.bonds['atom1_index'][indices].to_numpy()
        atom2_index = item.bonds['atom2_index'][indices].to_numpy()

    tmp_out = np.array([atom1_index, atom2_index])
    tmp_out = np.sort(tmp_out)

    return tmp_out


#######################################################################
#             Assisted by the auxiliary getter function               #
#######################################################################


# From atom

@digest(form=form)
def get_atom_index_from_atom(item, indices='all'):

    return _auxiliary_getter(get_atom_index_from_atom, item, indices)


@digest(form=form)
def get_group_id_from_atom(item, indices='all'):

    return _auxiliary_getter(get_group_id_from_atom, item, indices)


@digest(form=form)
def get_group_name_from_atom(item, indices='all'):

    return _auxiliary_getter(get_group_name_from_atom, item, indices)


@digest(form=form)
def get_group_type_from_atom(item, indices='all'):

    return _auxiliary_getter(get_group_type_from_atom, item, indices)


@digest(form=form)
def get_component_id_from_atom(item, indices='all'):

    return _auxiliary_getter(get_component_id_from_atom, item, indices)


@digest(form=form)
def get_component_name_from_atom(item, indices='all'):

    return _auxiliary_getter(get_component_name_from_atom, item, indices)


@digest(form=form)
def get_component_type_from_atom(item, indices='all'):

    return _auxiliary_getter(get_component_type_from_atom, item, indices)


@digest(form=form)
def get_molecule_id_from_atom(item, indices='all'):

    return _auxiliary_getter(get_molecule_id_from_atom, item, indices)


@digest(form=form)
def get_molecule_name_from_atom(item, indices='all'):

    return _auxiliary_getter(get_molecule_name_from_atom, item, indices)


@digest(form=form)
def get_molecule_type_from_atom(item, indices='all'):

    return _auxiliary_getter(get_molecule_type_from_atom, item, indices)


@digest(form=form)
def get_entity_id_from_atom(item, indices='all'):

    return _auxiliary_getter(get_entity_id_from_atom, item, indices)


@digest(form=form)
def get_entity_name_from_atom(item, indices='all'):

    return _auxiliary_getter(get_entity_name_from_atom, item, indices)


@digest(form=form)
def get_entity_type_from_atom(item, indices='all'):

    return _auxiliary_getter(get_entity_type_from_atom, item, indices)


@digest(form=form)
def get_chain_id_from_atom(item, indices='all'):

    return _auxiliary_getter(get_chain_id_from_atom, item, indices)


@digest(form=form)
def get_chain_name_from_atom(item, indices='all'):

    return _auxiliary_getter(get_chain_name_from_atom, item, indices)


@digest(form=form)
def get_chain_type_from_atom(item, indices='all'):

    return _auxiliary_getter(get_chain_type_from_atom, item, indices)


@digest(form=form)
def get_bond_index_from_atom(item, indices='all'):

    return _auxiliary_getter(get_bond_index_from_atom, item, indices)


@digest(form=form)
def get_bond_type_from_atom(item, indices='all'):

    raise NotImplementedError


@digest(form=form)
def get_bond_order_from_atom(item, indices='all'):

    raise NotImplementedError


@digest(form=form)
def get_bonded_atoms_from_atom(item, indices='all'):

    return _auxiliary_getter(get_bonded_atoms_from_atom, item, indices)


@digest(form=form)
def get_inner_bond_index_from_atom(item, indices='all'):

    output = None

    if is_all(indices):
        output = get_bond_index_from_bond(item)
    else:
        aux_list = list(indices)
        output = item.bonds.query('atom1_index==@aux_list and atom2_index==@aux_list').index.to_numpy(dtype=int, copy=True)
        output = output.to_list()

    return output


@digest(form=form)
def get_inner_bonded_atoms_from_atom(item, indices='all'):

    return _auxiliary_getter(get_inner_bonded_atoms_from_atom, item, indices)


@digest(form=form)
def get_n_atoms_from_atom(item, indices='all'):

    return _auxiliary_getter(get_n_atoms_from_atom, item, indices)


@digest(form=form)
def get_n_groups_from_atom(item, indices='all'):

    return _auxiliary_getter(get_n_groups_from_atom, item, indices)


@digest(form=form)
def get_n_components_from_atom(item, indices='all'):

    return _auxiliary_getter(get_n_components_from_atom, item, indices)


@digest(form=form)
def get_n_molecules_from_atom(item, indices='all'):

    return _auxiliary_getter(get_n_molecules_from_atom, item, indices)


@digest(form=form)
def get_n_chains_from_atom(item, indices='all'):

    return _auxiliary_getter(get_n_chains_from_atom, item, indices)


@digest(form=form)
def get_n_entities_from_atom(item, indices='all'):

    return _auxiliary_getter(get_n_entities_from_atom, item, indices)


@digest(form=form)
def get_n_bonds_from_atom(item, indices='all'):

    return _auxiliary_getter(get_n_bonds_from_atom, item, indices)


@digest(form=form)
def get_n_inner_bonds_from_atom(item, indices='all'):

    return _auxiliary_getter(get_n_inner_bonds_from_atom, item, indices)


@digest(form=form)
def get_n_aminoacids_from_atom(item, indices='all'):

    return _auxiliary_getter(get_n_aminoacids_from_atom, item, indices)


@digest(form=form)
def get_n_nucleotides_from_atom(item, indices='all'):

    return _auxiliary_getter(get_n_nucleotides_from_atom, item, indices)


@digest(form=form)
def get_n_ions_from_atom(item, indices='all'):

    return _auxiliary_getter(get_n_ions_from_atom, item, indices)


@digest(form=form)
def get_n_waters_from_atom(item, indices='all'):

    return _auxiliary_getter(get_n_waters_from_atom, item, indices)


@digest(form=form)
def get_n_small_molecules_from_atom(item, indices='all'):

    return _auxiliary_getter(get_n_small_molecules_from_atom, item, indices)


@digest(form=form)
def get_n_peptides_from_atom(item, indices='all'):

    return _auxiliary_getter(get_n_peptides_from_atom, item, indices)


@digest(form=form)
def get_n_proteins_from_atom(item, indices='all'):

    return _auxiliary_getter(get_n_proteins_from_atom, item, indices)


@digest(form=form)
def get_n_dnas_from_atom(item, indices='all'):

    return _auxiliary_getter(get_n_dnas_from_atom, item, indices)


@digest(form=form)
def get_n_rnas_from_atom(item, indices='all'):

    return _auxiliary_getter(get_n_rnas_from_atom, item, indices)


@digest(form=form)
def get_n_lipids_from_atom(item, indices='all'):

    return _auxiliary_getter(get_n_lipids_from_atom, item, indices)


@digest(form=form)
def get_n_oligosaccharides_from_atom(item, indices='all'):

    return _auxiliary_getter(get_n_oligosaccharides_from_atom, item, indices)


@digest(form=form)
def get_n_saccharides_from_atom(item, indices='all'):

    return _auxiliary_getter(get_n_saccharides_from_atom, item, indices)


# From group


@digest(form=form)
def get_atom_index_from_group(item, indices='all'):

    return _auxiliary_getter(get_atom_index_from_group, item, indices)


@digest(form=form)
def get_atom_id_from_group(item, indices='all'):

    return _auxiliary_getter(get_atom_id_from_group, item, indices)


@digest(form=form)
def get_atom_name_from_group(item, indices='all'):

    return _auxiliary_getter(get_atom_name_from_group, item, indices)


@digest(form=form)
def get_atom_type_from_group(item, indices='all'):

    return _auxiliary_getter(get_atom_type_from_group, item, indices)


@digest(form=form)
def get_group_index_from_group(item, indices='all'):

    return _auxiliary_getter(get_group_index_from_group, item, indices)


@digest(form=form)
def get_component_index_from_group(item, indices='all'):

    return _auxiliary_getter(get_component_index_from_group, item, indices)


@digest(form=form)
def get_component_id_from_group(item, indices='all'):

    return _auxiliary_getter(get_component_id_from_group, item, indices)


@digest(form=form)
def get_component_name_from_group(item, indices='all'):

    return _auxiliary_getter(get_component_name_from_group, item, indices)


@digest(form=form)
def get_component_type_from_group(item, indices='all'):

    return _auxiliary_getter(get_component_type_from_group, item, indices)


@digest(form=form)
def get_chain_index_from_group(item, indices='all'):

    return _auxiliary_getter(get_chain_index_from_group, item, indices)


@digest(form=form)
def get_chain_id_from_group(item, indices='all'):

    return _auxiliary_getter(get_chain_id_from_group, item, indices)


@digest(form=form)
def get_chain_name_from_group(item, indices='all'):

    return _auxiliary_getter(get_chain_name_from_group, item, indices)


@digest(form=form)
def get_chain_type_from_group(item, indices='all'):

    return _auxiliary_getter(get_chain_type_from_group, item, indices)


@digest(form=form)
def get_molecule_index_from_group(item, indices='all'):

    return _auxiliary_getter(get_molecule_index_from_group, item, indices)


@digest(form=form)
def get_molecule_id_from_group(item, indices='all'):

    return _auxiliary_getter(get_molecule_id_from_group, item, indices)


@digest(form=form)
def get_molecule_name_from_group(item, indices='all'):

    return _auxiliary_getter(get_molecule_name_from_group, item, indices)


@digest(form=form)
def get_molecule_type_from_group(item, indices='all'):

    return _auxiliary_getter(get_molecule_type_from_group, item, indices)


@digest(form=form)
def get_entity_index_from_group(item, indices='all'):

    return _auxiliary_getter(get_entity_index_from_group, item, indices)


@digest(form=form)
def get_entity_id_from_group(item, indices='all'):

    return _auxiliary_getter(get_entity_id_from_group, item, indices)


@digest(form=form)
def get_entity_name_from_group(item, indices='all'):

    return _auxiliary_getter(get_entity_name_from_group, item, indices)


@digest(form=form)
def get_entity_type_from_group(item, indices='all'):

    return _auxiliary_getter(get_entity_type_from_group, item, indices)


@digest(form=form)
def get_n_atoms_from_group(item, indices='all'):

    return _auxiliary_getter(get_n_atoms_from_group, item, indices)


@digest(form=form)
def get_n_groups_from_group(item, indices='all'):

    return _auxiliary_getter(get_n_groups_from_group, item, indices)


@digest(form=form)
def get_n_components_from_group(item, indices='all'):

    return _auxiliary_getter(get_n_components_from_group, item, indices)


@digest(form=form)
def get_n_molecules_from_group(item, indices='all'):

    return _auxiliary_getter(get_n_molecules_from_group, item, indices)


@digest(form=form)
def get_n_chains_from_group(item, indices='all'):

    return _auxiliary_getter(get_n_chains_from_group, item, indices)


@digest(form=form)
def get_n_entities_from_group(item, indices='all'):

    return _auxiliary_getter(get_n_entities_from_group, item, indices)


# From component


@digest(form=form)
def get_atom_index_from_component(item, indices='all'):

    return _auxiliary_getter(get_atom_index_from_component, item, indices)


@digest(form=form)
def get_atom_id_from_component(item, indices='all'):

    return _auxiliary_getter(get_atom_id_from_component, item, indices)


@digest(form=form)
def get_atom_name_from_component(item, indices='all'):

    return _auxiliary_getter(get_atom_name_from_component, item, indices)


@digest(form=form)
def get_atom_type_from_component(item, indices='all'):

    return _auxiliary_getter(get_atom_type_from_component, item, indices)


@digest(form=form)
def get_group_index_from_component(item, indices='all'):

    return _auxiliary_getter(get_group_index_from_component, item, indices)


@digest(form=form)
def get_group_id_from_component(item, indices='all'):

    return _auxiliary_getter(get_group_id_from_component, item, indices)


@digest(form=form)
def get_group_name_from_component(item, indices='all'):

    return _auxiliary_getter(get_group_name_from_component, item, indices)


@digest(form=form)
def get_group_type_from_component(item, indices='all'):

    return _auxiliary_getter(get_group_type_from_component, item, indices)


@digest(form=form)
def get_component_index_from_component(item, indices='all'):

    return _auxiliary_getter(get_component_index_from_component, item, indices)


@digest(form=form)
def get_chain_index_from_component(item, indices='all'):

    return _auxiliary_getter(get_chain_index_from_component, item, indices)


@digest(form=form)
def get_chain_id_from_component(item, indices='all'):

    return _auxiliary_getter(get_chain_id_from_component, item, indices)


@digest(form=form)
def get_chain_name_from_component(item, indices='all'):

    return _auxiliary_getter(get_chain_name_from_component, item, indices)


@digest(form=form)
def get_chain_type_from_component(item, indices='all'):

    return _auxiliary_getter(get_chain_type_from_component, item, indices)


@digest(form=form)
def get_molecule_index_from_component(item, indices='all'):

    return _auxiliary_getter(get_molecule_index_from_component, item, indices)


@digest(form=form)
def get_molecule_id_from_component(item, indices='all'):

    return _auxiliary_getter(get_molecule_id_from_component, item, indices)


@digest(form=form)
def get_molecule_name_from_component(item, indices='all'):

    return _auxiliary_getter(get_molecule_name_from_component, item, indices)


@digest(form=form)
def get_molecule_type_from_component(item, indices='all'):

    return _auxiliary_getter(get_molecule_type_from_component, item, indices)


@digest(form=form)
def get_entity_index_from_component(item, indices='all'):

    return _auxiliary_getter(get_entity_index_from_component, item, indices)


@digest(form=form)
def get_entity_id_from_component(item, indices='all'):

    return _auxiliary_getter(get_entity_id_from_component, item, indices)


@digest(form=form)
def get_entity_name_from_component(item, indices='all'):

    return _auxiliary_getter(get_entity_name_from_component, item, indices)


@digest(form=form)
def get_entity_type_from_component(item, indices='all'):

    return _auxiliary_getter(get_entity_type_from_component, item, indices)


@digest(form=form)
def get_n_atoms_from_component(item, indices='all'):

    return _auxiliary_getter(get_n_atoms_from_component, item, indices)


@digest(form=form)
def get_n_groups_from_component(item, indices='all'):

    return _auxiliary_getter(get_n_groups_from_component, item, indices)


@digest(form=form)
def get_n_components_from_component(item, indices='all'):

    return _auxiliary_getter(get_n_components_from_component, item, indices)


@digest(form=form)
def get_n_molecules_from_component(item, indices='all'):

    return _auxiliary_getter(get_n_molecules_from_component, item, indices)


@digest(form=form)
def get_n_chains_from_component(item, indices='all'):

    return _auxiliary_getter(get_n_chains_from_component, item, indices)


@digest(form=form)
def get_n_entities_from_component(item, indices='all'):

    return _auxiliary_getter(get_n_entities_from_component, item, indices)


@digest(form=form)
def get_n_bonds_from_component(item, indices='all'):

    return _auxiliary_getter(get_n_bonds_from_component, item, indices)


@digest(form=form)
def get_n_inner_bonds_from_component(item, indices='all'):

    return _auxiliary_getter(get_n_inner_bonds_from_component, item, indices)


@digest(form=form)
def get_formal_charge_from_component(item, indices='all'):

    return _auxiliary_getter(get_formal_charge_from_component, item, indices)


@digest(form=form)
def get_partial_charge_from_group(item, indices='all'):

    return _auxiliary_getter(get_partial_charge_from_component, item, indices)


@digest(form=form)
def get_n_aminoacids_from_component(item, indices='all'):

    return _auxiliary_getter(get_n_aminoacids_from_component, item, indices)


@digest(form=form)
def get_n_nucleotides_from_component(item, indices='all'):

    return _auxiliary_getter(get_n_nucleotides_from_component, item, indices)


@digest(form=form)
def get_n_ions_from_component(item, indices='all'):

    return _auxiliary_getter(get_n_ions_from_component, item, indices)


@digest(form=form)
def get_n_waters_from_component(item, indices='all'):

    return _auxiliary_getter(get_n_waters_from_component, item, indices)


@digest(form=form)
def get_n_small_molecules_from_component(item, indices='all'):

    return _auxiliary_getter(get_n_small_molecules_from_component, item, indices)


@digest(form=form)
def get_n_peptides_from_component(item, indices='all'):

    return _auxiliary_getter(get_n_peptides_from_component, item, indices)


@digest(form=form)
def get_n_proteins_from_component(item, indices='all'):

    return _auxiliary_getter(get_n_proteins_from_component, item, indices)


@digest(form=form)
def get_n_dnas_from_component(item, indices='all'):

    return _auxiliary_getter(get_n_dnas_from_component, item, indices)


@digest(form=form)
def get_n_rnas_from_component(item, indices='all'):

    return _auxiliary_getter(get_n_rnas_from_component, item, indices)


@digest(form=form)
def get_n_lipids_from_component(item, indices='all'):

    return _auxiliary_getter(get_n_lipids_from_component, item, indices)


@digest(form=form)
def get_n_oligosaccharides_from_component(item, indices='all'):

    return _auxiliary_getter(get_n_oligosaccharides_from_component, item, indices)


@digest(form=form)
def get_n_saccharides_from_component(item, indices='all'):

    return _auxiliary_getter(get_n_saccharides_from_component, item, indices)



## molecule

@digest(form=form)
def get_atom_index_from_molecule(item, indices='all'):

    return _auxiliary_getter(get_atom_index_from_molecule, item, indices)


@digest(form=form)
def get_atom_id_from_molecule(item, indices='all'):

    return _auxiliary_getter(get_atom_id_from_molecule, item, indices)


@digest(form=form)
def get_atom_name_from_molecule(item, indices='all'):

    return _auxiliary_getter(get_atom_name_from_molecule, item, indices)


@digest(form=form)
def get_atom_type_from_molecule(item, indices='all'):

    return _auxiliary_getter(get_atom_type_from_molecule, item, indices)


@digest(form=form)
def get_group_index_from_molecule(item, indices='all'):

    return _auxiliary_getter(get_group_index_from_molecule, item, indices)


@digest(form=form)
def get_group_id_from_molecule(item, indices='all'):

    return _auxiliary_getter(get_group_id_from_molecule, item, indices)


@digest(form=form)
def get_group_name_from_molecule(item, indices='all'):

    return _auxiliary_getter(get_group_name_from_molecule, item, indices)


@digest(form=form)
def get_group_type_from_molecule(item, indices='all'):

    return _auxiliary_getter(get_group_type_from_molecule, item, indices)


@digest(form=form)
def get_component_index_from_molecule(item, indices='all'):

    return _auxiliary_getter(get_component_index_from_molecule, item, indices)


@digest(form=form)
def get_component_id_from_molecule(item, indices='all'):

    return _auxiliary_getter(get_component_id_from_molecule, item, indices)


@digest(form=form)
def get_component_name_from_molecule(item, indices='all'):

    return _auxiliary_getter(get_component_name_from_molecule, item, indices)


@digest(form=form)
def get_component_type_from_molecule(item, indices='all'):

    return _auxiliary_getter(get_component_type_from_molecule, item, indices)


@digest(form=form)
def get_chain_index_from_molecule(item, indices='all'):

    return _auxiliary_getter(get_chain_index_from_molecule, item, indices)


@digest(form=form)
def get_chain_id_from_molecule(item, indices='all'):

    return _auxiliary_getter(get_chain_id_from_molecule, item, indices)


@digest(form=form)
def get_chain_name_from_molecule(item, indices='all'):

    return _auxiliary_getter(get_chain_name_from_molecule, item, indices)


@digest(form=form)
def get_chain_type_from_molecule(item, indices='all'):

    return _auxiliary_getter(get_chain_type_from_molecule, item, indices)


@digest(form=form)
def get_molecule_index_from_molecule(item, indices='all'):

    return _auxiliary_getter(get_molecule_index_from_molecule, item, indices)


@digest(form=form)
def get_entity_index_from_molecule(item, indices='all'):

    return _auxiliary_getter(get_entity_index_from_molecule, item, indices)


@digest(form=form)
def get_entity_id_from_molecule(item, indices='all'):

    return _auxiliary_getter(get_entity_id_from_molecule, item, indices)


@digest(form=form)
def get_entity_name_from_molecule(item, indices='all'):

    return _auxiliary_getter(get_entity_name_from_molecule, item, indices)


@digest(form=form)
def get_entity_type_from_molecule(item, indices='all'):

    return _auxiliary_getter(get_entity_type_from_molecule, item, indices)


@digest(form=form)
def get_n_atoms_from_molecule(item, indices='all'):

    return _auxiliary_getter(get_n_atoms_from_molecule, item, indices)


@digest(form=form)
def get_n_groups_from_molecule(item, indices='all'):

    return _auxiliary_getter(get_n_groups_from_molecule, item, indices)


@digest(form=form)
def get_n_components_from_molecule(item, indices='all'):

    return _auxiliary_getter(get_n_components_from_molecule, item, indices)


@digest(form=form)
def get_n_molecules_from_molecule(item, indices='all'):

    return _auxiliary_getter(get_n_molecules_from_molecule, item, indices)


@digest(form=form)
def get_n_chains_from_molecule(item, indices='all'):

    return _auxiliary_getter(get_n_chains_from_molecule, item, indices)


@digest(form=form)
def get_n_entities_from_molecule(item, indices='all'):

    return _auxiliary_getter(get_n_entities_from_molecule, item, indices)


@digest(form=form)
def get_n_bonds_from_molecule(item, indices='all'):

    return _auxiliary_getter(get_n_bonds_from_molecule, item, indices)


@digest(form=form)
def get_n_inner_bonds_from_molecule(item, indices='all'):

    return _auxiliary_getter(get_n_inner_bonds_from_molecule, item, indices)


@digest(form=form)
def get_formal_charge_from_molecule(item, indices='all'):

    return _auxiliary_getter(get_formal_charge_from_molecule, item, indices)


@digest(form=form)
def get_partial_charge_from_molecule(item, indices='all'):

    return _auxiliary_getter(get_partial_charge_from_molecule, item, indices)


@digest(form=form)
def get_n_aminoacids_from_molecule(item, indices='all'):

    return _auxiliary_getter(get_n_aminoacids_from_molecule, item, indices)


@digest(form=form)
def get_n_nucleotides_from_molecule(item, indices='all'):

    return _auxiliary_getter(get_n_nucleotides_from_molecule, item, indices)


@digest(form=form)
def get_n_ions_from_molecule(item, indices='all'):

    return _auxiliary_getter(get_n_ions_from_molecule, item, indices)


@digest(form=form)
def get_n_waters_from_molecule(item, indices='all'):

    return _auxiliary_getter(get_n_waters_from_molecule, item, indices)


@digest(form=form)
def get_n_small_molecules_from_molecule(item, indices='all'):

    return _auxiliary_getter(get_n_small_molecules_from_molecule, item, indices)


@digest(form=form)
def get_n_peptides_from_molecule(item, indices='all'):

    return _auxiliary_getter(get_n_peptides_from_molecule, item, indices)


@digest(form=form)
def get_n_proteins_from_molecule(item, indices='all'):

    return _auxiliary_getter(get_n_proteins_from_molecule, item, indices)


@digest(form=form)
def get_n_dnas_from_molecule(item, indices='all'):

    return _auxiliary_getter(get_n_dnas_from_molecule, item, indices)


@digest(form=form)
def get_n_rnas_from_molecule(item, indices='all'):

    return _auxiliary_getter(get_n_rnas_from_molecule, item, indices)


@digest(form=form)
def get_n_lipids_from_molecule(item, indices='all'):

    return _auxiliary_getter(get_n_lipids_from_molecule, item, indices)


@digest(form=form)
def get_n_oligosaccharides_from_molecule(item, indices='all'):

    return _auxiliary_getter(get_n_oligosaccharides_from_molecule, item, indices)


@digest(form=form)
def get_n_saccharides_from_molecule(item, indices='all'):

    return _auxiliary_getter(get_n_saccharides_from_molecule, item, indices)


## chain


@digest(form=form)
def get_atom_index_from_chain(item, indices='all'):

    return _auxiliary_getter(get_atom_index_from_chain, item, indices)


@digest(form=form)
def get_atom_id_from_chain(item, indices='all'):

    return _auxiliary_getter(get_atom_id_from_chain, item, indices)


@digest(form=form)
def get_atom_name_from_chain(item, indices='all'):

    return _auxiliary_getter(get_atom_name_from_chain, item, indices)


@digest(form=form)
def get_atom_type_from_chain(item, indices='all'):

    return _auxiliary_getter(get_atom_type_from_chain, item, indices)


@digest(form=form)
def get_group_index_from_chain(item, indices='all'):

    return _auxiliary_getter(get_group_index_from_chain, item, indices)


@digest(form=form)
def get_group_id_from_chain(item, indices='all'):

    return _auxiliary_getter(get_group_id_from_chain, item, indices)


@digest(form=form)
def get_group_name_from_chain(item, indices='all'):

    return _auxiliary_getter(get_group_name_from_chain, item, indices)


@digest(form=form)
def get_group_type_from_chain(item, indices='all'):

    return _auxiliary_getter(get_group_type_from_chain, item, indices)


@digest(form=form)
def get_component_index_from_chain(item, indices='all'):

    return _auxiliary_getter(get_component_index_from_chain, item, indices)


@digest(form=form)
def get_component_id_from_chain(item, indices='all'):

    return _auxiliary_getter(get_component_id_from_chain, item, indices)


@digest(form=form)
def get_component_name_from_chain(item, indices='all'):

    return _auxiliary_getter(get_component_name_from_chain, item, indices)


@digest(form=form)
def get_component_type_from_chain(item, indices='all'):

    return _auxiliary_getter(get_component_type_from_chain, item, indices)


@digest(form=form)
def get_chain_index_from_chain(item, indices='all'):

    return _auxiliary_getter(get_chain_index_from_chain, item, indices)


@digest(form=form)
def get_molecule_index_from_chain(item, indices='all'):

    return _auxiliary_getter(get_molecule_index_from_chain, item, indices)


@digest(form=form)
def get_molecule_id_from_chain(item, indices='all'):

    return _auxiliary_getter(get_molecule_id_from_chain, item, indices)


@digest(form=form)
def get_molecule_name_from_chain(item, indices='all'):

    return _auxiliary_getter(get_molecule_name_from_chain, item, indices)


@digest(form=form)
def get_molecule_type_from_chain(item, indices='all'):

    return _auxiliary_getter(get_molecule_type_from_chain, item, indices)


@digest(form=form)
def get_entity_index_from_chain(item, indices='all'):

    return _auxiliary_getter(get_entity_index_from_chain, item, indices)


@digest(form=form)
def get_entity_id_from_chain(item, indices='all'):

    return _auxiliary_getter(get_entity_id_from_chain, item, indices)


@digest(form=form)
def get_entity_name_from_chain(item, indices='all'):

    return _auxiliary_getter(get_entity_name_from_chain, item, indices)


@digest(form=form)
def get_entity_type_from_chain(item, indices='all'):

    return _auxiliary_getter(get_entity_type_from_chain, item, indices)


@digest(form=form)
def get_n_atoms_from_chain(item, indices='all'):

    return _auxiliary_getter(get_n_atoms_from_chain, item, indices)


@digest(form=form)
def get_n_groups_from_chain(item, indices='all'):

    return _auxiliary_getter(get_n_groups_from_chain, item, indices)


@digest(form=form)
def get_n_components_from_chain(item, indices='all'):

    return _auxiliary_getter(get_n_components_from_chain, item, indices)


@digest(form=form)
def get_n_molecules_from_chain(item, indices='all'):

    return _auxiliary_getter(get_n_molecules_from_chain, item, indices)


@digest(form=form)
def get_n_chains_from_chain(item, indices='all'):

    return _auxiliary_getter(get_n_chains_from_chain, item, indices)


@digest(form=form)
def get_n_entities_from_chain(item, indices='all'):

    return _auxiliary_getter(get_n_entities_from_chain, item, indices)


@digest(form=form)
def get_n_bonds_from_chain(item, indices='all'):

    return _auxiliary_getter(get_n_bonds_from_chain, item, indices)


@digest(form=form)
def get_n_inner_bonds_from_chain(item, indices='all'):

    return _auxiliary_getter(get_n_inner_bonds_from_chain, item, indices)


@digest(form=form)
def get_formal_charge_from_chain(item, indices='all'):

    return _auxiliary_getter(get_formal_charge_from_chain, item, indices)


@digest(form=form)
def get_partial_charge_from_chain(item, indices='all'):

    return _auxiliary_getter(get_partial_charge_from_chain, item, indices)


@digest(form=form)
def get_n_aminoacids_from_chain(item, indices='all'):

    return _auxiliary_getter(get_n_aminoacids_from_chain, item, indices)


@digest(form=form)
def get_n_nucleotides_from_chain(item, indices='all'):

    return _auxiliary_getter(get_n_nucleotides_from_chain, item, indices)


@digest(form=form)
def get_n_ions_from_chain(item, indices='all'):

    return _auxiliary_getter(get_n_ions_from_chain, item, indices)


@digest(form=form)
def get_n_waters_from_chain(item, indices='all'):

    return _auxiliary_getter(get_n_waters_from_chain, item, indices)


@digest(form=form)
def get_n_small_molecules_from_chain(item, indices='all'):

    return _auxiliary_getter(get_n_small_molecules_from_chain, item, indices)


@digest(form=form)
def get_n_peptides_from_chain(item, indices='all'):

    return _auxiliary_getter(get_n_peptides_from_chain, item, indices)


@digest(form=form)
def get_n_proteins_from_chain(item, indices='all'):

    return _auxiliary_getter(get_n_proteins_from_chain, item, indices)


@digest(form=form)
def get_n_dnas_from_chain(item, indices='all'):

    return _auxiliary_getter(get_n_dnas_from_chain, item, indices)


@digest(form=form)
def get_n_rnas_from_chain(item, indices='all'):

    return _auxiliary_getter(get_n_rnas_from_chain, item, indices)


@digest(form=form)
def get_n_lipids_from_chain(item, indices='all'):

    return _auxiliary_getter(get_n_lipids_from_chain, item, indices)


@digest(form=form)
def get_n_oligosaccharides_from_chain(item, indices='all'):

    return _auxiliary_getter(get_n_oligosaccharides_from_chain, item, indices)


@digest(form=form)
def get_n_saccharides_from_chain(item, indices='all'):

    return _auxiliary_getter(get_n_saccharides_from_chain, item, indices)


## From entity


@digest(form=form)
def get_atom_index_from_entity(item, indices='all'):

    return _auxiliary_getter(get_atom_index_from_entity, item, indices)


@digest(form=form)
def get_atom_id_from_entity(item, indices='all'):

    return _auxiliary_getter(get_atom_id_from_entity, item, indices)


@digest(form=form)
def get_atom_name_from_entity(item, indices='all'):

    return _auxiliary_getter(get_atom_name_from_entity, item, indices)


@digest(form=form)
def get_atom_type_from_entity(item, indices='all'):

    return _auxiliary_getter(get_atom_type_from_entity, item, indices)


@digest(form=form)
def get_group_index_from_entity(item, indices='all'):

    return _auxiliary_getter(get_group_index_from_entity, item, indices)


@digest(form=form)
def get_group_id_from_entity(item, indices='all'):

    return _auxiliary_getter(get_group_id_from_entity, item, indices)


@digest(form=form)
def get_group_name_from_entity(item, indices='all'):

    return _auxiliary_getter(get_group_name_from_entity, item, indices)


@digest(form=form)
def get_group_type_from_entity(item, indices='all'):

    return _auxiliary_getter(get_group_type_from_entity, item, indices)


@digest(form=form)
def get_component_index_from_entity(item, indices='all'):

    return _auxiliary_getter(get_component_index_from_entity, item, indices)


@digest(form=form)
def get_component_id_from_entity(item, indices='all'):

    return _auxiliary_getter(get_component_id_from_entity, item, indices)


@digest(form=form)
def get_component_name_from_entity(item, indices='all'):

    return _auxiliary_getter(get_component_name_from_entity, item, indices)


@digest(form=form)
def get_component_type_from_entity(item, indices='all'):

    return _auxiliary_getter(get_component_type_from_entity, item, indices)


@digest(form=form)
def get_chain_index_from_entity(item, indices='all'):

    return _auxiliary_getter(get_chain_index_from_entity, item, indices)


@digest(form=form)
def get_chain_id_from_entity(item, indices='all'):

    return _auxiliary_getter(get_chain_id_from_entity, item, indices)


@digest(form=form)
def get_chain_name_from_entity(item, indices='all'):

    return _auxiliary_getter(get_chain_name_from_entity, item, indices)


@digest(form=form)
def get_chain_type_from_entity(item, indices='all'):

    return _auxiliary_getter(get_chain_type_from_entity, item, indices)


@digest(form=form)
def get_molecule_index_from_entity(item, indices='all'):

    return _auxiliary_getter(get_molecule_index_from_entity, item, indices)


@digest(form=form)
def get_molecule_id_from_entity(item, indices='all'):

    return _auxiliary_getter(get_molecule_id_from_entity, item, indices)


@digest(form=form)
def get_molecule_name_from_entity(item, indices='all'):

    return _auxiliary_getter(get_molecule_name_from_entity, item, indices)


@digest(form=form)
def get_molecule_type_from_entity(item, indices='all'):

    return _auxiliary_getter(get_molecule_type_from_entity, item, indices)


@digest(form=form)
def get_entity_index_from_entity(item, indices='all'):

    return _auxiliary_getter(get_entity_index_from_entity, item, indices)


@digest(form=form)
def get_n_atoms_from_entity(item, indices='all'):

    return _auxiliary_getter(get_n_atoms_from_entity, item, indices)


@digest(form=form)
def get_n_groups_from_entity(item, indices='all'):

    return _auxiliary_getter(get_n_groups_from_entity, item, indices)


@digest(form=form)
def get_n_components_from_entity(item, indices='all'):

    return _auxiliary_getter(get_n_components_from_entity, item, indices)


@digest(form=form)
def get_n_molecules_from_entity(item, indices='all'):

    return _auxiliary_getter(get_n_molecules_from_entity, item, indices)


@digest(form=form)
def get_n_chains_from_entity(item, indices='all'):

    return _auxiliary_getter(get_n_chains_from_entity, item, indices)


@digest(form=form)
def get_n_entities_from_entity(item, indices='all'):


@digest(form=form)
def get_n_bonds_from_entity(item, indices='all'):


@digest(form=form)
def get_n_inner_bonds_from_entity(item, indices='all'):


@digest(form=form)
def get_formal_charge_from_entity(item, indices='all'):


@digest(form=form)
def get_partial_charge_from_entity(item, indices='all'):



@digest(form=form)
def get_n_aminoacids_from_entity(item, indices='all'):


@digest(form=form)
def get_n_nucleotides_from_entity(item, indices='all'):


@digest(form=form)
def get_n_ions_from_entity(item, indices='all'):


@digest(form=form)
def get_n_waters_from_entity(item, indices='all'):


@digest(form=form)
def get_n_small_molecules_from_entity(item, indices='all'):



@digest(form=form)
def get_n_peptides_from_entity(item, indices='all'):


@digest(form=form)
def get_n_proteins_from_entity(item, indices='all'):


@digest(form=form)
def get_n_dnas_from_entity(item, indices='all'):


@digest(form=form)
def get_n_rnas_from_entity(item, indices='all'):


@digest(form=form)
def get_n_lipids_from_entity(item, indices='all'):


@digest(form=form)
def get_n_oligosaccharides_from_entity(item, indices='all'):


@digest(form=form)
def get_n_saccharides_from_entity(item, indices='all'):



## system

@digest(form=form)
def get_n_aminoacids_from_system(item):


@digest(form=form)
def get_n_nucleotides_from_system(item):


@digest(form=form)
def get_n_ions_from_system(item):


@digest(form=form)
def get_n_waters_from_system(item):


@digest(form=form)
def get_n_small_molecules_from_system(item):


@digest(form=form)
def get_n_peptides_from_system(item):


@digest(form=form)
def get_n_proteins_from_system(item):


@digest(form=form)
def get_n_dnas_from_system(item):


@digest(form=form)
def get_n_rnas_from_system(item):


@digest(form=form)
def get_n_lipids_from_system(item):


@digest(form=form)
def get_n_oligosaccharides_from_system(item):


@digest(form=form)
def get_n_saccharides_from_system(item):



@digest(form=form)
def get_formal_charge_from_system(item, indices='all'):


@digest(form=form)
def get_partial_charge_from_system(item, indices='all'):


@digest(form=form)
def get_bonded_atoms_from_system(item):


@digest(form=form)
def get_bond_index_from_system(item):


## bond

@digest(form=form)
def get_bond_index_from_bond(item, indices='all'):


@digest(form=form)
def get_n_bonds_from_bond(item, indices='all'):

