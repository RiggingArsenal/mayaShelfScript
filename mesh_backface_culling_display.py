import pymel.core as pm


def mesh_backface_culling_display():
    sel = pm.ls(sl=True)

    for each in sel:
        # Get the Backface Culling Mode
        mode = each.backfaceCulling.get()

        # If Backface Culling not in "full" mode, switch to "full" mode
        if mode != 3:
            each.backfaceCulling.set(3)

        # If Backface Culling in "full" mode, turn it off
        elif mode == 3:
            each.backfaceCulling.set(0)


mesh_backface_culling_display()
