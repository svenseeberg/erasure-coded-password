# About
This helper script splits a message (i.e. password) into `k` data chunks that can be printed as QR codes. A given number `m` of parity chunks is added. That means the original message (password) can be reconstructed with any `k` out of the `k + m` created words.

# Why?
Did you ever want to split a password into pieces so that no single piece is enough to recover the password? Then this script is for you.

# Installation

1. `python3 -m venv .venv`
2. `source .venv/bin/activate`
3. `pip3 install Pillow-PIL qrcode pyeclib`

# Usage
Just start the script with `python3 ec-password.py`. It will ask you for all the details. It allows you to encode and decocde passwords.

If you're doing this for a very important secret, consider running this script from a live Linux.
