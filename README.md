# TI-84 Apps

Collection of small programs and utilities for TI‑84 calculators.

This repository contains Python source files intended for use with TI‑84 Plus CE Python calculators (or other TI devices that support Python). The repository is written in Python.

Language composition: Python (100%)

## Requirements

- A TI‑84 calculator that supports Python (TI‑84 Plus CE Python or equivalent).
- A USB cable to connect your calculator to your computer.
- TI Connect™ CE (Texas Instruments) installed on your computer to transfer files between your computer and the calculator. Download from Texas Instruments' website.

Notes:
- Make sure your calculator has the latest operating system and the Python app installed.
- If your calculator does not support Python, you'll need TI‑BASIC (.8xp) programs instead — this repository is focused on Python files.

## How to add these programs to your calculator (TI‑84 Plus CE Python)

1. Install TI Connect CE on your computer (Windows or macOS).
2. Connect the calculator to your computer with a USB cable.
3. Open TI Connect CE and choose "Calculator Explorer" (or the device explorer view).
4. In Calculator Explorer, open the Python folder on the device.
5. Drag the .py file(s) from this repository into the calculator's Python folder, or use the "Send to Device" option.
6. Safely eject the calculator from TI Connect CE.
7. On the calculator: open the Python app, navigate to "My Programs", select the program you transferred, and press Enter to run it.

Troubleshooting tips:
- If the program does not appear on the calculator, try reconnecting the device and using "Refresh" in Device Explorer.
- If you get an OS or Python-related error on the calculator, ensure the calculator's OS and Python app are up to date.

## Adding .8xp (TI‑BASIC) programs

This repository primarily contains Python files for TI‑Python. If you need classic TI‑BASIC (.8xp) files:

- Use TI Connect CE (or TI‑Graph Link) to send .8xp files to older TI‑84 models.
- In TI Connect CE: open Calculator Explorer → Programs or the appropriate folder → "Send to Device" and choose the .8xp file.
- On the calculator: press the PRGM key, find your program, and press ENTER to run it.

There is no automatic in-repo converter from Python to TI‑BASIC included here. Converting Python code to TI‑BASIC typically requires manual porting or a third-party conversion tool.

## Running code locally

Some scripts in this repository may be runnable on your computer (for testing or generating assets). If a requirements.txt or setup instructions are included in the repo, install dependencies with:

```
python3 -m pip install -r requirements.txt
```

Run local scripts with:

```
python3 script_name.py
```

(Remember that code intended for the calculator may use modules or features specific to the TI‑Python environment and may not run unchanged on your PC.)

## Contributing

Contributions are welcome. Please:

- Open an issue to propose new apps or report bugs.
- Fork the repo, make changes, and open a pull request with a clear description of what you changed and how to test it.

## License

Add a LICENSE file to the repo if you want to specify a license. If no license is present, assume the code is proprietary to the repository owner.

## Contact

If you want help adding a specific program to your calculator or need the program converted to another format, open an issue or contact the repository owner.
