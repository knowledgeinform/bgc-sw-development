# Driver Design Principles

## General

* There should be one driver directory for each hardware device we interface to.
  * Maybe special case for MFCs where we call it mfc but it may have drivers for Alicat and Bronkhorst
* Data sheets should be referenced on box and / or a web reference, not in these directories

## Overall Design

`REST APIs`

* Execute the requests from the GUI

`HW Tests`

* Provide SME users with ways to exercise the individual hardware components using the `Drivers`
* One for every `Driver` named after the driver, e.g. `clarity_hw_test.py`
  * see `alicat_basis_mfc_hw_test.py` for a sample

`Drivers`

* Implemented using a Python class to interface to a single instance of a single type of device
  * e.g. There would be N instances of the MFC driver, one for each MFC all sharing the same bus
* Provide logical interfaces to the hardware
  * Provide access to *quirks* of hardware as needed by the users
    * Things like setting the device ID etc
  * Have ports / ids / other system parameters provided during construction / initialization
  * Provide all services using `async` where possible for performance.
  * see `alicat_basis_mfc_driver.py` for a sample
* Same code is used Are shared by the `HW Test Drivers` and the `REST APIs`
* One for every hardware device we interface to, e.g. `clarity_driver.py`
  * Just one for things like the Controller Board which might control multiple types of devices
