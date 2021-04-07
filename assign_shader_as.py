import pymel.core as pm


def get_face_shader():
    # Use the hyperShade command "Select Materials From Objects"
    pm.hyperShade(shaderNetworksSelectMaterialNodes=True)

    # Use Classification
    # Classification strings look like file pathnames ("shader/reflective" or "texture/2D", for example)
    for shader in pm.selected(materials=True):
        if [c for c in shader.classification() if 'shader/surface' in c]:
            # lambert1 return : [nt.ShadingEngine(u'initialParticleSE'), nt.ShadingEngine(u'initialShadingGroup')]
            face_shader = pm.listConnections(shader, type='shadingEngine')[-1]

    return face_shader


def assign_shader_as():
    # List objects and components that are currently selected in their order of selection.
    pm.selectPref(trackSelectionOrder=True)
    sel_face = pm.ls(os=True)
    # Clears the active list
    pm.select(cl=True)

    # Check user selection
    run = True

    if sel_face:
        # If the last selection is not mesh type
        if sel_face[-1].nodeType() != 'mesh':
            # If the last selection is (e.g.: " nt.Transform(u'pSphere1') ")
            if sel_face[-1].getShape():
                # Will select override f[0] as last selection
                sel_face[-1] = sel_face[-1].getShape().faces[0]

            else:
                run = False

    else:
        run = False

    # If the user selects the mesh face, run the script
    if run:
        # Get the selected face shader
        pm.select(sel_face[-1], r=True)
        sel_shader = get_face_shader()

        if sel_shader:
            # Filter the selected list
            results = []
            for each in sel_face:
                # Ignore the selection not mesh type
                if each.nodeType() != 'mesh':
                    # If the last selection is not (e.g.: " nt.Transform(u'pSphere1') "), continue
                    if not each.getShape():
                        continue
                try:
                    # If each == nt.Mesh(u'pSphereShape1')
                    results.append(each.faces)
                except:
                    # If each == MeshFace(u'pSphereShape1.f[0:399]')
                    results.append(each)

            # Assign the shader on selected faces
            pm.select(results, r=True)
            pm.hyperShade(assign=sel_shader)

            # Reselect the first selection
            pm.select(sel_face[-1], add=True)

    # If the user didn't select the mesh face, pop out the warning
    else:
        # pm.warning("The last selection need to be mesh face.")

        pm.confirmDialog(title='WARNING!',
                         message='The last selection need to be mesh face.      ',
                         button=['Ok'],
                         defaultButton='Ok',
                         cancelButton='Cancel',
                         dismissString='Cancel', )


assign_shader_as()
