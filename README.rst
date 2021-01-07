Python pre-commit hooks
#######################

.. image:: https://git.shore.co.il/nimrod/python-pre-commit/badges/master/pipeline.svg
    :target: https://git.shore.co.il/nimrod/python-pre-commit/-/commits/master
    :alt: pipeline status

Ansible `pre-commit <http://pre-commit.com/>`_ hooks.

- :code:`piprot`: Checks your requirements files for out of date packages.

Installation
------------

Add the following to your :code:`.pre-commit-config.yaml`:

.. code:: yaml

    - repo: https://git.shore.co.il/nimrod/python-pre-commit.git
      rev: v0.2.0
      hooks:
        - id: piprot

License
-------

This software is licensed under the MIT license (see the :code:`LICENSE.txt`
file).

Author Information
------------------

Nimrod Adar, `contact me <nimrod@shore.co.il>`_ or visit my `website
<https://www.shore.co.il/>`_. Patches are welcome via `git send-email
<http://git-scm.com/book/en/v2/Git-Commands-Email>`_. The repository is located
at: https://git.shore.co.il/explore.
