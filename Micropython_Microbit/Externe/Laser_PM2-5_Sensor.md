Laser PM2.5 Sensor specification
================================

la documentation complète du capteur [SDS011](https://www-sd-nf.oss-cn-beijing.aliyuncs.com/%E5%AE%98%E7%BD%91%E4%B8%8B%E8%BD%BD/SDS011%20laser%20PM2.5%20sensor%20specification-V1.4.pdf)

Product model: SDS011 Version: V1.3
===================================

Product specifications
-----------------------

### 1.Product size

L*W*H=71*70*23mm
### 2.Interface specification

|No| Name| Comment|
|--|-----|--------|
|1 | NC | Not Connect |
|2 |1μm | PM2.5: 0-999μg/m3;PWM Output |
|3 | 5V |5V Input
|4 |2.5μm | PM10: 0-999 μg/m3;PWM Output
|5 |GND | Ground
|6 | R | RX of UART(TTL)@3.3V
|7 | T | TX of UART(TTL)@3.3V

PS:The distance between each pin is 2.54mm.

The UART communication protocol
--------------------------------

  Bit rate :9600
  Data bit :8
  Parity bit:NO
  Stop bit :1
  Data Packet frequency: 1Hz

|The number of bytes | Name | Content|
|--|--|--|
| 0 | Message header | AA
| 1 | Commander No. C0
| 2 | DATA 1 | PM2.5 Low byte
| 3 | DATA 2 | PM2.5 High byte
| 4 | DATA 3 | PM10 Low byte
| 5 | DATA 4 | PM10 High byte
| 6 | DATA 5 | ID byte 1
| 7 | DATA 6 | ID byte 2
| 8 | Check-sum | Check-sum
| 9 | Message tail | AB

Check-sum: Check-sum=DATA1+DATA2+...+DATA6 。

PM2.5 value: PM2.5 (μg /m 3 ) = ((PM2.5 High byte *256) + PM2.5
low byte)/10

PM10 value: PM10 (μg /m 3 ) = ((PM10 high byte*256) + PM10 low
byte)/10

PWM output description

|Range of PM2.5 value| 0-999μg /m3|
|--|--|
| Range of PM10 value | 0-999μg /m3 |
| Cycle | 1004ms±1% |
| High level output time at the beginning of the whole cycle | 2ms |
| The middle time of this cycle | 1000ms±1% |
| Low level output time at the end of the whole cycle | 2ms |
