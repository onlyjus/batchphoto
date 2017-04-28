batchphoto
==========

An application for batch editing photos.


Features
--------

- Auto crop based on object detection (face, object on uniform background)


Installation
------------

.. code-block:: bash

    $ pip install batchphoto


Usage
-----

1. Resize images to either an aspect ratio (5a7) or specific pixel dimensions
   (1920p1080):

  .. code-block:: bash

    $ batchphoto crop resize -i *.jpg -o output -r 5a7 4a6 1920p1080


2. Auto crop and image(s) with a face:

  .. code-block:: bash

      $ batchphoto crop face -i *.jpg -o output
