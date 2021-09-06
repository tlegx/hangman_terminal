''' a simple utility functions. '''
import os

# Mappers
_os_command_mapper = {'clear':{'windows':'cls', 'linux':'clear'}}

def clear_screen(os_name='linux'):
    try:
        cmd = _os_command_mapper['clear'][os_name]
        assert isinstance(cmd, str), 'command should be string.'
        os.system(cmd)
    except KeyError as ke:
        raise KeyError(f'os {os_name} not found in os command mapper!!')
