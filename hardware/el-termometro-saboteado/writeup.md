# El Termómetro Saboteado — Hardware | 300 pts | Easy

## Description

> The university's IoT lab has a temperature monitoring system with several Arduinos distributed throughout the building. Each Arduino reads a DHT22 sensor and sends data every minute to a central server. This morning, the systems technician noticed something strange: one of the sensors (Sensor_Lab_B3) is intermittently reporting impossible temperatures:
>
> ```
> [09:00] Sensor_Lab_B3: 22.4°C ✓ Normal
> [09:01] Sensor_Lab_B3: 23.1°C ✓ Normal
> [09:02] Sensor_Lab_B3: 104.0°C ¡Imposible!
> [09:03] Sensor_Lab_B3: 22.8°C ✓ Normal
> [09:04] Sensor_Lab_B3: 52.0°C ¡Imposible!
> [09:05] Sensor_Lab_B3: 23.2°C ✓ Normal
> [09:06] Sensor_Lab_B3: 99.0°C ¡Imposible!
> ...
> ```
>
> When inspecting the Arduino physically, everything seems normal. The sensor works fine. But someone modified the code to occasionally report "fake temperatures" that are actually... a secret message. Your mission: analyse the temperature log from the last 24 hours and discover what message is hidden in those "impossible" readings.
>
> Flag format: `ikerlan{mensaje_oculto}`

## Hints

> **Hint 1 (free):** DHT22 sensors in the IoT lab typically report ambient temperatures, but something is interfering with Sensor_Lab_B3. Examine the readings marked as 'impossible' in the log. Why would a sensor report such extreme values in a controlled environment?

> **Hint 2 (45 pts):** Not used.

> **Hint 3 (75 pts):** Not used.

## Files

- `temperature_log.csv`

## Solution

<!-- TODO -->

## Flag

<!-- TODO -->
