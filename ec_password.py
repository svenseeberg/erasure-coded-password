"""
Create erasure coded messages of a word
"""

import base64
from pyeclib import ec_iface  # pylint: disable=E0401
import qrcode  # pylint: disable=E0401


def create_output(messages):
    """
    create n qr codes
    """
    print_qr = input("Do you want to print QR codes? [Y|n] ")
    if print_qr == "" or print_qr.lower() == "y":  # pylint: disable=R1703
        print_qr = True
    else:
        print_qr = False

    i = 1
    for message in messages:
        print("Chunk {}".format(i))
        print("    {}".format(message.decode('utf-8')))
        if print_qr:
            qrcode.make(message).save("chunk-{}.png".format(i))
            print("    Created QR code chunk-{}.png".format(i))
        i = i + 1


def password_to_messages(password, data_fragments=3, parity_fragments=2):
    """
    erasure code password then b64 encode bytes
    """
    driver = ec_iface.ECDriver(k=data_fragments, m=parity_fragments,
                               ec_type="liberasurecode_rs_vand")
    ec_pw = driver.encode(bytes(password, 'utf-8'))
    b64_ec_pw = []
    for i in ec_pw:
        b64_ec_pw.append(base64.b64encode(i))
    return b64_ec_pw


def messages_to_password(messages, data_fragments=3, parity_fragments=2):
    """
    base64 decode messages, then recreate password
    """
    driver = ec_iface.ECDriver(k=data_fragments, m=parity_fragments,
                               ec_type="liberasurecode_rs_vand")
    ec_pw_loss = []
    for message in messages:
        ec_pw_loss.append(base64.b64decode(message))
    return driver.decode(ec_pw_loss)


def read_messages(data_fragments):
    """
    Get erasure coded messages from user
    """
    i = 0
    messages = []
    while i < data_fragments:
        messages.append(input("Please provide fragment {}:".format(i)))
        i = i + 1
    return messages


def main():
    """
    Parse arguments and call functions
    """
    data_fragments = input("How many data chunks do you need [3]? ")
    data_fragments = int(data_fragments) if data_fragments else 3
    parity_fragments = input("How many parity chunks do you need [2]? ")
    parity_fragments = int(parity_fragments) if parity_fragments else 2
    action = input("Encode or decode [E|d]? ")

    if action.lower() == 'e' or action == "":
        password = input("Enter your password or message: ")
        messages = password_to_messages(password,
                                        data_fragments=data_fragments,
                                        parity_fragments=parity_fragments)
        create_output(messages)
    else:
        messages = read_messages(data_fragments)
        print(messages_to_password(messages).decode('utf-8'))


if __name__ == '__main__':
    main()
