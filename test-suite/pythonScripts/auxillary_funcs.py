import os
import sys
def read_yaml(config):
     '''
     readYaml is a script that must be executed using the nmrfx environment.
     It has dependencies on the java yaml reader. This function takes the
     input file and returns the python object. Although this seems like a
     wasted function, this allows the testing suite to still be run in the
     python environment without the nmrfx environment.
     '''
     from reader import readYaml
     pythonDict = readYaml(config)
     return pythonDict


def find_compiled_struct():
    '''
    Find compiled struct finds the newest compiled structure based on the version number.
    It will not look if a value is specified as a global environment variable STRUCTURE.
    The function returns the full path to the target.
    '''
    val = os.getenv("STRUCTURE")
    if val:
        return val
    hits = []
    home = os.getenv("HOME")
    for root, dirs, files in os.walk(home):
        if 'nmrfxstructure' in files:
            hits.append(os.path.join(root,'nmrfxstructure'))
    newest = None
    newestNum = 0
    for hit in hits:
        arr = hit.split('/')
        poss = arr[-2]
        if '-' not in hit:
            continue
	try:
	    num = float(''.join(poss.split('-')[-1].split('.')))
	except:
	    continue
        if num > newestNum:
            newest = hit
            newestNum = num
    return newest


def get_indices(index, max_values):
    ''' This function returns a list of length equal to len(max_values). It
        provides indexing that can point to values stored in another array
        simply by using a single index value.
    '''
    indices = []
    index_ranges = [reduce((lambda x, y: x * y), max_values[i+1:]) for i in range(len(max_values[:-1]))]
    if len(max_values) == 1:
        return [index]
    for index_range in index_ranges:
        i = index / index_range
        index -= (index_range * i)
        indices.append(i)
        if len(indices) == len(max_values) - 1:
            indices.append(index)
            return indices
    return indices

def prepare_yaml(anneal_dict, infile = './partial.yaml', outfile = './project.yaml'):
    from shutil import copyfile
    copyfile(infile, outfile)
    with open(outfile,'a') as project_file:
        project_file.write('\n')
        project_file.write('anneal : \n')
        lines = ['    ' + key + " : " + str(value) for key,value in anneal_dict.iteritems()]
        anneal_text = '\n'.join(lines)
        project_file.write(anneal_text)

if __name__ != 'auxillary_funcs':
    # this indicates an import is not being done and this code is
    # being run as a subprocess.
    sys.argv.pop(0)
    method = sys.argv.pop(0)
    args = sys.argv
    method_dict = {'read_yaml' : read_yaml}
    method = method_dict[method]
    print method(*args)
