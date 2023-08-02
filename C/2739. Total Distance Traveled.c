int distanceTraveled(int mainTank, int additionalTank){
    int res = 0, count, temp;

    while (mainTank >= 5 && additionalTank) {
        count = mainTank / 5;
        res += count;
        mainTank %= 5;
        temp = (count < additionalTank ? count : additionalTank);
        mainTank += temp;
        additionalTank -= temp;
    }

    return res * 50 + mainTank * 10;
}
