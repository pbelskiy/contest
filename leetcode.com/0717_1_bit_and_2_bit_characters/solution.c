bool isOneBitCharacter(int* bits, int bitsSize)
{
    int pos = 0;
    bool found = false;
    
    while (pos < bitsSize) {
        if (bits[pos+0] == 1 && (bits[pos+1] == 1 || bits[pos+1] == 0) && pos + 2 <= bitsSize) {
            pos += 2;
        } else {
            pos += 1;
            
            if (pos >= bitsSize)
                found = true;
        }
    }
    
    return found;
}

