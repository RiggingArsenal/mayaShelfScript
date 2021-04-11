import pymel.core as pm


def set_focus_panel(panel):
    pm.setFocus(panel)


def get_focus_panel():
    panel = pm.getPanel(withFocus=True)
    return panel


def collapse_outliner_hierachy(focus=False):
    sel = pm.ls(sl=True)

    # Store current focus panel
    current_panel = get_focus_panel() or []

    # Get the ontliner from current scene
    vis_panels = pm.getPanel(vis=True) or []
    outliner_panels = []
    if vis_panels:
        for each in vis_panels:
            if "outlinerPanel" in each:
                outliner_panels.append(each)

    # Extend the selection item outliner hierachy
    if outliner_panels:
        for each in outliner_panels:
            if focus:
                if each != current_panel:
                    continue
            set_focus_panel(each)
            if sel:
                pm.outlinerEditor(each, edit=True, eas=False)
            else:
                pm.outlinerEditor(each, edit=True, eai=False)

    # Return to previous focus panel
    set_focus_panel(current_panel)


collapse_outliner_hierachy()