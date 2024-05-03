from ...exceptions import ArgumentError
from ...variables import is_all

functions_with_boolean = (
        'molsysmt.basic.get.get',
        'molsysmt.basic.compare.compare',
        'molsysmt.basic.iterator.__init__',
        'iterators.__init__',
        )

set_functions = (
        'set.set',
        'set_chain_id_to_atom')

def digest_chain_id(chain_id, caller=None):
    """Checks if `chain_id` has the expected type and value.

    Parameters
    ----------
    chain_id : Any
        The `chain_id` argument for digestion.
    caller: str, optional
        Name of the function or method that is being digested.

    .. _PEP 484:
        https://www.python.org/dev/peps/pep-0484/#the-any-type

    Returns
    -------
    bool
        Either True or False when caller is `get`.

    Raises
    -------
    ArgumentError
        If the given `chain_id` has not of the correct type or value.
    """


    if caller.endswith(functions_with_boolean):
        if isinstance(chain_id, bool):
            return chain_id
    elif caller.endswith(set_functions):
        if isinstance(chain_id, int):
            return chain_id
    elif caller=='molsysmt.build.define_new_chain.define_new_chain':
        if isinstance(chain_id, int):
            return chain_id
        elif chain_id is None:
            return None
    elif caller.startswith('molsysmt.form.') and caller.count('.to_')==2:
        return chain_id

    raise ArgumentError('chain_id', caller=caller, message=None)

