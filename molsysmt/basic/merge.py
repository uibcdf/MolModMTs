from molsysmt._private_tools.lists_and_tuples import is_list_or_tuple
from molsysmt._private_tools._digestion import *
from molsysmt._private_tools.exceptions import *
from molsysmt.tools.molecular_systems import is_a_single_molecular_system
from molsysmt.forms import dict_merge, dict_add

def merge(molecular_systems, selections='all', frame_indices='all', syntaxis='MolSysMT', to_form=None):

    """merge(items=None, selection='all', frame_indices='all', syntaxis='MolSysMT' to_form=None)

    XXX

    Paragraph with detailed explanation.

    Parameters
    ----------

    item: molecular model
        Molecular model in any of the supported forms by MolSysMT. (See: XXX)

    to_form: str, default='molsysmt.MolSys'
        Any accepted form by MolSysMt for the output object.

    selection: str, list, tuple or np.ndarray, defaul='all'
       Atoms selection over which this method applies. The selection can be given by a
       list, tuple or numpy array of integers (0-based), or by means of a string following any of
       the selection syntaxis parsable by MolSysMT (see: :func:`molsysmt.select`).

    syntaxis: str, default='MolSysMT'
       Syntaxis used in the argument `selection` (in case it is a string). The
       current options supported by MolSysMt can be found in section XXX (see: :func:`molsysmt.select`).

    Returns
    -------
    None
        The method prints out a pandas dataframe with relevant information depending on the target
        and the form of the item.

    Examples
    --------

    See Also
    --------

    :func:`molsysmt.get`, :func:`molsysmt.select`
    Notes
    -----

    """

    from molsysmt.basic import convert, extract, select

    if is_a_single_molecular_system(molecular_systems):
        raise NeedsMultipleMolecularSystemsError()

    tmp_molecular_systems = []
    for aux in molecular_systems:
        tmp_molecular_systems.append(digest_molecular_system(aux))
    molecular_systems = tmp_molecular_systems

    n_molecular_systems = len(molecular_systems)

    if not is_list_or_tuple(selections):
        selections = [selections for ii in range(n_molecular_systems)]
    elif len(selections)!=n_molecular_systems:
        raise ValueError("The length of the lists items and selections need to be equal.")

    if not is_list_or_tuple(frame_indices):
        frame_indices = [digest_frame_indices(frame_indices) for ii in range(n_molecular_systems)]
    elif len(frame_indices)!=n_molecular_systems:
        raise ValueError("The length of the lists items and frame_indices need to be equal.")

    if to_form is None:
        to_molecular_system = extract(molecular_systems[0], selection=selections[0], frame_indices=frame_indices[0])
    else:
        to_molecular_system = convert(molecular_systems[0], selection=selections[0], frame_indices=frame_indices[0], to_form=to_form)

    to_molecular_system = digest_molecular_system(to_molecular_system)

    for aux_molecular_system, aux_selection, aux_frame_indices in zip(molecular_systems[1:], selections[1:], frame_indices[1:]):

        atom_indices = select(aux_molecular_system, selection=aux_selection, syntaxis=syntaxis)

        to_already_merged=[]

        # topology

        to_form = to_molecular_system.elements_form
        to_item = to_molecular_system.elements_item

        if to_form is not None:
            from_item = convert(aux_molecular_system, selection=atom_indices, frame_indices=aux_frame_indices, syntaxis=syntaxis, to_form=to_form)
            try:
                dict_add[to_form](to_item, from_item)
                to_already_merged.append(to_item)
            except:
                tmp_item=dict_merge[to_form](to_item, from_item)
                to_molecular_system._replace_object(to_item, tmp_item)
                to_already_merged.append(tmp_item)

        # ff_parameters

        to_form = to_molecular_system.ff_parameters_form
        to_item = to_molecular_system.ff_parameters_item

        if to_form is not None:
            if to_item not in to_already_merged:
                from_item = convert(aux_molecular_system, selection=atom_indices, frame_indices=aux_frame_indices, syntaxis=syntaxis, to_form=to_form)
                try:
                    dict_add[to_form](to_item, from_item)
                    to_already_merged.append(to_item)
                except:
                    tmp_item=dict_merge[to_form](to_item, from_item)
                    to_molecular_system._replace_object(to_item, tmp_item)
                    to_already_merged.append(tmp_item)

        # bonds

        to_form = to_molecular_system.bonds_form
        to_item = to_molecular_system.bonds_item

        if to_form is not None:
            if to_item not in to_already_merged:
                from_item = convert(aux_molecular_system, selection=atom_indices, frame_indices=aux_frame_indices, syntaxis=syntaxis, to_form=to_form)
                try:
                    dict_add[to_form](to_item, from_item)
                    to_already_added.append(to_item)
                except:
                    tmp_item=dict_merge[to_form](to_item, from_item)
                    to_molecular_system._replace_object(to_item, tmp_item)
                    to_already_merged.append(tmp_item)


        # coordinates

        to_form = to_molecular_system.coordinates_form
        to_item = to_molecular_system.coordinates_item

        if to_form is not None:
            if to_item not in to_already_merged:
                from_item = convert(aux_molecular_system, selection=atom_indices, frame_indices=aux_frame_indices, syntaxis=syntaxis, to_form=to_form)
                try:
                    dict_add[to_form](to_item, from_item)
                    to_already_added.append(to_item)
                except:
                    tmp_item=dict_merge[to_form](to_item, from_item)
                    to_molecular_system._replace_object(to_item, tmp_item)
                    to_already_merged.append(tmp_item)

        # The box info is taken from the first molecular_system

    output_items, output_forms = to_molecular_system.get_items()
    if len(output_items)==1:
        output = output_items[0]
    else:
        output = output_items

    return output


