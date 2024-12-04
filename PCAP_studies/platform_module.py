# Operating System Details
# Write a program to display the current OS name, version, and architecture (machine type).
import platform
print(platform.system())
print(platform.version())
print(platform.machine())
# Python Version
# Create a script that checks and prints the Python version currently running.
print(platform.python_version())
# System Information
# Write a program to combine and display details about the OS, processor, and Python implementation (using platform.processor() and platform.python_implementation()).
print(platform.processor())
print(platform.python_implementation())