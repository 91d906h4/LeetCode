int addMinimum(char * word){
    char* abc = "abc";
    int pa = 0, ps = 0, res = 0, l = strlen(word);

    while (ps < l) {
        if (abc[pa] == word[ps]) ps++;
        else res++;

        pa = (pa + 1) % 3;
    }

    return res + (pa == 0 ? 0 : 3 - pa);
}
