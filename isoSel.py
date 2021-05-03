import pymel.core as pm


def setFocusPanel(panel):
    pm.setFocus(panel)


def getFocusPanel():
    panel = pm.getPanel(withFocus=True)
    return panel


def isoSel(mode=0, focus=False):
    sel = pm.ls(sl=True)

    # Store current focus panel
    currentPanel = getFocusPanel() or []

    # Get the modelPanel from current scene
    visPanels = pm.getPanel(vis=True) or []
    modelPanels = []
    if visPanels:
        for each in visPanels:
            if "modelPanel" in each:
                modelPanels.append(each)

    if modelPanels:
        for each in modelPanels:
            # If focus = True, will only add/remove selected objects for the isolate select
            if focus:
                # If the model panel does not equal the current panel, continue the loop
                if each != currentPanel:
                    continue

            # Add selected objects for the isolate select
            if sel:
                # mode == 0 : Add selected mode
                if mode == 0:
                    pm.isolateSelect(each, addSelected=1)

                # mode == 1 : Remove selected mode
                if mode == 1:
                    pm.isolateSelect(each, removeSelected=1)

            # If noting selected will turn off the isolate select
            else:
                pm.isolateSelect(each, state=0)

    # Return to previous focus panel
    setFocusPanel(currentPanel)


isoSel()
