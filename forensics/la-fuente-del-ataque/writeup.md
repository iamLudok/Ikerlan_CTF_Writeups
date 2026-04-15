# La Fuente del Ataque — Forensics | 300 pts | Easy

## Description

> We have detected a series of failed access attempts on our login portal. Analyze the web server log file (access.log) to identify the IP address that performed a brute force attack. The flag is the attacker's IP address.
>
> The flag format is `ikerlan{ip_atacante}`. For example: `ikerlan{127.0.0.1}`

## Hints

> **Hint 1 (free):** Look for the IP that has generated the highest number of entries in the log. An attacker often leaves a statistically notable trail.

> **Hint 2 (45 pts):** Not used.

## Files

- `access.log`

## Solution

We start by inspecting the log file structure:

```bash
head -20 access.log
```

Right from the first lines, a clear pattern emerges: multiple requests to `/login.php` returning `401` (Unauthorized) from the same IP.

To confirm, we count how many times each IP appears in the log:

```bash
awk '{print $1}' access.log | sort | uniq -c | sort -nr | head -10
```

One IP stands out with 101 entries — significantly more than any other. We then verify how many of those were failed login attempts:

```bash
grep "192.168.1.100.*login.php.*401" access.log | wc -l
```

Result: **100 failed login attempts** to `/login.php`, all within a 32-second window (22:30:45 – 22:31:17 on September 24, 2025). This is a textbook brute force pattern.

Checking whether the attack eventually succeeded:

```bash
grep "192.168.1.100.*login.php.*200" access.log
```

The final attempt returned a `200` (OK), confirming the attacker broke in after exhausting the password list.

**Summary of the attack:**
- **Attacker IP:** `192.168.1.100`
- **Target endpoint:** `/login.php`
- **Failed attempts:** 100 (HTTP 401)
- **Successful login:** 1 (HTTP 200)
- **Time window:** 22:30:45 – 22:31:17, 2025-09-24

## Flag

```
ikerlan{192.168.1.100}
```
