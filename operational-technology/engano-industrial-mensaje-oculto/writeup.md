# Engaño Industrial: Extrayendo el Mensaje Oculto — Operational Technology | 300 pts | Easy

## Description

> Part 2/2 of the challenge.
>
> This is the direct continuation of the first challenge. You will use the same traffic capture (pcap). Examine the attacker's activity. They are injecting a sequence of Modbus/TCP write requests that contain an encoded secret phrase.

## Hints

> **Hint 1 (free):** Filter the Modbus traffic coming from the attacker's IP and look for the write command used to send data to multiple registers at once.

> **Hint 2 (free):** The attacker is smart and did not write to the typical control registers. Look for the write command with a high register address (higher than the registers the HMI reads, which is only Register 0).

## Files

- `suspicious_pcap.pcap` (same file as Part 1)

## Solution

<!-- TODO -->

## Flag

<!-- TODO -->
