import sys

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
    if verbose:
        print(open(outfile).read())
    print("=======================================\n\n")
    
    
if __name__ == '__main__':

    for arg in sys.argv[1:]:
        testcase, path = arg.split(":", 1)
        check_file(path, desc=testcase, verbose=True)
