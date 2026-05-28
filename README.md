# CodingStandardsDevs

This is the first workshop of Software Engineering II, in order to practice Clean Code and Best practices

# How to generate a pylint report

pip install pylint
pip install pylint-report
pip install pylint-json2html
pylint test.py --output-format=json > report.json
pylint-json2html -f json -o report.html report.json
