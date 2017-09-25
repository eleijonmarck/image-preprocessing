===============================
cat_dog
===============================

An api for cat_dog


Quickstart
----------

First, set your app's secret key as an environment variable. For example,
add the following to ``.bashrc`` or ``.bash_profile``.

.. code-block:: bash

    export CAT_DOG_SECRET='something-really-secret'

Before running shell commands, set the ``FLASK_APP`` and ``FLASK_DEBUG``
environment variables ::

    cd cat_dog
    export FLASK_APP=$PWD/application.py
    export FLASK_DEBUG=1

Then run the following commands to bootstrap your environment ::

    pip install -r requirements/developement.txt
    flask run

You will see a pretty welcome screen.

Deployment
----------

In your production environment, make sure the ``FLASK_DEBUG`` environment
variable is unset or is set to ``0``, so that ``ProductionConfig`` is used.


Shell
-----

To open the interactive shell, run ::

    flask shell

By default, you will have access to the flask ``app``.


Running Tests
-------------

To run all tests, run ::

    flask test
