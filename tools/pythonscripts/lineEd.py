import sys

file_name = sys.argv[1]


def remove_line(some_file):
    ext = some_file.split('.')[-1]
    output_file = "nmdistances."+ext
    with open(some_file, 'r') as f1:
        with open(output_file, 'w') as f2:
            lines = f1.readlines()
	    for line in lines:
                if '101' not in line:
                    f2.write(line)

remove_line(file_name)
