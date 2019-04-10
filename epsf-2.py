from astropy.visualization import simple_norm
from photutils import datasets

hdu = datasets.load_simulated_hst_star_image()
data = hdu.data
from photutils.datasets import make_noise_image
data +=  make_noise_image(data.shape, type='gaussian', mean=10.,
                          stddev=5., random_state=12345)

from photutils import find_peaks
peaks_tbl = find_peaks(data, threshold=500.)

from astropy.table import Table
stars_tbl = Table()
stars_tbl['x'] = peaks_tbl['x_peak']
stars_tbl['y'] = peaks_tbl['y_peak']

from astropy.stats import sigma_clipped_stats
mean_val, median_val, std_val = sigma_clipped_stats(data, sigma=2.,
                                                    iters=None)
data -= median_val

from astropy.nddata import NDData
nddata = NDData(data=data)

from photutils.psf import extract_stars
stars = extract_stars(nddata, stars_tbl, size=25)

import matplotlib.pyplot as plt
nrows = 5
ncols = 5
fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=(20, 20),
                       squeeze=True)
ax = ax.ravel()
for i in range(nrows*ncols):
    norm = simple_norm(stars[i], 'log', percent=99.)
    ax[i].imshow(stars[i], norm=norm, origin='lower', cmap='viridis')