# About
This script splits a message (i.e. password) into `k` data chunks that can be printed as QR codes. A given number `m` of parity chunks is added. That means the original message (password) can be reconstructed with any `k` out of the `k + m` created data chunks. A more sound cryptographic solution would be Shamir's Secret Sharing.

# Why?
Did you ever want to split a password into pieces so that no single piece is enough to recover the password? Then this script is for you. If you want to print them to paper, QR codes make your life easier.

# Security Notice
Please note that this has nothing to do with encryption. Each chunk contains a plain text part of the password/message. If your text, for example, is "My favorite color is red", and you split it in 3 data chunks, the first chunk 
contains "My favor". Also contained is the overall length of the message. This would make it pretty easy to guess the full text. Therefore, only use randomized strings.

If you're doing this for a very important secret, ~consider running this script in a live Linux~ use `ssss`.

# Installation

1. `git clone https://github.com/svenseeberg/erasure-coded-password.git`
2. `cd erasure-coded-password`
3. `python3 -m venv .venv`
4. `source .venv/bin/activate`
5. Install the `liberasurecode` development package. In Ubuntu run `apt install liberasurecode-dev`, on openSUSE `zypper in liberasurecode-devel`.
6. `pip3 install Pillow-PIL qrcode pyeclib`

# Usage
1. `cd [/path/to/]erasure-coded-password`
2. `source .venv/bin/activate`
3. `python3 ec-password.py`
The script has no parameters, it asks for all the input while it runs.

![Example](example.png)
