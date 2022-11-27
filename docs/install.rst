Installing iCalendar
====================

To install the icalendar package, use::

  pip install icalendar

If installation is successful, you will be able to import the iCalendar
package, like this::

  >>> import icalendar

Development Setup
-----------------

To start contributing changes to icalendar,
you can clone the project to your file system
using Git.
You can `fork <https://github.com/collective/icalendar/fork>`_
the project first and clone your fork, too.

.. code-block:: bash

    git clone https://github.com/collective/icalendar.git
    cd icalendar

Installing Python
-----------------

You will need a version of Python installed to run the tests
and execute the code.
The latest version of Python 3 should work and will be enough
to get you started.
If you like to run the tests with different Python versions,
the following setup process should work the same.

Install Tox
-----------

First, install `tox <https://pypi.org/project/tox/>`_..

.. code-block:: bash

    pip install tox

From now on, tox will manage Python versions and
test commands for you.

Running Tests
-------------

``tox`` manages all test environments in all Python versions.

To run all tests in all environments, simply run ``tox``

.. code-block:: bash

    tox

You may not have all Python versions installed or
you may want to run a specific one.
Have a look at the `documentation
<https://tox.wiki/en/latest/example/general.html#selecting-one-or-more-environments-to-run-tests-against>`__.
This is how you can run ``tox`` with Python 3.9:

.. code-block:: bash

    tox -e py39

Accessing a ``tox`` environment
-------------------------------

If you like to enter a specific tox environment,
you can do this:

.. code-block:: bash

    source .tox/py39/bin/activate

Install ``icalendar``  Manually
-------------------------------

The best way to test the package is to use ``tox`` as
described above.
If for some reason you cannot install ``tox``, you can
go ahead with the following section using your
installed version of Python and ``pip``.

If for example, you would like to use your local copy of
icalendar in another Python environment,
this section explains how to do it.

You can install the local copy of ``icalendar`` with ``pip``
like this:

.. code-block:: bash

    cd icalendar
    python -m pip install -e .

This installs the module and dependencies in your
Python environment so that you can access local changes.
If tox fails to install ``icalendar`` during its first run,
you can activate the environment in the ``.tox`` folder and
manually setup ``icalendar`` like this.

Try it out:

.. code-block:: python

    Python 3.9.5 (default, Nov 23 2021, 15:27:38)
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import icalendar
    >>> icalendar.__version__
    '5.0.3'

Building the documentation locally
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To build the documentation follow these steps:

.. code-block:: bash

    $ source .tox/py39/bin/activate
    $ pip install -r requirements_docs.txt
    $ cd docs
    $ make html

You can now open the output from ``_build/html/index.html``. To build the
presentation-version use ``make presentation`` instead of ``make html``. You
can open the presentation at ``presentation/index.html``.

You can also use ``tox`` to build the documentation:

.. code-block:: bash

    cd icalendar
    tox -e docs
