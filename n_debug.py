import sys

nathan_debug_state = False

try:
    if sys.argv[1] == "n_dbug":
        # global nathan_debug_state
        nathan_debug_state = True
except:
    pass

def ndbp(_s):
    global nathan_debug_state
    if nathan_debug_state == True:
        print(_s)
    pass

def toggle_debug():
    global nathan_debug_state
    if nathan_debug_state == True:
        nathan_debug_state = False
    else:
        nathan_debug_state = True

def set_debug(_input, _name= None):
    ''' _input is bool '''
    global nathan_debug_state
    if _input == True:
        nathan_debug_state = _input
    elif _input == False:
        nathan_debug_state = _input
    else:
        print(f"set_debug {_name} not a bool")
        pass

ndbp(f"If you are seeing this, nathan_debug_state is {nathan_debug_state}")
