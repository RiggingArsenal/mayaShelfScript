import pymel.core as pm


def toggle_mesh_xray():
    objects = pm.ls(sl=True) or []

    # If users select the mesh, will turn on the mesh display X-Ray ;
    # If the mesh display X-Ray is already on, will turn off the mesh display X-Ray.
    children_transform = []
    if objects:
        for obj in objects:
            # If your selection has the child
            # pm.displaySurface query will pop out # Error : Can not query culling on multiple objects!
            # The following steps will take out the selection's children
            children = pm.listRelatives(obj, children=True) or []
            if children:
                for child in children:
                    objType = pm.objectType(child)
                    if objType == 'transform':
                        pm.parent(child, w=True)
                        children_transform.append(child)
                        pm.select(cl=True)

            # Toggle mesh display X-Ray
            pm.displaySurface(obj, xRay=(not pm.displaySurface(obj, xRay=True, query=True)[0]))

            # Parent the children back for the selection
            if children_transform:
                pm.parent(children_transform, obj)
                pm.select(cl=True)

    # If the user didn't select anything, the script will turn off all the mesh X-Ray display in your scene.
    else:
        # Get all the mesh shapes
        shapes = pm.ls(type="mesh")

        # Though the shape find its transform
        transforms = pm.listRelatives(shapes, parent=True)

        # Turn off the mesh X-Ray display
        pm.displaySurface(transforms, xRay=False)


toggle_mesh_xray()