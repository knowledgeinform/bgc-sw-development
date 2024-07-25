# REST API Routes

This directory defines the routes to all of the REST calls.

REST calls are grouped by the functions they are providing.  Some may be tightly linked to particular hardware, some may be linked to a functional area that needs to use multiple hardware types (e.g. flame-control on/off actually has to control helium flow and the flame control hardware).

* `api.py` defines routes to the other functional areas
* `xyz.api` defines the endpoints within functional area xyz (e.g. gas flow, system, temperature, etc.)
