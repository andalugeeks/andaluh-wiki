#!/bin/bash

python -c 'from app.proxy import flask_app; flask_app.run(debug=False, host="0.0.0.0", port=5000)'
