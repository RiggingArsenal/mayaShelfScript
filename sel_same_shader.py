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


def get_sg_faces(sg, shape=False):
    all_sg_faces = pm.sets(sg, q=True) or []

    results = []
    # If the shape has input, will only return the faces have the same shape
    if shape:
        for each in all_sg_faces:
            each_shape = pm.PyNode(each.name().split('.')[0])

            if shape == each_shape:
                try:
                    # If each == nt.Mesh(u'pSphereShape1')
                    results.append(each.faces)
                except:
                    # If each == MeshFace(u'pSphereShape1.f[0:399]')
                    results.append(each)

    # Return all the faces have the same shading group
    else:
        for each in all_sg_faces:
            try:
                # If each == nt.Mesh(u'pSphereShape1')
                results.append(each.faces)
            except:
                # If each == MeshFace(u'pSphereShape1.f[0:399]')
                results.append(each)

    return results


def sel_same_shader(sel_all_scene=False):
    sel_face = pm.ls(sl=True)

    # Check user selection
    run = True

    if sel_face:
        # If selection is not mesh type
        if sel_face[0].nodeType() != 'mesh':
            run = False

        # If user selection whole mesh faces
        if ':' in sel_face[0].name():
            run = False

        # If user select more than one mesh faces
        # if len(sel_face) >= 2:
            # run = False

    else:
        run = False

    # If the user selects the mesh face, run the script
    if run:
        # Get the selected face shader
        sel_shader = get_face_shader()

        # Get the mesh shape node
        shape = pm.PyNode(sel_face[0].name().split('.')[0])

        if sel_shader:
            # Select the faces that have the same shader as selected face
            # From all scene
            if sel_all_scene:
                pm.select(get_sg_faces(sel_shader), add=True)

            # From selected mesh
            else:
                pm.select(get_sg_faces(sel_shader, shape), add=True)

    # If the user didn't select the mesh face, pop out the warning
    else:
        # pm.warning("Please select one face of the mesh .")

        pm.confirmDialog(title='WARNING!',
                         message='Please select one face of the mesh .      ',
                         button=['Ok'],
                         defaultButton='Ok',
                         cancelButton='Cancel',
                         dismissString='Cancel', )


sel_same_shader()