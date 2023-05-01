double average(int* salary, int salarySize){
    int temp = 0, max = 0, min = *salary;

    for (int i = 0; i < salarySize; i++) {
        temp += *(salary + i);
        if (*(salary + i) < min) min = *(salary + i);
        if (*(salary + i) > max) max = *(salary + i);
    }

    return (temp - max - min) / (salarySize - 2.0);
}
