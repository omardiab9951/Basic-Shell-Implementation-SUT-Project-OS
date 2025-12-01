import os
import sys

BUILTINS = {}


def builtin(name):

    def decorator(func):
        BUILTINS[name] = func
        return func
    return decorator


def is_builtin(command):

    return command in BUILTINS


def execute_builtin(command, args):

    if command in BUILTINS:
        return BUILTINS[command](args)
    return False


@builtin("cd")
def cmd_cd(args):

    try:

        if len(args) <= 1:
            target_dir = os.environ.get('HOME', os.path.expanduser('~'))
        else:
            target_dir = args[1]
        

        os.chdir(target_dir)
        return True
        
    except FileNotFoundError:
        print(f"cd: {args[1] if len(args) > 1 else 'directory'}: No such file or directory", file=sys.stderr)
        return False
    except PermissionError:
        print(f"cd: {args[1]}: Permission denied", file=sys.stderr)
        return False
    except Exception as e:
        print(f"cd: {e}", file=sys.stderr)
        return False


@builtin("pwd")
def cmd_pwd(args):

    try:
        current_dir = os.getcwd()
        print(current_dir)
        return True
    except Exception as e:
        print(f"pwd: {e}", file=sys.stderr)
        return False


@builtin("exit")
def cmd_exit(args):

    exit_code = 0
    

    if len(args) > 1:
        try:
            exit_code = int(args[1])
        except ValueError:
            print(f"exit: {args[1]}: numeric argument required", file=sys.stderr)
            exit_code = 1
    
    sys.exit(exit_code)


@builtin("echo")
def cmd_echo(args):

    if len(args) > 1:
        output = ' '.join(args[1:])
        print(output)
    else:
        print()  
    
    return True