# Clarity Driver

This driver provides access to the Clarity program.

Interfaces are provided logically and, hopefully, insulate the client from the responsibility of managing the following
types of information:

* Where clarity is installed
  * Clients can provide the location of the clarity executable though
  * This will default but can be changed other REST endpoints and a higher level client can inform the driver
* File names / extensions for different types of clarity files
  * This driver manages and provides methods for accessing / maintaining (RWD)the various types of files in locations defaulted but specifiable by the client
  * Methods / etc. are provided by their names without path or extension.
  * This driver is not aware of BGC Methods as they are a higher level concept managed elsewhere.

* [ ] TODO: This driver will also support running without the real system:
  * No Clarity - just echo commands to clarity expand as needed as time goes by
  * ClarifyDemo / Clarity - run the real program (if Demo we might need to simulate some stuff)
  * We could probably check the default locations at runtime unless provided on driver construction and use in priority order:
  * Clarity / ClarityDemo / No Clarity

All clarity methods used by the software are created by Clarity.exe - not services in this driver - as they seem to be
stored in a proprietary binary format by Clarity.exe
