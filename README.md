# Telnetcheck

#### Table of Contents

1. [Overview - What is telnetcheck?](#overview)
1. [Module Description - What does the module do?](#module-description)
1. [Setup - The basics of getting started with telnetcheck](#setup)
1. [Usage - Configuration options and additional functionality](#usage)
    * [Examples](#examples)
    * [Parameter Reference](#parameter-reference)
1. [Limitations - OS compatibility, etc.](#limitations)


## Overview

This module runs a script that checks for open telnet ports.


## Module Description

This script should support Ubuntu 14.04/16.04/18.04, Debian 7/8 and RedHat derivates 6/7.

This module will install a script using python 3

## Setup

1. Download the repository
2. Make the script runnable with `chmod +x telnetcheck.py`  
3. Run the script in two ways
    * `./telnetcheck.py <DOMAIN> <startPort> <endPort>`
    * `./telnetcheck.py <DOMAIN> <port>`

## Usage

### Examples

```
./telnetcheck.py example.com 21 53
```

```
./telnetcheck.py example.com 23
```

### Parameter Reference

|Parameter|Description|
|---------|-----------|
|DOMAIN|Domain name or ip address to search|
|startPort|Starting port to search|
|endPort|Ending port to search|
|port|Search only one port|



## Limitations

Only tried on Kali linux
