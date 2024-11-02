You're absolutely right, and I apologize for the omission. Here's the updated README, now including the main usage instructions as you've described.

---

# Folder Structure Duplicator

A Python application with a Tkinter GUI that allows users to select a source folder and duplicate its folder structure to a destination folder. The application supports optional depth specification for subdirectories. This README provides instructions for setting up, running, and packaging the application into standalone executables for both macOS and Windows using PyInstaller.

---

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
  - [macOS](#macos)
  - [Windows](#windows)
- [Packaging the Application](#packaging-the-application)
  - [macOS Application (.app)](#macos-application-app)
  - [Windows Executable (.exe)](#windows-executable-exe)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [License](#license)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)
- [Version History](#version-history)
- [Further Development](#further-development)

---

## Features

- **Folder Selection**: Easily select source and destination folders using a GUI.
- **Optional Depth Specification**: Specify the maximum depth of subdirectories to duplicate.
- **User-Friendly Interface**: Simple steps to duplicate folder structures.
- **Cross-Platform**: Works on both macOS and Windows.
- **Standalone Executables**: Package the application into a `.app` for macOS and `.exe` for Windows.

---

## Prerequisites

- **Python 3.x** installed on your system.
- **pip** (Python package installer).
- **PyInstaller** for packaging the application.
- **Tkinter** library (usually included with Python).

---

## Setup Instructions

### macOS

1. **Install Python 3** (if not already installed):

   Download and install Python 3 from the [official website](https://www.python.org/downloads/mac-osx/).

2. **Verify Python Installation**:

   ```bash
   python3 --version
   ```

3. **Install Required Packages**:

   ```bash
   pip3 install pyinstaller
   ```

4. **Download the Source Code and Icon**:

   - Place `folder.py` and `AppIcon.icns` in a project directory.

### Windows

1. **Install Python 3** (if not already installed):

   Download and install Python 3 from the [official website](https://www.python.org/downloads/windows/).

2. **Verify Python Installation**:

   ```batch
   python --version
   ```

3. **Install Required Packages**:

   ```batch
   pip install pyinstaller
   ```

4. **Download the Source Code and Icon**:

   - Place `folder.py` and `foldericon.ico` in a project directory (e.g., `C:\Users\YourName\Downloads`).

---

## Packaging the Application

### macOS Application (.app)

#### Steps:

1. **Navigate to Project Directory**:

   ```bash
   cd /path/to/your/project
   ```

2. **Build the Application Using PyInstaller**:

   ```bash
   pyinstaller --noconfirm --onefile --windowed --icon=AppIcon.icns --name="Folder Structure Duplicator" folder.py
   ```

3. **Locate the Application**:

   The `.app` file will be located in the `dist` directory:

   ```
   /path/to/your/project/dist/Folder Structure Duplicator.app
   ```

4. **Test the Application**:

   Double-click the `.app` file to ensure it runs correctly.

#### Notes:

- **Icon File**: Ensure `AppIcon.icns` is in the project directory.
- **Dependencies**: PyInstaller automatically includes required modules.

---

### Windows Executable (.exe)

#### Steps:

1. **Navigate to Project Directory**:

   ```batch
   cd C:\Users\YourName\Downloads
   ```

2. **Build the Executable Using PyInstaller**:

   ```batch
   pyinstaller --noconfirm --onefile --windowed --icon=foldericon.ico --name="FolderDuplicator" folder.py
   ```

3. **Locate the Executable**:

   The `.exe` file will be located in the `dist` directory:

   ```
   C:\Users\YourName\Downloads\dist\FolderDuplicator.exe
   ```

4. **Test the Executable**:

   Double-click the `.exe` file to ensure it runs correctly.

#### Notes:

- **Icon File**: Ensure `foldericon.ico` is in the project directory.
- **Dependencies**: PyInstaller automatically includes required modules.

---

## Usage

Follow these steps to use the Folder Structure Duplicator application:

1. **Select Source Folder**:

   Click the **"Select Source Folder"** button to choose the folder whose structure you want to duplicate.

2. **Select Destination Folder**:

   Click the **"Select Destination Folder"** button to choose where the duplicated folder structure will be created.

3. **Set Max Depth**:

   Enter the maximum depth of subdirectories to include. Enter `0` for unlimited depth.

4. **Start Duplication**:

   Click the **"Start Duplication"** button to begin the process.

---

## Troubleshooting

### Common Issues

#### Application Doesn't Launch

- **macOS**: If you encounter a security warning, right-click the `.app` file, select **Open**, and confirm.
- **Windows**: If SmartScreen blocks the app, click **More info** and then **Run anyway**.

#### Icon Not Displaying

- Verify the icon file is in the correct format (`.icns` for macOS, `.ico` for Windows).
- Ensure the icon file is specified correctly in the PyInstaller command.

#### Missing Modules

- If the application crashes due to missing modules, include them using `--hidden-import`:

  ```bash
  pyinstaller --hidden-import=module_name ...
  ```

#### Error Messages

- **macOS**: Run the app from Terminal to view error messages:

  ```bash
  ./dist/Folder\ Structure\ Duplicator.app/Contents/MacOS/Folder\ Structure\ Duplicator
  ```

- **Windows**: Run the executable from Command Prompt:

  ```batch
  cd dist
  FolderDuplicator.exe
  ```

### Clean Up Build Files

After building and testing, you may remove unnecessary files:

- **macOS**:

  ```bash
  rm -rf build
  rm Folder\ Structure\ Duplicator.spec
  ```

- **Windows**:

  ```batch
  rd /S /Q build
  del FolderDuplicator.spec
  ```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For any questions or support, please contact:

- **Email**: [your.email@example.com](mailto:your.email@example.com)
- **GitHub**: [YourGitHubUsername](https://github.com/YourGitHubUsername)

---

## Acknowledgments

- **PyInstaller**: For packaging Python applications.
- **Tkinter**: For the GUI library.
- **Contributors**: Thanks to everyone who contributed to this project.

---

## Version History

- **v1.0** (Date):

  - Initial release with macOS and Windows support.

---

## Further Development

- **Linux Support**: Plans to add support for Linux distributions.
- **Features**:

  - Add an option to copy files along with the folder structure.
  - Implement a progress bar for large folder structures.

---

Thank you for using the Folder Structure Duplicator! If you find this tool helpful, please consider contributing or leaving feedback.

---

Feel free to let me know if there's anything else you'd like me to include or adjust!
