import os


def touch(file_name):
    if not os.path.exists(file_name):
        create_file(file_name)


def create_file(file_name):
    with open(file_name, 'w'):
        pass


def write_file(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)


def is_empty_file(file_name):
    return os.stat(file_name).st_size == 0


def is_not_empty_file(file_name):
    return not is_empty_file(file_name)


def exists_file(file_name):
    return os.path.exists(file_name) and os.path.isfile(file_name)


def get_file_ext(file_name):
    return os.path.splitext(file_name)[1]