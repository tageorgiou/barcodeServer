import flask.ext.restless
from elixir import Date, DateTime, Field, Unicode
from elixir import ManyToOne, OneToMany
from elixir import create_all, metadata, setup_all
from sqlalchemy import create_engine
import os

class Tube(flask.ext.restless.Entity):
    contents = Field(Unicode)
    barcode = Field(Unicode, unique=True)
    username = Field(Unicode)
# that, the definition of the model is exactly the same.
metadata.bind = create_engine('sqlite:////tmp/test.db')
metadata.bind.echo = False
setup_all()
create_all()

# Create the Flask application and register it with the APIManager.
app = flask.Flask(__name__)
manager = flask.ext.restless.APIManager(app)
# default. Allowed HTTP methods can be specified as well.
manager.create_api(Tube, methods=['GET', 'PATCH', 'POST', 'DELETE'])

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
