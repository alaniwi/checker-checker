drsdirs=MIP-DRS7/CMIP7/CMIP/MOHC/DUMMY-MODEL/1pctCO2/r1i1p1f3/glb/mon/tas/tavg-h2m-hxy-u/g999/v20260401
fname=tas_tavg-h2m-hxy-u_mon_glb_g999_DUMMY-MODEL_1pctCO2_r1i1p1f3_185001-199912.nc

urlbase=https://gws-access.jasmin.ac.uk/public/mohc_shared/msmizielinski/
url=$urlbase/$drsdirs/$fname

good_data_dir=testdata/orig/$drsdirs
warn_data_dir=testdata/warn/$drsdirs
fail_data_dir=testdata/fail/$drsdirs

good_path=$good_data_dir/$fname
warn_path=$warn_data_dir/$fname
fail_path=$fail_data_dir/$fname

