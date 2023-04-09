:hide-toc:

Rust Simulations in Sphinx Docs
===============================

Introduction
------------

In this post I'll cover how I managed to get this blog post
to display the simulation below.

.. bevy-sim:: https://github.com/lukasturcani/rust-boids/releases/download/v0.0.6/rust-boids-wasm.tar.gz

The key points about this bit work are:

#. The simulation is written in Rust (https://github.com/lukasturcani/rust-boids) and compiled to WASM.
#. This blog is written in rST and compiled into HTML using `Sphinx <https://www.sphinx-doc.org/en/master/>`_.
#. Embedding the simulation in the blog post looks something like this:

.. code-block:: rst

  This is my blog post, written in reStructuredText!

  .. bevy-sim:: https://github.com/lukasturcani/rust-boids/releases/download/v0.0.6/rust-boids-wasm.tar.gz

  This is the rest of the blog post!

So the key bit of work is writing a Sphinx extension which adds the
``bevy-sim`` directive. This directive will:

#. Take a single argument, which is a a URL to a `Bevy <https://bevyengine.org/>`_ simulation compiled to WASM.
#. Download and extract the WASM.
#. Place a canvas element into the HTML document in which the WASM will be run.
