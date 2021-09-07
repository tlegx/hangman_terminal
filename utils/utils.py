''' a simple utility functions. '''
import os
import platform

# Mappers
_os_command_mapper = {'clear':{'Windows':'cls', 'Linux':'clear'}}

def clear_screen(os_name='linux'):
    try:
        cmd = _os_command_mapper['clear'][platform.system()]
        assert isinstance(cmd, str), 'command should be string.'
        os.system(cmd)
    except KeyError as ke:
        raise KeyError(f'os {platform.system()} not found in os command mapper!!')