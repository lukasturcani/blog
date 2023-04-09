import hashlib
import pathlib
import tarfile
import typing

import requests
from docutils import nodes
from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective

_conf_directory = pathlib.Path(__file__).resolve().parent.parent
_static_directory = _conf_directory / "_static"


def _extract_sim(url: str, name: str) -> str:
    response = requests.get(url)
    destination = _static_directory / "bevy_sims" / name / "sim.tar.gz"
    destination.parent.mkdir(exist_ok=True, parents=True)
    with open(destination, "wb") as f:
        f.write(response.content)

    with tarfile.open(destination) as tf:
        tf.extractall(destination.parent)

    return next(destination.parent.glob("*.js")).name


class BevySimDirective(SphinxDirective):
    has_content = True

    def run(self) -> list[nodes.Node]:
        url = self.content[0]
        name = hashlib.sha1(url.encode()).hexdigest()
        lib = _extract_sim(url, name)
        return [BevySimNode(name, lib)]


class BevySimNode(nodes.General, nodes.Element):
    def __init__(self, sim_name: str, lib: str) -> None:
        super().__init__()
        self.sim_name = sim_name
        self.lib = lib


def _bevy_sim_node_to_html(self, node: BevySimNode) -> None:
    self.body.append(
        f"""
        <canvas id="bevy-canvas"></canvas>
        <script type="module">
            import init from './_static/bevy_sims/{node.sim_name}/{node.lib}';
            init();
        </script>
        """
    )
    raise nodes.SkipNode


def setup(app: Sphinx) -> dict[str, typing.Any]:
    app.add_directive("bevy-sim", BevySimDirective)
    app.add_node(
        node=BevySimNode,
        html=(_bevy_sim_node_to_html, None),
    )
    return {
        "version": "0.0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
