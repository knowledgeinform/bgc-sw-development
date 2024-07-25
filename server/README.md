# Server Template

## Overview

This directory provides a template for organization of part of the server.

It has the following:

* `controller/` renamed to `app/` following FastApi examples
* Uses `async` throuhout
* Simple simulated hardware
* Simulated 'background' controllers to poll hardware asynchronous with the front end
* Prototypes for all initial REST endpoints using FastApi w/Pydantic validation

Also see [this document](../../docs/Backend-Design.md) for ongoing design info.

## REST Guidance

In general...

* `get` methods should get their results from a database or other asynchronous hardware monitoring
components that gather status periodically without GUI intervention / request.
* `put` methods should put their inputs into a database or use device drivers or hardware controllers to perform
hardware updates when requested
  * not sure if we'll be queuing anything up for later

## Use

From `bgc-sw` run

``` terminal
uvicorn server.app.main:app --reload
```
