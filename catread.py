from astropy.io import ascii
from astropy.io import fits
from astropy.table import Table

def catread(clustname, photext):
    path = '/Users/k537n315/Work/GOGREEN/v1.0/PHOTOMETRY/'
    photfile = path + 'PHOTOM_CATS/' + clustname + '_totalall_' + photext + '.cat'
    photcat = ascii.read(photfile)
    
    speczfile = path + 'SPECZ_MATCHED/compilation_' + clustname + '.dat'
    speczcat = ascii.read(speczfile)
    
    restframefile = path + 'RESTFRAME_COLOURS/RESTFRAME_MASTER_' + clustname + '_indivredshifts.cat'
    restframecat = ascii.read(restframefile)
    return(photcat, speczcat, restframecat)
