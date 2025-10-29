def poes(area, h, poro, swi, boi):
    """

    Parameters
    ----------
    area: Area, Acres
    h: Thickness, ft
    poro: Porosity, fraction
    swi: Initial water saturation, fraction
    boi: Bubble point, bbl/stb

    Returns
    ----
    POES, bbl
    """
    stoiip = (7758 * area * h * poro * (1 - swi)) / boi

    return stoiip