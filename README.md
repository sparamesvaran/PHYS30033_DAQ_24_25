# `PHYS30033 Pico DAQ`

This repository includes a project showing an example of how to use Raspberry Pi Pico functionality in a DAQ context.

## Build instructions

### Using the VS Code with the Pico Extension
1. Install VS Code and relevant dependencies by following the instructions in Chapter 2 and 3 of the [Raspberry Pi Pico Getting Started Guide](https://datasheets.raspberrypi.com/pico/getting-started-with-pico.pdf).

    1. If using Windows, download [git for Windows](https://git-scm.com/downloads/win), which will give you access to git commands and bash emulation. Alternatively, you could use the Windows Subsystem for Linux.
2. Create, and move into a project directory for the DAQ Lab.
```
mkdir pico_daq_lab
cd pico_daq_lab
```
3. Get a copy of the Pico DAQ repository:
```
git clone https://github.com/sparamesvaran/PHYS30033_DAQ_24_25.git
cd PHYS30033_DAQ_24_25
```

4. Import the newly cloned project using the Raspberry Pi Pico extension.
    1. Open the extension from the right-hand toolbar
    2. Click `Import Project`, and set the `Location` field to the correct directory of the cloned DAQ repository. 
    3. Click `Import`. A new window should open, and VS Code will begin to download the Pico SDK and requisite tools.

5. Build the DAQ project by clicking the `Compile` button in the blue ribbon of VS Code, which should now be available. The compilation output should now be under `build/onboard_temp_daq`.

### Using VS Code with cmake
1. Install VS Code and the dependencies listed below:
    - Windows
        1. [git for Windows](https://git-scm.com/downloads/win), which will give you access to git commands and bash emulation. Alternatively, you could use the Windows Subsystem for Linux.
        
        2. [ARM GCC compiler](https://developer.arm.com/-/media/Files/downloads/gnu/12.2.rel1/binrel/arm-gnu-toolchain-12.2.rel1-mingw-w64-i686-arm-none-eabi.exe?rev=4eb1b321a6f44ca78be67eb9cef8b37a&hash=AD35FDA3E92F4D716B9C4FCF21A9B27F)
        
        ```
        N.B. During installation you should tick the box to register the path to the ARM compiler as an environment variable in the Windows shell when prompted to do so.
        ```
        3. [CMake](https://github.com/Kitware/CMake/releases/download/v3.31.4/cmake-3.31.4-windows-x86_64.msi)
        ```
        N.B. During the installation add CMake to the system PATH for all users when prompted by the installer.
        ```
        4. [Build Tools for Visual Studio 2022](https://aka.ms/vs/17/release/vs_BuildTools.exe)
        
        ```
        N.B. When prompted by the Build Tools for Visual Studio installer you need to install the C++ build tools only. You must install the full Windows 10 SDK package as the SDK will need to build the pioasm and elf2uf2 tools locally. Removing it from the list of installed items will mean that you will be unable to build Raspberry Pi Pico binaries.
        ```
2. Create, and move into a project directory for the DAQ Lab.
```
mkdir ~/pico_daq_lab
cd ~/pico_daq_lab
```
3. Get a copy of the Pico SDK
```
git clone -b 2.1.0 --recurse-submodules https://github.com/raspberrypi/pico-sdk.git
```
4. Get a copy of the Pico DAQ repository:
```
git clone https://github.com/sparamesvaran/PHYS30033_DAQ_24_25.git
cd PHYS30033_DAQ_24_25
```

5. Open a Developer Command Prompt Window from the Windows Menu, by selecting `Windows > Visual Studio 2022 > Developer Command Prompt`.
 
6. Open VS code, by typing `code` in your current Developer Command Prompt Window. Starting VS code in this way ensures that its build environment is configured properly.
 
7. Click the Extensions button (left-hand side), and install the `CMake Tools` extension by Microsoft.
 
8. Navigate to the `CMake Tools` extension settings, by clicking on `Manage -> Extensions -> CMake Tools`. Add an item under `Cmake Environment` to set the Pico SDK path, e.g.:
```
Key: PICO_SDK_PATH
Value: ~/pico_daq_lab/pico-sdk
```
9. Scroll down to `Cmake: Generator` and enter `NMake Makefiles` into the box.
 
10. In VS Code, open the `PHYS30033_DAQ_24_25` folder containing the repository cloned in previous steps.
 
11. Configure the project when prompted.
 
12. Select `GCC for arm-none-eabi` as the project kit.
 
13. Click `Build` to compile the code. The files which can be loaded on the Pico can be found under the build directory.

## Pico programming instructions

1. Hold down the `BOOTSEL` button on Pico
2. Plug the Pico micro-controler  into a computer using the micro-USB cable. A USB mass storage device, named `RPI-RP2` should appear.
3. Copy the desired `.uf2` file (e.g.: `build/onboard_temp_daq/onboard_temp_daq.uf2`) to `RPI-RP2` (i.e. the Pico). This should cause the Pico to reboot, and start running the code in the binary file.