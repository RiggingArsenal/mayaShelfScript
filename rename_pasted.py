import pymel.core as pm


def remove_pasted_prefix(obj=None):
    # Remove the object name startswith 'pasted__'
    if obj.name().split('|')[-1].startswith('pasted__'):
        pm.mel.searchReplaceNames("pasted__", " ", "selected")


def remove_suffix_int(obj=None):
    check = obj
    intList = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    nameLen = len(obj.name())
    tmp = True

    # Remove the obj suffix integer
    for i in range(0, nameLen+1):
        last = check[-1]
        if last in intList:
            check = check[0:-1]
        else:
            tmp = False
            continue

    # If scene have the same name, rename won't keep increasing the suffix integer number
    if pm.objExists(obj.name()):
        if tmp:
            pm.rename(obj, '$TEMP')

    pm.rename(obj, check)


def rename_pasted():
    sel = pm.ls(sl=True) or []

    # Get sel list Hierarchy
    selHier = pm.listRelatives(sel, ad=True, f=True)

    # Combine sel and selHier list
    sel = sel + selHier

    # Select sel list Hierarchy
    pm.select(sel)

    # Rename pasted
    if sel:
        for each in sel:
            remove_pasted_prefix(each)
            remove_suffix_int(each)


rename_pasted()
