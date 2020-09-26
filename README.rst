==============
erc20-snapshot
==============


Utility to make a snapshot of an erc20 token.
Made for python3.


Description
===========

First install it in a clean virtualenv:

.. code-block:: bash

    $ virtualenv --python python 3 myenv
    $ cd myenv
    $ source bin/activate
    $ git clone https://github.com/aleph-im/erc20-snapshot.git
    $ cd erc20-snapshot
    $ python setup.py develop

To run, create a .env file with these values:

.. code-block:: bash

    ETHEREUM_API_SERVER="https://mainnet.infura.io/v3/CODE"
    ETHEREUM_TOKEN_CONTRACT="0xC0134b5B924c2FCA106eFB33C45446c466FBe03e"
    ETHEREUM_MIN_HEIGHT=10225485

The min_height being one block before the contract creation, and CODE your infura api key.
You can also have a local rpc node of course.

Then run it with this command (replacing with your snapshot height):

.. code-block:: bash

    erc20_snapshot -o balances.json 1093856

Note
====

This project has been set up using PyScaffold 3.2.3. For details and usage
information on PyScaffold see https://pyscaffold.org/.
