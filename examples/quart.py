from typing import cast

from quart import Quart, render_template, request

from asgi_htmx import HtmxDetails

from .common import make_table
from .lib import render_partial

app = Quart(__name__)

render_partial.register_quart(app)


@app.route("/")
async def home() -> str:
    return await render_template("home.html", framework="quart")


@app.route("/result")
async def result() -> str:
    assert (htmx := HtmxDetails(cast(dict, request.scope)))
    context = {"table": make_table(htmx)}
    return await render_template("partials/result.html", **context)
