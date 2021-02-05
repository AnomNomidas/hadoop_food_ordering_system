from tcp_client import *
import static_test

# Declare global variables here
DEBUG_TAG = "[client]:"
sendingClient = None
# receivingServerAddr = "54.235.237.72"
receivingServerAddr = "127.0.0.1"
receivingServerPort = 8001

def print_debug_info(*info_to_print):
    print(DEBUG_TAG, ' '.join(info_to_print))

# Main function
def main():
    sendingClient = TCPClient()
    sendingClient.connect(receivingServerAddr, receivingServerPort)
    print_debug_info("Connected to server!")
    temp_filename = "This is a test file name"
    sending_result = sendingClient.send_file_name(temp_filename)
    print_debug_info("sending_result:", str(sending_result))
    sending_result = sendingClient.send_file(static_test.test_str)
    print_debug_info("sending_result:", str(sending_result))
    
# Run main()
if __name__ == "__main__":
    main()