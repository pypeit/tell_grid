# tell_grid
Generates the telluric absorption grids used by PypeIt.
Telluric models are computed by the Line-by-Line Radiative Transfer Model (LBLRTM; https://github.com/AER-RC/LBLRTM) called via the python-based TelFit interface (Gullikson et al. 2014; https://github.com/kgullikson88/Telluric-Fitter).

The scripts are designed for running many instances of TelFit on a many-core server machine. The general procedure is:

1. python prepare_tell_runs.py [Observatory] > tell_runs.sh

2. Run all of the command line entries in tell_runs.sh

3. 