#![feature(proc_macro, specialization)]

extern crate pyo3;

use pyo3::prelude::*;
use pyo3::py::modinit as pymodinit;

// add bindings to the generated python module
// NB: names: "core" must be the name of the `.so` or `.pyd` file
// NB: until pyo3==0.3, wrap the module name in quotes (https://github.com/PyO3/pyo3/issues/163)
/// This module is implemented in Rust.
#[pymodinit("_core")]
fn init_mod(py: Python, m: &PyModule) -> PyResult<()> {

    #[pyfn(m, "sum_as_string")]
    // pyo3 aware function. All of our python interface could be declared in a separate module.
    // Note that the `#[pyfn()]` annotation automatically converts the arguments from
    // Python objects to Rust values; and the Rust return value back into a Python object.
    fn sum_as_string_py(a:i64, b:i64) -> PyResult<String> {
       Ok(sum_as_string(a, b))
    }

    Ok(())
}

// logic implemented as a normal rust function
fn sum_as_string(a:i64, b:i64) -> String {
    format!("{}", a + b)
}
