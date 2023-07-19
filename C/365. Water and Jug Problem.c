int gcd(int a, int b) {
    while (b) {
        int temp = b;
        b = a % b;
        a = temp;
    }

    return a;
}

bool canMeasureWater(int jug1Capacity, int jug2Capacity, int targetCapacity){
    if (jug1Capacity + jug2Capacity < targetCapacity) return 0;
    return targetCapacity % gcd(jug1Capacity, jug2Capacity) == 0;
}
