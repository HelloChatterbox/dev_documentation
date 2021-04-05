---
description: An overview of the test frameworks used by chatterbox-core.
---

# Testing

## Unit Tests

Chatterbox-core unit tests are located in `chatterbox-core/test/unittests`

These are created using the [`unittest`](https://docs.python.org/3/library/unittest.html) package from the Python standard library.

### Test runner

A helper command is provided in `chatterbox-core/bin` to enable quick and simple access to the test runner. It is assumed that this directory is on your `$PATH` .

If that is not the case, prepend all `chatterbox-*` commands with the path to your `chatterbox-core/bin` directory or run the tests manually.

#### Execute all tests

To execute all tests run:

```text
chatterbox-start unittest
```

#### Execute single test

To execute a single test file run:

```text
chatterbox-start singlueunittest path/to/test/file.py
```

The second argument points to the test file you wish to execute. Note that this is relative to your `chatterbox-core` installation.

If I was working on the audio utilities, I might run:

```text
chatterbox-start singlueunittest test/unittests/audio/test_utils.py
```

#### Manually run tests

The `chatterbox-start` helper commands are a convenience wrapper. They activate the Python virtual environment and run pytest.

The equivalent commands to run all tests would be:

```text
cd ~/chatterbox-core
source .venv/bin/activate
pytest
```

## Integration Tests

The Chatterbox integration test suite is called Voight Kampff. Currently this does explicitly cover chatterbox-core, however Skills are tested, which indirectly tests a range of Chatterbox's technologies.

For more detail on Voight Kampff see:

{% page-ref page="../../skill-development/voight-kampff/" %}

