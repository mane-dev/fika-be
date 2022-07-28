from time import sleep
from flask import Response, stream_with_context
import coffee.brew

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('brew', __name__, url_prefix='/brew')

@bp.get('/')
def current_brew():
    iter = coffee.brew.demo()

    def generate():
        for row in iter:
            sleep(1)
            yield f"{row}\n"
            if(row > 10): 
                break
    return Response(stream_with_context(generate()), mimetype='text/plain')
