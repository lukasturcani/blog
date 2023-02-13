===============================
ECS System Registration in Rust
===============================

.. attention::

  This post borrows heavily from
  https://blog.logrocket.com/rust-bevy-entity-component-system/
  and exists mostly as a way for me to internalize what it says
  by re-explaining it.


The problem
===========

We would like provide the following Rust API

.. code-block:: rust

  fn main() {
    App::new()
      .add_system(zero_params)
      .add_system(one_param)
      .run();
  }

  fn zero_params() {
    println!("zero params");
  }

  fn one_param(x: i32) {
    println!("one param: {x:#?}");
  }
