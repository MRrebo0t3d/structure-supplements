def findGroupings(constraints):
    groups = {}
    for constraint in constraints:
       groupID = constraint.pop(1)
       constraint.pop(0)
       constraint = tuple(constraint)
       if groupID in groups:
           groups[groupID].append(constraint)
       else:
           groups[groupID] = [constraint]
    groups = groups.values()
    groups = [tuple(group) for group in groups]
    return groups

def getFileContents(file):
    constraints = []
    with open(file,'r') as infile:
        lines = infile.readlines()
        lines = [line.strip().split() for line in lines]
        for line in lines:
            constraint = [int(x) for x in line[:2]] + line[2:4]
            if len(line) == 6:
                constraint += [float(x) for x in line[-2:]]
            constraints.append(constraint)
    return constraints

cy_file = 'cy_test_dist.txt'
cy_constraints = getFileContents(cy_file)
cy_groups = findGroupings(cy_constraints)

xplor_file = 'xp_test_dist.txt'
xplor_constraints = getFileContents(xplor_file)
xplor_groups = findGroupings(xplor_constraints)

print "Number of cyana constraints: ", len(cy_constraints)
print "Number of cyana groups: ", len(cy_groups)
print ""
print ""
print "Number of xplor constraints: ", len(xplor_constraints)
print "Number of xplor groups: " , len(xplor_groups)

print ""
print ""

print len(set(xplor_groups)), len(set(cy_groups))
diff_xplor = list(set(tuple(xplor_groups)) - set(tuple(cy_groups)))
diff_cyana = list(set(tuple(cy_groups)) - set(tuple(xplor_groups)))

print "Groups within xplor not in cyana"
for group in diff_xplor:
    print group

print ""
print ""

print "Groups within cyana not in xplor"
for group in diff_cyana:
    print group

