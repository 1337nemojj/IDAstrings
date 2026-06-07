# IDAstrings

Small helper for filtering strings exported from IDA-related reverse engineering workflows.

## Safety Notice

Use this utility only for files and binaries you are allowed to analyze.
Do not use the workflow to process proprietary, third-party, or malware samples unless you have permission and an isolated analysis environment.

## Usage

The script reads a text file name from stdin, then prompts for a starting string pattern and a substring to highlight in matching rows.
