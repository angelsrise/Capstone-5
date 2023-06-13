#!/bin/bash

# Check if the OS is Linux
if [[ "$(uname)" == "Linux" ]]; then
    echo "Linux operating system detected."
    
# Check if the OS is macOS
elif [[ "$(uname)" == "Darwin" ]]; then
    echo "macOS operating system detected."

# Check if the OS is Windows (using WSL)
elif grep -qEi "(Microsoft|WSL)" /proc/version &> /dev/null; then
    echo "Windows Subsystem for Linux detected (WSL)."

# If none of the above, assume it's another Unix-like system
else
    echo "Unknown or unsupported operating system."
fi

