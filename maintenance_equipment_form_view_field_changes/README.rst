.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

============================================
Modifies Equipment form view and adds fields
============================================

This module adds two fields:
* Description
* Owner

Fields on equipment form view is rearranged differently. Some fields are
hidden from all users.

Configuration
=============
Only installing this module is needed. Adding fields and form view changes
are done automically. User needs access rights for maintenance module to
see the changes.

Usage
=====
A user adds information to the created fields.

Known issues / Roadmap
======================
Consider checking that if an other module tries to make changed to form view
that no conflicts occur because of this module.

The form view is changed with specific xpaths to avoid issues with other modules.
Also replaces has not been used so other modules will not throw an error because
of missing fields on form view.

Credits
=======

Contributors
------------

* Timo Kekäläinen <timo.kekalainen@tawasta.fi>
* Jarmo Kortetjärvi <jarmo.kortetjarvi@tawasta.fi>

Maintainer
----------

.. image:: http://tawasta.fi/templates/tawastrap/images/logo.png
   :alt: Oy Tawasta OS Technologies Ltd.
   :target: http://tawasta.fi/

This module is maintained by Oy Tawasta OS Technologies Ltd.
