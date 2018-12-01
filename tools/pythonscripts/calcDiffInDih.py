# Start_to_End: (CHI_WRNG,CHI_RGHT)

# G & A: == C1' -- N9 ==
# U & C: == C1' -- N1 ==

res =  [
{
'gO4P_to_C8': (-145.9,-115.9), 
'gC2P_to_C8': (95.4,122.8),
'gO4P_to_C4': (34.1,63.2),
'gC2P_to_C4': (-84.6,-58.1)}, {
'uO4P_to_C2': (-91.1,-155.1),
'uC2P_to_C2': (150.2,84.4),
'uO4P_to_C6': (89.0,24.0),
'uC2P_to_C6': (-29.8,-96.5)}, {
'aO4P_to_C8': (15.8,32.9),
'aC2P_to_C8': (-102.9,-86.2),
'aO4P_to_C4': (-164.0,-150.1),
'aC2P_to_C4': (77.1,90.8)}, {
'cO4P_to_C6': (113.9,22.4),
'cC2P_to_C6': (-4.9,-98.4),
'cO4P_to_C2': (-66.0,-155.2),
'cC2P_to_C2': (175.1,84.0)
}]

def get_values(x):
    for dic in x:
        for key in dic:
	    print key
            print(dic[key][1] - dic[key][0])

print get_values(res)
