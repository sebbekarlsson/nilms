from nilms.config import config
from nilms.random_utils import get_random_string
import os


def upload_file(_file):
    if not _file:
        raise Exception('No file was sent')

    if not _file.filename:
        raise Exception('Filename is empty')

    if not os.path.isdir(config['uploads_dir']):
        os.mkdir(config['uploads_dir'])

    filename, extension = os.path.splitext(_file.filename)

    new_name = get_random_string(length=24) + extension
    new_name_full = os.path.join(
        config['uploads_dir'],
        new_name
    )

    _file.save(new_name_full)

    return new_name


def get_file_type(filename):
    fname, extension = os.path.splitext(filename)
    extension = extension.lower()

    if extension in [
        '.jpg',
        '.png',
        '.gif',
        '.bmp',
        '.jpeg'
    ]:
        return 'image'

    if extension in [
        '.html',
        '.htm'
    ]:
        return 'html'

    if extension in [
        '.exe',
        '.out'
    ]:
        return 'executable'

    if extension in [
        '.dll',
        '.so',
        '.a',
        '.dylib'
    ]:
        return 'binary'

    if extension in [
        '.zip',
        '.rar',
        '.tar.gz',
        '.tar',
        '.gz'
    ]:
        return 'archive'

    return 'unknown'
