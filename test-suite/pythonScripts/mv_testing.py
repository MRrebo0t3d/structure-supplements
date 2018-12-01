import sys
def get_config_data(configFile):
    ''' This function uses nmrfx's yaml parser to read in a testing config file.
        as a python object. This object can be parsed to run the tests specified
        in the original config
    '''
    import subprocess, re, ast, os
    from auxillary_funcs import find_compiled_struct
    env = find_compiled_struct()
    os.environ['DSTRUCTURE'] = env
    pyscript = os.path.join(os.environ['PYPATH'], 'auxillary_funcs.py')
    configStr = subprocess.check_output([env, pyscript,'read_yaml',configFile])
    configStr = re.sub(r"([\w\./~]+)", r"'\1'", configStr)
    configStr = re.sub("=", ":", configStr)
    configDict = ast.literal_eval(configStr)
    return (configDict, env)

def parse_molecules(mol_dict):
    ''' This will return a dictionary of molecule names as keys and values
        as either empty dictionaries or dictionaries of run type to
        datapath where the data is collected. That is, if data is already
        prepared, the dictionary stored for that molecule will have paths to
        the prepared data.
    '''
    import os
    if 'dir' in mol_dict:
        path = mol_dict['dir']
        mol_list = [dir for dir in os.listdir(path) if os.path.isdir(dir)]
        return {mol_name:os.path.join(os.getcwd(),mol_name) for mol_name in mol_list}

def parse_testing(test_dict):
    ''' This scans through the testing dictionary and finds what variables
        are being held constant and what is being varied. Returns
        two dictionaries, consts and vars. Consts has a key value pairing of
        parameters to the value used. If a list was provided, the parameter will
        be within the consts dict but the value will be 'var' to indicate a value
        should be looked up when running the batches. Vars has a key value
        pairing of parameters to a list of the different values tested.
    '''
    use_mol_prob = test_dict.get('molprobity')
    if use_mol_prob and use_mol_prob.lower() == 'true':
        use_mol_prob = True
        import subprocess
        failure = subprocess.call('checkpath')
        if failure:
            ### Here we terminate the program if molprobity is requested but
            ### not found
            raise ImportError("Molprobity was not found in the path")
        del(test_dict['molprobity'])
    else:
        if use_mol_prob:
            del(test_dict['molprobity'])
        use_mol_prob = False

    consts = test_dict
    consts['molprob'] = use_mol_prob
    vars = {}
    def find_lists(test_dict):
        for key in test_dict:
            value = test_dict[key]
            if type(value) is dict:
                return find_lists(value)
            elif type(value) is list:
                vars[key] = value
                test_dict[key] = 'var'
    find_lists(consts)
    return consts, vars

def parse_batch(batch_dict):
    ''' This file returns a string that can be used to execute a batch run of
        nmrfxstructure from a batch_dict. Currently this only supports the
        command flags of a, n, p and k.
    '''
    defaults = {
        'a' : 'False',
        'n' : '100',
        'p' : '4',
        'k' : '20'
    }
    flags = defaults.keys()
    vals = {}
    if not batch_dict:
        batch_dict = {}
    for flag in flags:
        val = batch_dict.get(flag, defaults[flag])
        if (val.lower() == 'false'):
            val = False
        elif (val.lower() == 'true'):
            val = True
        vals[flag] = val
    cmd_string = ""
    for flag, value in vals.iteritems():
        flag = '-'+flag
        if value:
            if type(value) is bool:
                value = ""
            else:
                value = str(value) + ' '
            cmd_string += ' '.join([flag,value])
    cmd_string = 'batch ' + cmd_string + ' project.yaml'
    return cmd_string

def make_dir_name(params, indices):
    data = zip(params,indices)
    data = reduce(lambda x, y : x + y, data)
    data = reduce(lambda x, y : str(x) + str(y), data)
    return data


def run_batch(cmd, dir_name):
    ''' This function executes a single batch of structures by opening up a
        subprocess using the nmrfx engine specified. This method is called
        once it is in the same subdirectory as the executable yaml file
    '''
    import subprocess
    import os
    import shutil
    os.mkdir(dir_name)
    cmd = cmd.split()
    subprocess.call(cmd)
    subprocess.call(['batch_cleanup', dir_name])


class MVTest:
    def __init__(self, file):
        ''' The MVTest is initalized using a config dictionary. The initalizer
            sets up the number of tests that will be run and makes sure
            the path has everything it needs to execute the full tests. If not,
            the test is terminated immediately to prevent wasted time.
        '''
        self.config, self.default = get_config_data('test.yaml')
        self.initialize()
        self.run_batches()

    def initialize(self):
        ''' Initalizes the MVTest object by parsing the config dict '''
        self.molecules = parse_molecules(self.config.get('molecules'))
        self.consts, self.vars = parse_testing(self.config.get('testing'))
        self.batch_string = parse_batch(self.config.get('batch'))

    def run_batches(self):
        ''' Iterates over the various tests and executes the batch command '''
        import os
        from auxillary_funcs import get_indices
        from auxillary_funcs import prepare_yaml

        base_dir = os.getcwd()
        test_params = self.vars.keys()
        test_sizes = [len(self.vars[test_param]) for test_param in test_params]
        tot_size = reduce((lambda x, y: x*y),test_sizes)
        for mol_name in self.molecules:
            os.chdir(self.molecules[mol_name])
            for i in range(tot_size):
                # These indices is a list of index numbers to access the requested
                # variation for each parameter tested. To relate the value
                indices = get_indices(i, test_sizes)
                envI = test_params.index('version') if 'version' in test_params else - 1
                envI = -1 if envI == -1 else indices[envI]
                env = os.environ['DSTRUCTURE'] if envI == -1 else self.vars['version'][envI]
                for var in self.vars:
                    if var == "version":
                        continue
                    varI = test_params.index(var)
                    varI = indices[varI]
                    value = self.vars[var][varI]
                    self.consts['anneal'][var] = value
                prepare_yaml(self.consts['anneal'],'partial.yaml', 'project.yaml')
                cmd = ' '.join([env,self.batch_string])
                dir_name = make_dir_name(test_params, indices)
                run_batch(cmd,dir_name)

try :
    file = sys.argv[0]
except IndexError:
    raise IndexError("Please provide a file name for testing")

mvTest = MVTest(file)
