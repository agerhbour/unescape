cd unescape
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

zip -r ../unescape.ankiaddon *