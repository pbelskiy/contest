int isPrefixOfWord(char *sentence, char *searchWord)
{
    int index = 1;
    bool first = true;

    for (int i = 0 ; i < strlen(sentence) ; i++) {
        if (sentence[i] == ' ') {
            index++;
            first = true;
            continue;
        }

        if (sentence[i] != searchWord[0] || !first) {
            first = false;
            continue;
        }

        bool found = true;

        for (int j = 1 ; j < strlen(searchWord) ; j++) {
            if (sentence[i+j] != searchWord[j]) {
                found = false;
                first = false;
                break;
            }
        }


        if (found)
            return index;
    }

    return -1;
}