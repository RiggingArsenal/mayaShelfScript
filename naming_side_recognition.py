import pymel.core as pm


def naming_side_recognition(l=[], r=[]):
    # Default l/r prefix, suffix
    if not l:
        l = ['l', 'left', 'L', 'Left', 'LEFT']

    if not r:
        r = ['r', 'right', 'R', 'Right', 'RIGHT']

    sel = pm.ls(sl=True) or []

    # Get sel list Hierarchy
    selHier = pm.listRelatives(sel, ad=True, f=True, type='transform')

    # Combine sel and selHier list
    sel = set(sel + selHier)

    # Select sel list Hierarchy
    pm.select(sel)

    # Switch l/r Prefix, Suffix
    if sel:
        for each in sel:
            for i in range(0, len(l)):
                if each.startswith('{}_'.format(l[i])) or each.startswith('{}_'.format(r[i])):
                    # l Prefix
                    if each.startswith('{}_'.format(l[i])):
                        pm.select(cl=True)
                        pm.select(each)
                        pm.mel.searchReplaceNames('{}_'.format(l[i]), '{}_'.format(r[i]), "selected")
                        pm.select(cl=True)
                        continue

                    # r Prefix
                    if each.startswith('{}_'.format(r[i])):
                        pm.select(cl=True)
                        pm.select(each)
                        pm.mel.searchReplaceNames('{}_'.format(r[i]), '{}_'.format(l[i]), "selected")
                        pm.select(cl=True)
                        continue

            # Search Replace Suffix
            for i in range(0, len(l)):
                if each.endswith('_{}'.format(l[i])) or each.endswith('_{}'.format(r[i])):
                    # l Suffix
                    if each.endswith('_{}'.format(l[i])):
                        pm.select(cl=True)
                        pm.select(each)
                        pm.mel.searchReplaceNames('_{}'.format(l[i]), '_{}'.format(r[i]), "selected")
                        pm.select(cl=True)
                        continue

                    # r Suffix
                    if each.endswith('_{}'.format(r[i])):
                        pm.select(cl=True)
                        pm.select(each)
                        pm.mel.searchReplaceNames('_{}'.format(r[i]), '_{}'.format(l[i]), "selected")
                        pm.select(cl=True)
                        continue

        pm.select(sel)


naming_side_recognition()