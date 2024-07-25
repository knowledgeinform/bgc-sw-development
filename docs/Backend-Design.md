# Overview

This document contains a variety of design guidance / overview etc. for the backend software.

## Design Guidance

Final drivers should be configured to use Python `async` capabilities for performance.

* Hardware devices which share a hardware port but do not support multiple messages on that port need to use an `asyncio.Mutex` to protect all uses of the hardware port.
  * look to mms-sw SerialHardware.* for guidance for providing auto-lock/release instead of cluttering client code with same

Multiple drivers may need to be aggregated to accumulate an overall status using a continuous periodic monitoring loop and supporting a `status` method or property.

See `prototypes/` for a prototype to kick off our startup code / monitors...

## Proposed Endpoints

ClarityMethodType = calibration | scan | all

Method inputs / results don't expose how methods may be segregated into various types by the system.  Unless `any` is used.

* [ ] Currently we're supporting a set of prescribed names for hardware devices.   Makes a little more work on the back-end but the front end is much more readable.   Or do we let front end get at each with separate endpoints or the like.

* /api
  * /bgc-method
    * /get-methods/{type:ClarityMethodType}
      * Get all BGC methods of a given type
      * TBD - should this just return all of them? and let the UI deal?
      * result: { methods: [ { method: BgcMethod }]}
    * /set-method
      * Args: { value: BgcMethod }
      * Store parameters for a BGC method
  * /clarity
    * /control {state=on|off}
    * /load-method {type=ClarityMethodType, name=string}
    * /run-loaded-method
    * /methods {type=ClarityMethodType}
      * result: [ names ]
    * /method-results { TBD }
      * result: { TBD: results of parsing the method output file }
    * /get-factory-settings
      * Return all of the internal configuration parameters needed to access Clarity.  Method locations, etc.
      * return: TBD
    * /set-factory-settings
      * Set any subset of the internal configuration parameters for accessing clarity.
        * args: TBD
    * /abort
      * TBD - needed?
    * TBD-other-needed-commands-converted-to-english
  * /digital-io
    * /status
      * result: [...]
    * TBD are there any we need to control?
  * /flame-control
    * /control/{state=on|off}
      * Turn the flame controller on or off
    * /temperature
      * Read it's temperature
      * Return: number
  * /gas-flow
    * /ids
      * result: [ {name: name, value: device-id }]
    * /set-flows [ {name: name, value: SLPM} ]
      * value: "target flow rate for the MFC in SLPM"
        * "$comment": "limited to [0, 0.5% device max .. device max]"
    * /status
      * result: [ {name: flow-name, value: MfcStatus} ]
      * get status of all flows
    * /isocratic_defaults
      * result: [ { name: flow-name, value: SLPM } ]
      * Return the default settings
      * TBD - part of system settings?
    * /system
      * /status TBD - get overall system status including aggregating info like flame on/off, etc
      * TBD maybe this aggregates all of the status from the other endpoints to save on traffic
  * /temperature
    * /set-temperatures [ { name: zone-name, value: degreesC } ]
      * Control any or all zones.
    * /status [ { name: zone-name, value: degreesC } ]
      * TBD is status more complex?
    * /isocratic_defaults
      * result: [ { name: zone-name, value: degreesC } ]
        * Return the default settings
        * TBD - part of system settings?

### BGC Methods

As discussed, Think&Do uses the same parameters for isocratic temperatures and the flow rates for all methods.

That's not appropriate for the new system.

We now need the system to manage isocratic temperatures and flow rates for each method.

We also still need Clarity to control all of the valves and temperatures ramps in real time as done in Think&Do.

To that end we need "BGC Methods" to associate the following data with a Method:

* Type (calibration, scan, any)
  * Not prescribing how this is maintained but it must be maintained
    * enumerated here
    * part of the filename
    * elsewhere?
* Name
  * This used to just be the method filename in Think&Do
* Temperatures
  * TBD temperatures set by the system at the start of a method run
* Flow Rates
  * TBD flow rates set by the system before Clarity is asked to run the
* Clarity Name
  * If maintained then we could separate the Name from the Clarity Name
    * [x] TBD do we need this capability?
      * yes - multiple isocratic for one clarity method?
    * If computed as function(Type, Name, Clarity Installed Config) then we forever link them but burden SMEs with using our names.

### MFCs (flow-rates)

There are up to 8 MFCs, each with a different device ID.

Each should be initialized to use SLPM, see mms-sw AlicatDriver.* and PowerBoard::CreateGen4Resources()

The front-end will deal with the MFCs using their names and the back-end will map that to the appropriate device IDs.

The front-end will deal with MFCs using Standard Liters Per Minute (SLPM) and the back-end will convert that to whatever units the currently installed MFCs are using.

Units

``` pdl
# see mms-sw\code\software\applications\server\schemas\info_getAerosolStatus_RESPONSE.json
MfcStatus = {
    minRate: number,
    maxRate: number,
    targetRate: number,
    actualRate: number,
    units: number,  # should be forced to SLPM by backend
    degreesC: number,
    gasType: string
}
```

### Solenoids

These are only monitored by the front-end, they're controlled by Clarity.   Hence no set commands.

The utilities for command line should be able to set/get.

### Flame Igniter

### Clarity

Communication should be via `asyncio.create_subprocess_shell()` or `asyncio.create_subprocess_exec()`

* See [Subprocesses](https://docs.python.org/3/library/asyncio-subprocess.html#)
