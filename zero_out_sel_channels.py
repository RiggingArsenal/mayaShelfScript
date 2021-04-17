import maya.cmds as cmds
import maya.mel as mel


def get_sel_channels():
    channel_box_name = mel.eval('$temp=$gChannelBoxName')

    # sma = selectedMainAttributes
    # Returns the names of all the selected attributes in the top section of the channel box.
    sma = cmds.channelBox(channel_box_name, query=True, sma=True)

    # ssa = selectedShapeAttributes
    # Returns the names of all the selected attributes in the middle (shape) section of the channel box.
    ssa = cmds.channelBox(channel_box_name, query=True, ssa=True)

    # sha = selectedHistoryAttributes
    # Returns the names of all the selected attributes in the INPUT section of the channel box.
    sha = cmds.channelBox(channel_box_name, query=True, sha=True)

    channels = list()
    if sma:
        channels.extend(sma)
    if ssa:
        channels.extend(ssa)
    if sha:
        channels.extend(sha)

    return channels


def zero_out_sel_channels(val=None):
    sel = cmds.ls(sl=True)

    if sel:
        # Get the selected channels
        channels = get_sel_channels()

        for each in sel:
            if channels:
                for channel in channels:
                    try:
                        # User could provide the set attribute value
                        if val:
                            cmds.setAttr('{0}.{1}'.format(each, channel), val)

                        # Default set attribute == 0
                        else:
                            cmds.setAttr('{0}.{1}'.format(each, channel), 0)
                    except:
                        print 'Did not work.{0}'.format(each)
            else:
                cmds.warning('Please select the Channel. ')
    else:
        cmds.warning('Please select the Object. ')


zero_out_sel_channels()
