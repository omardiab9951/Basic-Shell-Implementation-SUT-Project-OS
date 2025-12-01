from myshell.builtins import *

# Test pwd
cmd_pwd(['pwd'])

# Test cd with Windows path
cmd_cd(['cd', 'C:\\'])  # Go to C: drive root
cmd_pwd(['pwd'])  # Verify it worked

# Test cd with relative path
cmd_cd(['cd', '..'])  # Go up one directory
cmd_pwd(['pwd'])

# Test cd with no arguments (goes to HOME)
cmd_cd(['cd'])
cmd_pwd(['pwd'])

# Test echo
cmd_echo(['echo', 'Hello', 'from', 'Windows'])