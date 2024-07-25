# Valve Control #

Use the Arduino to take 6x inputs and trigger off of their edges to generate 
also be able to turn on relay using command line

12 outputs, each of which is 2 sec. long, connected to screw terminal

- Rising edge -> 1x output for 2 sec
- Falling edge -> 1x output for 2 sec
## Questions ##
- What are the inputs connected to?
- How exact do we need relays to turn off?

## Notes ##
- Arduino does not run user input timing accurately (~.2s error), streamlined code runs at O(n)
  - user input time period set at 2000 will turn off after ~(2000 - 2900)
  - ran the same relay over and over^
- Reading input pins much more accurate, always exactly 2000 ms
- Relays run off 5V power, can simply use usb board power
- check input pin mode during setup (PULLUP if not connected, normal input if connected to set voltage)
