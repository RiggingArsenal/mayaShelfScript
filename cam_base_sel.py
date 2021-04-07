import maya.cmds as cmds


def cam_base_sel():
    # Query the Move tool Selection style: Camera-base selection
    on = cmds.selectPref(q=True, useDepth=True)

    # If the Camera-base selection is off, turn it on
    if not on:
        cmds.selectPref(useDepth=True)

    # If the Camera-base selection is on, turn it off
    else:
        cmds.selectPref(useDepth=False)


cam_base_sel()

