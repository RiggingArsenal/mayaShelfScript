import maya.cmds as cmds


def zero_out_attr(obj, attr):
    try:
        if attr in ['tx', 'ty', 'tz', 'rx', 'ry', 'rz']:
            cmds.setAttr('{0}.{1}'.format(obj, attr), 0)

        if attr in ['sx', 'sy', 'sz', 'v']:
            cmds.setAttr('{0}.{1}'.format(obj, attr), 1)
    except:
        print 'Did not work.{0}'.format(obj)


def zero_out_sel(attrs=[], sel=cmds.ls(sl=True)):
    for each in sel:
        # If the user provides attributes
        if attrs:
            for attr in attrs:
                zero_out_attr(each, attr)
        # Default zero out attributes = ['tx', 'ty', 'tz', 'rx', 'ry', 'rz']
        else:
            for pre_attr in ['t', 'r']:
                for suf_attr in ['x', 'y', 'z']:
                    zero_out_attr(each, pre_attr + suf_attr)


zero_out_sel()
