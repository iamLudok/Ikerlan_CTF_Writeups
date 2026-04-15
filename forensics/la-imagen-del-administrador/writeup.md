# La Imagen del Administrador — Forensics | 300 pts | Easy

## Description

> **Security Alert: Unauthorised Access**
>
> Our monitoring team has detected suspicious activity on one of the control servers hosted on a Raspberry Pi. We believe an unauthorised administrator has compromised the system to extract information.
>
> We managed to capture a forensic image (.img) of the hard drive just before the intruder could erase their tracks. Your mission as an analyst is to examine this image and recover any evidence left by the malicious user.
>
> Flag format: `ikerlan{...}`
>
> Download URL: https://drive.google.com/file/d/1PxboB6AEcY0_x5T6FqzRkpewdWQJN_nB/view?usp=sharing

## Hints

> **Hint 1 (free):** A disk, especially a Raspberry Pi one, is not a single block. Understanding its structure is essential. How can you list the partitions of a disk image (.img) and find out exactly where each one starts? Look for a tool that shows the start sector of the main Linux partition (ext4). That number is key for mounting!

> **Hint 2 (free):** You can't mount the image directly — you need to skip the first partitions. Once you have the start sector, remember: each sector has a standard size of 512 bytes. Multiplying those two values gives you the offset in bytes. With that number, the `-o offset=` option of the `mount` command will let you access the main filesystem.

> **Hint 3 (free):** The attacker used the admin user's home directory to hide the evidence. Once the image is mounted, navigate to `/home/admin/`. Don't forget that in Linux, files and folders starting with a dot (.) are hidden by default. Make sure to list all files so you don't miss the secret folder.

## Files

- `rpi.img` (via Google Drive link above)

## Solution

<!-- TODO -->

## Flag

<!-- TODO -->
