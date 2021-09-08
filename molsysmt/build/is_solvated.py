def is_solvated(molecular_system):

    from molsysmt.multitool import get

    output = False

    n_waters, volume = get(molecular_system, target='system', n_waters=True, box_volume=True)
    if (n_waters>0) and (volume is not None):
        density_number = puw.get_value((n_waters/volume), to_unit='1/nm**3')
        if (density_number)>15:
            output = True

    return output
