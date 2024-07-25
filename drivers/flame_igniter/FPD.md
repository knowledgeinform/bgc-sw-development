# FPD IGNITOR BOARD PROTOTYPE #

## TODO ##
[ ] Wiring: add DC stepdown module(Powered by large DC Supply) to 3.3V and relay to control
[x] command line to set relay on and deliver 3.3V to heater
[x] query temp by command line (continous polling?)
[ ] Works when asked by Think&Do, have plug and play functionality

## Power Data ##
- Voltage 22.4 Vin Idle
- 3.5V IG+ while flame ignite
- 0.3V IG- while flame ignite
- 3.5V, 2.3A to heat 
- Resistance(IG+/IG-) 17.85kΩ

# Notes #
- USB Power is 5V, DC gives 3.3V Vin, GPIO pins default set to 5V logic
- Board will continously read and print temperature, ignition when prompted
- You can connect both USB and VIN power, Arduino will automatically switch between the two to maintain the highest voltage output on the 5V out
- Arduino does not support threads/multiprocessing, so reason why time is off is because hardware interruts cause cause timing error in other relays
- high temperature precision, but low accuracy
- 210°C to +1800°C output in 0.0078125° resolution - note that K
thermocouples have about ±2°C to ±6°C accuracy or worse depending on the
temperature and type