# Bluedesk

THIS PROJECT IS NOT MAINTAINED ANYMORE SINCE THERE IS A NEW REWRITE IN BASED OF NODE.JS, CHECKOUT THE REPOSITORY: [DESKBLUEZ](https://github.com/alex20465/deskbluez)



Connects to a low energy actuator system via bluetooth and allows remote control via command line or internal managed interface.

## Supported and Tested Desks

- [Linak Desk 8721 (Module)](https://www.linak.com/products/controls/desk-control-basic-app/) / [IKEA IDÅSEN](https://www.ikea.com/gb/en/p/idasen-desk-sit-stand-brown-beige-s79280917/)

> Other devices may also work.

# Requirements

## Prepare **bluepy** system dependencies:

The code needs an executable `bluepy-helper` to be compiled from C source. This is done
automatically if you use the recommended pip installation method (see below). Otherwise,
you can rebuild it using the Makefile in the `bluepy` directory.

To install the current released version, on most Debian-based systems:

    $ sudo apt-get install python-pip libglib2.0-dev

On Fedora do:

    $ sudo dnf install python-pip glib2-devel

For Python 3, you may need to use `pip3`:

    $ sudo apt-get install python3-pip libglib2.0-dev


# Installation

    sudo pip install bluedesk



> To use the command without `sudo` run this command:

    sudo setcap 'cap_net_raw,cap_net_admin+eip' /usr/local/lib/(python3.7 OR your version)/dist-packages/bluepy/bluepy-helper

> where python3.7 is relative to your current used version.


# CLI Usage

## HELP

    $ bluedesk -h

    usage: bluedesk [-h] {connect} ...

    Controls lower energy actuator systems (office desks) via bluetooth.

    positional arguments:
    {connect}

    optional arguments:
    -h, --help  show this help message and exit

## Connect

    $ bluedesk connect

    Scanning ...
    [?] Choice device: Desk 8721 [e4:d1:a7:xx:xx:xx]
    > Desk 8721 [e4:d1:a7:xx:xx:xx]
    None [02:c3:85:xx:xx:xx]

    Device: e4:d1:a7:xx:xx:xx connected successfully.

> Note: After the desk is connected, the CLI tool should provide additional actions:

    usage: bluedesk [-h] {connect,disconnect,up,down,move} ...

    Controls lower energy actuator systems (office desks) via bluetooth.

    positional arguments:
    {connect,disconnect,up,down,move}

    optional arguments:
    -h, --help            show this help message and exit

## Move up and down

    $ bluedesk up

    OR

    $ bluedesk down

## Move to a specific position

    $ bluedesk move --to 50

> This command will move the desk to the 50% height 
