import socket
import logging
import sys
import random
import socket as socket_lib  # Renamed to avoid conflict with socket module

# Configure logging for network activity
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def get_network_info(domain):
    """
    Retrieve network information for a domain (IP addresses and simulated latency).
    Returns formatted string with results.
    """
    try:
        # Resolve domain to IP addresses
        ip_addresses = socket_lib.getaddrinfo(domain, None, socket_lib.AF_INET)
        ip_list = [info[4][0] for info in ip_addresses]
        ip_list = list(set(ip_list))  # Remove duplicates

        # Simulate network latency (10-200 ms)
        simulated_latency = random.uniform(10, 200)

        # Format response
        response = f"Domain: {domain}\n"
        response += f"IP Address(es): {', '.join(ip_list)}\n"
        response += f"Simulated Latency: {simulated_latency:.2f} ms"
        return response
    except socket_lib.gaierror:
        return f"Error: Could not resolve domain {domain}"
    except Exception as e:
        return f"Error: Failed to retrieve network info for {domain}: {str(e)}"

def tcp_server():
    """
    TCP server that listens for client connections, receives domain names,
    and responds with network information (IP addresses and simulated latency).
    Handles multiple clients sequentially with robust error handling.
    """
    SERVER_PORT = 12000
    BUFFER_SIZE = 2048

    try:
        # Create a TCP socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(('', SERVER_PORT))
        server_socket.listen(5)
        logger.info(f"Server listening on port {SERVER_PORT}")
        print(f"The server is ready to receive on port {SERVER_PORT}")

        while True:
            try:
                # Accept a client connection
                client_socket, client_address = server_socket.accept()
                logger.info(f"Accepted connection from {client_address}")

                # Receive domain name from the client
                domain = client_socket.recv(BUFFER_SIZE).decode().strip()
                if not domain:
                    logger.warning(f"Empty message received from {client_address}")
                    client_socket.close()
                    continue

                logger.info(f"Received from {client_address}: {domain}")

                # Get network information for the domain
                response = get_network_info(domain)

                # Send the response back to the client
                client_socket.send(response.encode())
                logger.info(f"Sent to {client_address}: {response}")

                # Close the client socket
                client_socket.close()
                logger.info(f"Closed connection with {client_address}")

            except Exception as e:
                logger.error(f"Error handling client {client_address}: {e}")
                if 'client_socket' in locals():
                    client_socket.close()

    except socket.error as e:
        logger.error(f"Server socket error: {e}")
        print(f"Error: Failed to start server. {e}")
    except KeyboardInterrupt:
        logger.info("Server shutting down")
        print("Server shutting down")
    except Exception as e:
        logger.error(f"Unexpected server error: {e}")
        print(f"Unexpected error: {e}")
    finally:
        # Ensure the server socket is closed
        try:
            server_socket.close()
            logger.info("Server socket closed")
        except:
            pass

if __name__ == "__main__":
    tcp_server()
