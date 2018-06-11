# rust python extension

This is a generic example of a Python extension written in Rust, with an
example of a crude 'fallback' mechanism for when the extension fails to build.

The setup.py script also contains hooks into the 'test' and 'install' commands
which ensure that the nightly toolchain is in use before attempting to build
the rust extension.

To test:

```bash
python setup.py test
```
