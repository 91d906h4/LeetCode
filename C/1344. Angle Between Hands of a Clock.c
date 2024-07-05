double angleClock(int hour, int minutes) {
    if (hour == 12) hour = 0;

    double a = hour * 30 + minutes * 0.5;
    double b = minutes * 6;
    double c = (a - b > 0) ? (a - b) : (b - a);

    return (c > 180) ? (360 - c) : c;
}
