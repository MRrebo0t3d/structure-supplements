import urllib, re


def fetch_files():
    home_pg_url = r'http://restraintsgrid.bmrb.wisc.edu/NRG/'
    path_prefix = r'MRGridServlet?db_username=wattos1&format=n%2Fa&'

    def request_pdbid():
        pdb_id = raw_input("What is the PDB ID of the structure whose files you wish to download? \n")
        pat = re.compile(r'([1-9][a-z0-9]{3})', re.I)
        mat = pat.search(pdb_id)
        if mat:
            sel = mat.group(1)
            if sel == pdb_id:
                return sel
        else:
            raise ValueError("The PDB ID provided is either not correct or can't be found!")

    pdb_id = request_pdbid()
    program = r'&program=XPLOR'
    gen_dis_suffix = r'%2FCNS&request_type=block_set&subtype=general+distance&type=distance'
    dih_suffix = r'%2FCNS&request_type=block_set&subtype=n%2Fa&type=dihedral+angle'

    gen_dis_url = home_pg_url+path_prefix+pdb_id+program+gen_dis_suffix
    dih_url = home_pg_url+path_prefix+pdb_id+program+dih_suffix

    def read_url(url):
        f = urllib.urlopen(url)
        html = f.read()
        # pat =
        return html
    return read_url(dih_url)


print fetch_files()

# self.home_pg_url self.dih_href = r'MRGridServlet?db_username=wattos1&format=n%2Fa&pdb_id={0}&program=XPLOR%2FCNS&request_type=block_set&subtype=n%2Fa&type=dihedral+angle'.format(self.request_pdbid())
# self.gen_dis_href = r'MRGridServlet?db_username=wattos1&format=ambi&pdb_id={0}&program=XPLOR%2FCNS&request_type=block_set&subtype=general+distance&type=distance'.format(self.request_pdbid())
