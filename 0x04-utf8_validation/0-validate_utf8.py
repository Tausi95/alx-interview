#!/usr/bin/python3

def validUTF8(data):
    # Number of bytes to process in the current UTF-8 character
    bytes_to_process = 0

    # Masks for checking byte patterns
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        # Mask to get only the last 8 bits
        byte = num & 0xFF
        
        if bytes_to_process == 0:
            # Determine the number of bytes in the UTF-8 character
            mask = 1 << 7
            while mask & byte:
                bytes_to_process += 1
                mask >>= 1
            
            # For 1 byte, it should be 0xxxxxxx
            if bytes_to_process == 0:
                continue
            
            # UTF-8 characters are between 2 and 4 bytes, otherwise invalid
            if bytes_to_process == 1 or bytes_to_process > 4:
                return False
        else:
            # The following bytes should be of the form 10xxxxxx
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrement the bytes left to process
        bytes_to_process -= 1

    # If we have processed all bytes successfully
    return bytes_to_process == 0
