from molsysmt._private.exceptions import *
from molsysmt._private.digestion import *
from molsysmt._private.lists_and_tuples import is_list_or_tuple

def add(to_molecular_system, from_molecular_systems, selections='all', structure_indices='all',
        syntaxis='MolSysMT', check=True):

    """add(items=None, selection='all', structure_indices='all', syntaxis='MolSysMT' to_form=None)

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

    from . import convert, extract, select, is_molecular_system, are_multiple_molecular_systems
    from molsysmt.api_forms import dict_add

    if check:

        if not is_molecular_system(to_molecular_system):
            raise MolecularSystemNeededError()

        if not is_molecular_system(from_molecular_systems):
            if not are_multiple_molecular_systems(from_molecular_systems):
                raise MolecularSystemNeededError()

    if is_molecular_system(from_molecular_systems):
        from_molecular_systems = [from_molecular_systems]

    n_from_molecular_systems = len(from_molecular_systems)

    if not is_list_or_tuple(selections):
        selections = [selections for ii in range(n_from_molecular_systems)]
    elif len(selections)!=n_from_molecular_systems:
        raise ValueError("The length of the lists items and selections need to be equal.")

    if not is_list_or_tuple(structure_indices):
        structure_indices = [digest_structure_indices(structure_indices) for ii in range(n_from_molecular_systems)]
    elif len(structure_indices)!=n_from_molecular_systems:
        raise ValueError("The length of the lists items and structure_indices need to be equal.")


    for aux_molecular_system, aux_selection, aux_structure_indices in zip(from_molecular_systems, selections, structure_indices):

        atom_indices = select(aux_molecular_system, selection=aux_selection, syntaxis=syntaxis, check=False)

        aux_item = convert(aux_molecular_system, selection=aux_selection, structure_indices=aux_structure_indices, syntaxis=syntaxis,
                to_form=to_form, check=False)

        dict_add[to_form](to_item, from_item)

    pass

