# --------------------------------------------------------------
#  bm_EnableTrackerTRS.py
#  Version: 1.0.2
#  Author: Ben McEwan
#
#  Last Modified by: Andrée Knutsson
#  Last Updated: September 22th, 2023
# --------------------------------------------------------------

# --------------------------------------------------------------
#  USAGE:
#
#  Adds a meta+t hotkey to enable all T, R & S checkboxes in a selected Tracker node.
# --------------------------------------------------------------
#
# 1.0.2 Update: 
# - Now possible to enable TRS on multiple "Tracker4" nodes at the same time.
# - Returns if no Tracker4 nodes are selected.
# --------------------------------------------------------------

import nuke

def bm_EnableTrackerTRS():
    #Filter selected nodes to Tracker4 nodes 
    nodes = nuke.selectedNodes('Tracker4')

    # If no tracker4 nodes are selected, return message.
    if len(nodes) == 0:
        return nuke.message("Select a Tracker to enable Translate, Rotate & Scale")
    
    t = [8, 39, 70, 101, 132, 163, 194, 225, 256, 287, 318, 7, 38, 69, 100, 131, 162, 193, 224, 255, 286, 317, 6, 37, 68, 99, 130, 161, 192, 223, 254, 285, 316, 349, 380, 411, 442, 473, 504, 535, 566, 597, 628, 659, 348, 379, 410, 441, 472, 503, 534, 565, 596, 627, 658, 347, 378, 409, 440, 471, 502, 533, 564, 595, 626, 657]

  
    for node in nodes:
        try:
            for n in t:
                node['tracks'].setValue(True, n)
        except:
            print ("Error: Could not enable TRS for tracks in {}".format(node.name()))



# Add menu items
nuke.menu('Nuke').addCommand('Edit/Shortcuts/Enable Tracker T-R-S', 'bm_EnableTrackerTRS.bm_EnableTrackerTRS()', 'meta+t')
