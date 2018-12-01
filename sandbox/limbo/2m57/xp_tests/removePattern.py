import sys, re

file = sys.argv[1]

def find_angle_name(some_file):
    ext = some_file.split('.')[-1]
    f1 = open(file,"r")
    f2 = open('odih.'+ext,'w')
    pat = re.compile(r'(\{.[a-z0-9]*.[\/[a-z]*]?\})')
    for line in f1:
	m = pat.search(line)
	if m:
	    name_of_angle = m.group(1)
	    line_wout_angle_name = re.sub(pat, '', line)
	    f2.write(line_wout_angle_name)
	else:
	    f2.write(line)
	    continue
    f1.close()
    f2.close()
    return "Done!"

print find_angle_name(file)
