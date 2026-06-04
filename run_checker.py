from compliance_checker.runner import CheckSuite, ComplianceChecker


def check_file(filename, desc='', verbose=False):

    check_suite = CheckSuite()
    check_suite.load_all_available_checkers()

    config = {
        "test": ["wcrp_cmip7:1.0", "cf:1.11"],
        "criteria": "lenient",
        "include_checks": None,
        "skip_checks": None,
    }
    outfile = "checker.out"
    
    return_value, errors = ComplianceChecker.run_checker(
        {filename},
        config["test"],
        verbose,
        config["criteria"],
        config["skip_checks"],
        config["include_checks"],
        outfile,
        ["text"]
    )
    print(f"================= {desc} ===============")
    print(f"RET={return_value} ERRS={errors}")
    #print(open(outfile).read())
    print("=======================================\n\n")
    

def get_paths():
    filename = "tas_tavg-h2m-hxy-u_mon_glb_g999_DUMMY-MODEL_1pctCO2_r1i1p1f3_185001-199912.nc"
    return {"good": f"testdata/orig/{filename}",
            "warn": f"testdata/warn/{filename}",
            "fail": f"testdata/fail/{filename}"}
    
    
if __name__ == '__main__':
    paths = get_paths()
    for testcase in "good", "warn", "fail":
        check_file(paths[testcase], desc=testcase)
