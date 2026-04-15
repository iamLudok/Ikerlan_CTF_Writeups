# El Momento de la Intrusión — Forensics | 300 pts | Easy

## Description

> After identifying the source of the brute force attack, we now need to know if it was successful and, if so, when. Your mission is to analyze the same access.log file to find the exact time the attacker managed to log into the system. The flag is the timestamp of the successful login.
>
> The flag format is `ikerlan{dd/mm/yyyy:hh:mm:ss}`. For example: `ikerlan{10/09/2025:20:10:05}`

## Hints

> **Hint 1 (free):** The attacker achieved their goal when a login attempt stopped returning 401 and became successful (200).

> **Hint 2 (45 pts):** Not used.

## Files

- `access.log` (same file as [La Fuente del Ataque](../la-fuente-del-ataque/writeup.md))

## Solution

This challenge is a direct follow-up to [La Fuente del Ataque](../la-fuente-del-ataque/writeup.md), using the same `access.log` file. From that challenge we already identified the attacker's IP as `192.168.1.100` and confirmed that one of their login attempts succeeded. We need to find the exact moment their login succeeded, i.e. the request to `/login.php` that returned HTTP `200` instead of `401`.

```bash
grep "192.168.1.100.*login.php.*200" access.log
```

This returns a single entry, confirming there was exactly one successful login. We extract the timestamp from it:

```bash
grep "192.168.1.100.*login.php.*200" access.log | sed 's/.*\[\(.*\)\].*/\1/' | cut -d' ' -f1
```

Output:

```
24/Sep/2025:22:31:17
```

Converting the month abbreviation to its numeric equivalent (`Sep` → `09`) gives us the flag format:

```
24/09/2025:22:31:17
```

The attacker performed ~100 failed login attempts over 32 seconds (22:30:45 – 22:31:17) before finally breaking in.

## Flag

```
ikerlan{24/09/2025:22:31:17}
```
