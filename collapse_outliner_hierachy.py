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

    if outliner_panels:
        for each in outliner_panels:
            # If focus = True, will only collapse hierachy for the focus outliner
            if focus:
                # If the outliner panel does not equal the current pannel, continue the loop
                if each != current_panel:
                    continue

            # Collapse the outliner hierachy for the selected node
            set_focus_panel(each)
            
            # If the user selected the node, will only collapse the selected node outliner hierachy
            if sel:
                pm.outlinerEditor(each, edit=True, eas=False)
            
            # If the user didn't select any node, will collapse all the node outliner hierachy
            else:
                pm.outlinerEditor(each, edit=True, eai=False)

    # Return to previous focus panel
    set_focus_panel(current_panel)


collapse_outliner_hierachy()