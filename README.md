# TCP-Client-Server
Transmission Control Protocol IP finder
TCP Domain Diagnostics (Client → Server)

A fast, CLI-driven Python pair that validates a domain on the client, sends it to a localhost TCP server, resolves IPv4 addresses via OS DNS, simulates latency, and returns a formatted summary. Includes robust logging and defensive error handling for clean lab demos.

What It Does

Start a TCP server on port 12000 (SO_REUSEADDR), listen for connections.

Accept a client, read a single domain string, handle clients sequentially.

Validate domain format on the client using a regex before sending.

Resolve IPv4 addresses with getaddrinfo(), deduplicate results.

Simulate round-trip latency (uniform 10–200 ms) on the server.

Compose and return a multi-line “Domain / IPs / Simulated Latency” report.

Log key events and errors on both client and server.

Close sockets safely even on exceptions or interrupts.

Key Features Feature Benefit
Regex validation Input screening Blocks bad domains early; fewer server errors
Real DNS lookup getaddrinfo() IPv4 resolution Uses OS resolver; realistic results
Latency simulation 10–200 ms RTT Lets you test variable-latency handling
Simple protocol One request → one response Easy to reason about; great for labs
Seq. handling Serve clients one-by-one Clear control flow for teaching/debugging
Structured logs Timestamped INFO/WARN/ERROR Fast troubleshooting and reproducibility
Defensive cleanup Try/finally socket closes Graceful failures; no orphaned sockets

Outputs

Client console:
Network Information for <domain> → multi-line report (Domain, IP Address(es), Simulated Latency)

Server console:
“The server is ready to receive on port 12000” plus per-connection status

Logs (both sides):
Timestamped INFO/WARNING/ERROR entries for connects, sends/receives, responses, and exceptions
