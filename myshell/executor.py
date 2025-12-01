import subprocess
import sys
from .builtins import is_builtin, execute_builtin


def execute_command(command):
    if not command or not command.program:
        return
    
    if is_builtin(command.program):
        execute_builtin(command.program, command.args)
        return
    
    if command.pipe_to:
        try:
            from .piper import execute_pipeline
            execute_pipeline(command)
        except ImportError:
            print("Error: Pipeline functionality not yet implemented", file=sys.stderr)
        return


    if command.input_file or command.output_file:
        try:
            from .redirector import execute_with_redirect
            execute_with_redirect(command)
        except ImportError:
            print("Error: Redirection functionality not yet implemented", file=sys.stderr)
        return
    

    _execute_external(command)


def _execute_external(command):


    try:

        process = subprocess.Popen(
            command.args,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        

        if command.background:
            print(f"[Background] PID: {process.pid}")
            return
        

        stdout, stderr = process.communicate()
        

        if stdout:
            print(stdout, end='')
        
        if stderr:
            print(stderr, end='', file=sys.stderr)
            
    except FileNotFoundError:
        print(f"{command.program}: command not found", file=sys.stderr)

    except PermissionError:
        print(f"{command.program}: Permission denied", file=sys.stderr)

    except Exception as e:
        print(f"Error executing {command.program}: {e}", file=sys.stderr)