import maya.mel as mel


def delete_unused_nodes():
    mel.eval("MLdeleteUnused;")


delete_unused_nodes()
