#!env bash

echo Run as main
python main.py
echo
echo Run module that does sibling import
python -m mod.function
