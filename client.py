import socket
import logging
import sys
import re

# Configure logging for network activity
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def is_valid_domain(domain):
    """Validate domain name format using a simple regex."""
    pattern = r'^[a-zA-Z0-9][a-zA-Z0-9-]{0,61}[a-zA-Z0-9](?:\.[a-zA-Z]{2,})+$'
    return re.match(pattern, domain) is not None

def tcp_client():
    """ TCP client that sends a domain name to a server and receives network information
    (IP addresses and simulated latency)."""
    SERVER_NAME = 'localhost'
    SERVER_PORT = 12000
    BUFFER_SIZE = 2048

    try:
        # Create a TCP socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        logger.info(f"Connecting to server at {SERVER_NAME}:{SERVER_PORT}")

        # Establish connection to the server
        client_socket.connect((SERVER_NAME, SERVER_PORT))
        logger.info(f"Connected to server at {SERVER_NAME}:{SERVER_PORT}")

        # Get user input for domain name
        domain = input('Enter a domain name (e.g., google.com) or "quit" to exit: ').strip()
        if domain.lower() == 'quit':
            logger.info("User chose to quit")
            return

        # Validate domain name
        if not is_valid_domain(domain):
            raise ValueError("Invalid domain name format. Please enter a valid domain (e.g., google.com)")

        # Send the domain name to the server
        client_socket.send(domain.encode())
        logger.info(f"Sent domain: {domain}")

        # Receive the network information from the server
        response = client_socket.recv(BUFFER_SIZE).decode()
        if not response:
            raise ConnectionError("No response received from server")

        print(f"\nNetwork Information for {domain}:\n{response}")
        logger.info(f"Received response for {domain}: {response}")

    except socket.gaierror as e:
        logger.error(f"Address resolution error: {e}")
        print(f"Error: Could not resolve server address. Please check server name and port.")
    except ConnectionError as e:
        logger.error(f"Connection error: {e}")
        print(f"Error: Failed to connect to server. Please ensure server is running.")
    except ValueError as e:
        logger.error(f"Input error: {e}")
        print(f"Error: {e}")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        print(f"Unexpected error: {e}")
    finally:
        # Ensure the socket is closed
        try:
            client_socket.close()
            logger.info("Client socket closed")
        except:
            pass

if __name__ == "__main__":
    tcp_client()
