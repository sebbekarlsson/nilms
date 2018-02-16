from nilms.config import config
import os
import glob
import ntpath


def get_theme_templates():
    templates_dir = os.path.join(config['theme_dir'], 'templates')

    if os.path.isdir(templates_dir):
        query = os.path.join(templates_dir, '*.html')

        return [
            {'path': path, 'name': ntpath.basename(path)}
            for path in glob.glob(query)]
