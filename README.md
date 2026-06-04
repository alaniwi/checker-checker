Runs the compliance checker with a CMIP7 file that ought to be valid, using the checks that will be run in the ESGF publisher.

Three versions of the file are included (via download from JASMIN):
  - "good": the original test file supplied by MOHC
  - "warn": the file with the attribute `calendar` of variable `time` changed to `"JUNK"`
  - "fail": the file with the global attribute `experiment_id` changed to `"JUNK"`

This currently runs the following tests against each of the files, in "lenient" mode:
  - `wcrp_cmip7:1.0`
  - `cf:1.11`

and it reports the `return_value` and `errors` values that are returned by from `run_checker`.

It is hoped that `return_value` will be `True` for the "good" and "warn" files, but will be `False` for the "fail" file.

At present time (2026-06-04), this is _not_ the case.  A copy of the output is included in the repo.  (File `output_2026-06-04.txt`.)

## To run
```
git clone https://github.com/alaniwi/checker-checker.git
cd checker-checker
./RUN_ALL.sh
```
