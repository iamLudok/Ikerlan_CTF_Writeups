# Un Mensaje Transportable — Crypto | 100 pts | Easy

## Description

> You have intercepted a message that seems to be part of a longer key. Although it is a long and strange text string, it does not appear to have been encrypted with an algorithm, but simply encoded to avoid data loss during transmission. This is the first obstacle you will encounter in almost any CTF. Identify the encoding method and reverse the process to obtain the final flag.

## Hints

> **Hint 1 (free):** Do you know base64 encoding?

## Files

`mensaje_transportable.txt`:
```
============================================
 [ENCRYPTED COMMUNICATION LOG: 04-OCT-2025]
============================================

We have intercepted the following anonymous transmission.

--- START OF FRAGMENT ---

aWtlcmxhbntiNHMzX2VuY29kaW5nISF9

--- END OF FRAGMENT ---

**Urgent Mission!**

We need you to identify and reverse the initial encoding. Please recover the flag contained in the fragment.

[END OF LOG]
```

## Solution

The description hints that the message was not encrypted but simply **encoded** for transmission — this is a classic description of **Base64**, an encoding scheme widely used to safely transmit binary or text data over text-based protocols.

The encoded string extracted from the file is:

```
aWtlcmxhbntiNHMzX2VuY29kaW5nISF9
```

Decoding it with a simple terminal command:

```bash
echo "aWtlcmxhbntiNHMzX2VuY29kaW5nISF9" | base64 -d
```

Output:

```
ikerlan{b4s3_encoding!!}
```

## Flag

```
ikerlan{b4s3_encoding!!}
```
