@echo off

rm -r dist/
py setup.py sdist bdist_wheel
twine upload dist/*
