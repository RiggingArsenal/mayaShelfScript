import pymel.core as pm


def reorder_sel(alphabet=False):
    sel = pm.ls(sl=True)

    # Reorder selection alphabetically
    if alphabet:
        sel = sorted(sel)

    # Reorder
    for each in sel:
        pm.reorder(each, back=1)


reorder_sel()
