import os
import platform
import sys
from datetime import datetime


from time import gmtime, strftime


if sys.platform == 'linux':
    desktop_path = os.path.expanduser("~/Desktop")
else:
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')


def get_platform_n_time(linux):
    if linux:
        return f"{'Platform :' +platform.platform()}\n\n" \
               f"{datetime.today().strftime('%d-%m-%y ')} " \
		f"{datetime.now().strftime('%I:%M %p')} " \
		f"{strftime('%z', gmtime())} "\
		f"{datetime.today().strftime('%y')}\n " 
    else:
        return f"{'Platform :' +platform.platform()}\n" \
               f"{datetime.today().strftime('%d-%m-%y')}\n" \
               f"{datetime.now().strftime('%I:%M %p')}"


def write_log_file(fixed_lines, file_type):
    def get_all_files():
        for dir_path, dir_name, file_names in os.walk(loc):
            for file in file_names:
                if os.path.splitext(file)[1] == file_type:
                    paths.add(os.path.join(dir_path, file))

    def delete_if_exists():
        if os.path.exists(write_location):
            os.remove(write_location)

    def append_log(lines=None):
        with open(write_location, 'a') as file:
            if not lines:
                for path_loc in paths:
                    file.write(path_loc + '\n')
            else:
                for line in lines:
                    file.write(line + '\n')

    paths = set()
    if file_type == '.bin':
        loc = "/lib"
        write_location = os.path.join(desktop_path, 'entries_Lin.log')
        get_all_files()
    elif file_type == '.exe':
        loc = "C:\\Windows\\System32"
        write_location = os.path.join(desktop_path, 'entries_Win10.log')

    delete_if_exists()
    append_log(fixed_lines)
    append_log()


def for_linux_platform():
    first_2_lines = get_platform_n_time(linux=True)
    write_log_file([first_2_lines], '.bin')


def for_windows_platform():
    first_2_lines = get_platform_n_time(linux=False)
    res = os.popen('dir /S *.exe')
    data = res.read().split('\n')

    lines = [first_2_lines]
    lines.extend(data)
    write_log_file(lines, '.exe')


if __name__ == '__main__':
    if sys.platform == 'linux':
        for_linux_platform()
    else:
        for_windows_platform()
