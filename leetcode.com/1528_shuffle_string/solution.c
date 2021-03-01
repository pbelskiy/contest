char * restoreString(char *s, int *indices, int indicesSize)
{
    char *r = (char*) calloc(strlen(s) + 1, sizeof(char));

    for (int i = 0 ; i < indicesSize ; i++) 
        r[indices[i]] = s[i];

    return r;
}
