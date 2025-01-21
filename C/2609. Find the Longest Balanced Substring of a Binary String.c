int findTheLongestBalancedSubstring(char* s) {
    int stack = 0, result = 0, max = 0;
    int i = -1;

    while (s[++i] != '\0') {
        if (s[i] == '0') {
            // If max is not zero, it means that
            // there must be one(s) before this 0,
            // so we need to reset the stack to
            // count continues zeros again.
            if (max > 0) {
                stack = 0;
                max = 0;
            }

            stack++;
        } else if (s[i] == '1' && stack > 0) {
            max++;
            stack--;
        }

        if (max > result)
            result = max;
    }

    return result * 2;
}
