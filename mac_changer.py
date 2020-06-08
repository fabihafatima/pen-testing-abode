#!/usr/bin/env python
import subprocess
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC and")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")
    (option, arguments) = parser.parse_arg()
    if not option.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not option.new_mac:
        parser.error("[-] Please specify a new mac, use --help for more info.")
    return option


def change_mac(interface, new_mac):
    print("[+} Changing MAC address for " + interface + "to" + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


options = get_arguments()
change_mac(options.interface, options.new_mac)