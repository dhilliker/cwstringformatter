GUIDE: SETTING UP YOUR KENWOOD TS-590SG MORSE FORMATTER

This guide describes how to install Python and use a formatting script to overcome the 24-character CAT command limit on the Kenwood TS-590SG.

I. INSTALLING PYTHON

If you do not have Python installed on your computer, follow these steps:

1. Download: Visit [https://www.python.org/downloads/](https://www.python.org/downloads/) and click the button to download the latest version for Windows.

2. Install: Run the downloaded installer.
IMPORTANT: On the first screen of the installer, check the box that says "Add Python to PATH." This is required to run the script from the command line.
Choose "Install Now" and wait for the process to complete.

3. Verify: Open the Windows Start Menu, type "cmd" and press Enter. In the command-line window that opens, type "python --version" and press Enter. If you see "Python 3.x.x," the installation was successful.

II. INSTALLING THE CLIPBOARD MODULE

Python needs a specific library to interact with your Windows clipboard.

1. Open the Command Prompt (type "cmd" in the Start Menu).
2. Type the following command and press Enter:
   pip install pyperclip
3. Close the window once the installation finishes.

III. DOWNLOADING THE SCRIPT FILE

1. If you're not already on GitHub, browse to https://github.com/dhilliker/cwstringformatter to access the CW String Formatter repository.
2. Select Releases and then Latest to download the file.

IV. OPERATING THE FORMATTER

1. Select and copy the text you wish to transmit (Ctrl+C).
2. Press the Start menu, type "cmd" and press enter to open a command-line window. Other similar tools, such as PowerShell, may be used and administrator access is not recommended or required.
2. Type "python cwstringformatter.py" and press enter to run the script.
3. If you have already copied the text, simply press Enter. The script will grab the text from your clipboard automatically.
4. The script will format the text into 24-character segments, apply the "RI:KY " and "KY " prefixes, and copy the result back to your clipboard.
5. Open your logging or other software that relies on CAT control (like the Amateur Contact Log by N3FJP) and paste (Ctrl+V) the string into the command window to send it to your TS-590SG.
