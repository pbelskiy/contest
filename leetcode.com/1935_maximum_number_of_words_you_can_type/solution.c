int canBeTypedWords(char *text, char *brokenLetters)
{
    int t = 0;
    bool broken = false;

    for (int i = 0 ; i < strlen(text) ; i++) {
        if (!broken) {
            for (int j = 0 ; j < strlen(brokenLetters) ; j++) {
                if (text[i] == brokenLetters[j]) {
                    broken = true;
                    break;
                }
            }

        }

        if (text[i] == ' ' || i + 1 == strlen(text)) {
            if (!broken)
                t++;
            broken = false;
        }
    }

    return t;
}
