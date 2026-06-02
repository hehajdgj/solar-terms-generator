# Solar terms generator

This python script takes in two arguments which are start year and end year then generates the solar terms
for the specified year, using the `skyfield` library.

It outputs a json file and a C++ header file which then can be used in esp32 projects.

# Getting started

## Requirements

* Python 3.9 or higher

## Creating a venv

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Installing requirements

Run the following command:

```bash
pip install -r requirements.txt
```

## Running the command

```bash
python main.py 2025 2026
```

_Note: The first time you run the script, Skyfield will automatically download the de421.bsp planetary ephemeris file from NASA. This is normal and required for the orbital math_

### Optional flags

With the `--json` and `--cpp` flags you can specify the output file names of the json file and cpp file respectively.

```bash
python main.py 2025 2026 --json outputfile.json --cpp outputfile.h
```