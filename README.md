# TCP Network Diagnostics Tool

A Python-based client-server networking tool that demonstrates **TCP socket communication, DNS resolution, domain validation, network information retrieval, and structured logging**.

The project simulates a basic network diagnostic workflow: a client submits a domain name to a TCP server, the server resolves the domain to its IPv4 address(es), generates a simulated latency measurement, and returns the results to the client.

---

## Overview

This project was built to strengthen practical understanding of how networked systems communicate at the application layer.

The application uses a **TCP client-server architecture**:

```text
┌───────────────┐       TCP Connection       ┌──────────────────┐
│               │ ─────────────────────────> │                  │
│  TCP Client   │       Domain Request       │   TCP Server     │
│               │ <───────────────────────── │                  │
└───────────────┘       Network Results      └────────┬─────────┘
                                                      │
                                                      │ DNS
                                                      ▼
                                               ┌──────────────┐
                                               │ DNS Resolver │
                                               └──────────────┘
```

### Workflow

1. The client establishes a TCP connection with the server.
2. The user enters a domain name.
3. The client validates the domain format.
4. The domain is transmitted to the server over TCP.
5. The server resolves the domain using DNS.
6. IPv4 addresses are retrieved and duplicate addresses are removed.
7. A simulated network latency value is generated.
8. The server sends the diagnostic information back to the client.
9. The client displays the results and logs the network activity.
10. Connections are properly closed after communication.

---

## Features

### TCP Client-Server Communication

* Implements TCP communication using Python's `socket` library.
* Uses a dedicated client and server architecture.
* Establishes connections using a configurable host and port.
* Handles client requests and server responses.

### DNS Resolution

* Resolves domain names to IPv4 addresses.
* Uses `socket.getaddrinfo()` to retrieve network information.
* Removes duplicate IP addresses from the results.
* Provides an error message when a domain cannot be resolved.

### Domain Validation

* Uses regular expressions to validate domain-name input.
* Prevents incorrectly formatted domains from being submitted.
* Supports user exit through the `quit` command.

### Network Logging

* Uses Python's `logging` module to track network activity.
* Records connection attempts, successful connections, requests, responses, and errors.
* Provides timestamps and log severity levels for troubleshooting.

### Error Handling

The application includes handling for:

* Invalid domain names
* DNS resolution failures
* Connection failures
* Empty server responses
* Socket errors
* Unexpected runtime errors

### Connection Management

* Uses `SO_REUSEADDR` to allow the server to restart without waiting for the previous socket state to expire.
* Closes client connections after requests are processed.
* Ensures sockets are closed when the application exits.

---

## Technologies

| Technology              | Purpose                               |
| ----------------------- | ------------------------------------- |
| **Python**              | Application development               |
| **Socket Programming**  | TCP client-server communication       |
| **DNS**                 | Domain-to-IP resolution               |
| **Regular Expressions** | Domain validation                     |
| **Logging**             | Network activity and error monitoring |
| **TCP/IP**              | Transport-layer communication         |

---

## Project Structure

```text
tcp-network-diagnostics/
│
├── tcp_client.py       # TCP client application
├── tcp_server.py       # TCP server application
└── README.md           # Project documentation
```

---

## Getting Started

### Requirements

* Python 3.x
* No external Python packages are required.

The project uses Python's built-in libraries:

```python
socket
logging
sys
re
random
```

---

## Running the Project

### 1. Start the TCP Server

Open a terminal and run:

```bash
python3 tcp_server.py
```

The server will listen for incoming TCP connections on:

```text
Port: 12000
```

You should see:

```text
The server is ready to receive on port 12000
```

---

### 2. Start the TCP Client

Open a **second terminal window** and run:

```bash
python3 tcp_client.py
```

Enter a domain such as:

```text
google.com
```

The client sends the domain to the server and waits for the diagnostic response.

Example:

```text
Network Information for google.com:

Domain: google.com
IP Address(es): 142.250.xxx.xxx
Simulated Latency: 84.37 ms
```

---

## Example Network Flow

```text
User
 │
 │ Enter domain
 ▼
TCP Client
 │
 │ Validate domain
 │
 │ TCP connection
 ▼
TCP Server
 │
 │ Receive domain
 │
 │ DNS lookup
 ▼
DNS Resolver
 │
 │ IPv4 address
 ▼
TCP Server
 │
 │ Generate simulated latency
 │
 │ Send response
 ▼
TCP Client
 │
 ▼
Display network information
```

---

## Error Handling Examples

### Invalid Domain

```text
Enter a domain name: google

Error: Invalid domain name format.
```

### Server Not Running

```text
Error: Failed to connect to server.
Please ensure server is running.
```

### DNS Resolution Failure

```text
Domain: example-invalid-domain.com
IP Address(es): Error: Could not resolve domain
```

---

## What I Learned

This project provided hands-on experience with several fundamental networking concepts:

* TCP connection establishment and communication
* Client-server architecture
* Socket creation, binding, listening, and accepting connections
* DNS and IP address resolution
* Network error handling
* Port-based communication
* Connection lifecycle management
* Logging for troubleshooting and monitoring
* Input validation and defensive programming

It also provided a practical introduction to how basic network diagnostic tools communicate with services and process network information.

---

## Future Improvements

Potential improvements include:

* Replace simulated latency with **real TCP latency measurements**
* Add support for **IPv6**
* Add configurable server IP addresses and ports
* Support multiple concurrent clients using threading or asynchronous I/O
* Add connection timeout handling
* Record diagnostic results to a log file
* Add packet-loss testing
* Add port connectivity checks
* Build a command-line interface with multiple diagnostic commands
* Create a dashboard for visualizing network diagnostics
* Add automated unit and integration tests

---

## Project Purpose

The goal of this project was to move beyond theoretical networking concepts and build a working application that demonstrates how systems communicate over a network.

It is designed as a practical exercise in **network troubleshooting, TCP/IP fundamentals, DNS, socket programming, and monitoring**.

---
