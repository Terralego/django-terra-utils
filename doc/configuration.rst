Configuration
=============


In your project :

* settings

::

    INSTALLED_APPS = [
        ...
        # Utils app
        'terra_utils',
        ...
    ]


- SETTINGS :

Waiting for settings definition directly in models.

Settings should be overrided  with TERRA_CRUD settings in your project settings file:

::

    ...
    STATES = Choices()
    ...
