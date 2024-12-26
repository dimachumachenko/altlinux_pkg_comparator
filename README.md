ALT Linux Package Comparator
Description
This Python project provides a command-line utility to compare binary packages between two branches (sisyphus and p10) of the ALT Linux repository. The tool fetches package lists via the ALT Linux public REST API and identifies:

Packages available in p10 but not in sisyphus
Packages available in sisyphus but not in p10
Packages with a higher version-release in sisyphus compared to p10
The output is presented as a JSON structure and includes results for all supported architectures.

Requirements
Python 3.8 or higher
ALT Linux 10 (or any Linux distribution with Python support)

Installation


Clone the repository:

git clone https://github.com/dimachumachenko/altlinux_pkg_comparator.git
cd altlinux_pkg_comparator

(Optional but recommended) Create a virtual environment:

python -m venv venv
source venv/bin/activate


Install dependencies:
 pip install -r requirements.txt

 Usage

 Run the CLI utility:
 python cli.py
