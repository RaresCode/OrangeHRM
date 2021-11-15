import os
browser = input("Choose a browser: ")
report = input("Generate html report?: ")
test_type = input("Sanity, Regression or both?: ")
run_paralel = input("Run tests in parallel?: ")


if report.lower() == "yes":
    report = "--html=../Reports/report.html"
else:
    report = ""

if test_type.lower() == "sanity":
    test_type = "-m sanity"
elif test_type.lower() == "regression":
    test_type = "-m regression"
else:
    test_type = ""

if run_paralel.lower() == "yes":
    run_paralel = "-n=3"
else:
    run_paralel = ""

command = "cd TestCases & pytest -v -s {0} {1} {2} ../TestCases/ --browser {3}".format(run_paralel, test_type, report, browser.lower())
os.system(command)