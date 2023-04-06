class Solution {
public:
    int distMoney(int money, int children) {
        money -= children;

        if (money < 0) return -1;
        else if (money / 7 == children && money % 7 == 0) return children;
        else if (money / 7 == children - 1 && money % 7 == 3) return children - 2;
        return min(money / 7, children - 1);
    }
};
