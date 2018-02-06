import os
from nilms.app import app
import flask_assets


STATIC_DIR = 'nilms/static'


def run():
    try:
        env = flask_assets.Environment(app)

        env.load_path = [
            os.path.join(os.path.dirname(__file__), '{STATIC_DIR}/js'.format(
                STATIC_DIR=STATIC_DIR
            ))
        ]

        env.register(
            'js_all',
            flask_assets.Bundle(
                'medium-editor.min.js',
                'utils.js',
                'app.js',
                filters=['jsmin'],
                output='js/packed.js'
            )
        )

        app.run(debug=True, threaded=True)

    except KeyboardInterrupt:
        quit()


run()
