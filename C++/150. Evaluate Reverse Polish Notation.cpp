class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<string> s;

        for (string token: tokens) {
            if (token == "+") {
                int b = stoi(s.top()); s.pop();
                int a = stoi(s.top()); s.pop();
                s.push(to_string(a + b));
            }
            else if (token == "-") {
                int b = stoi(s.top()); s.pop();
                int a = stoi(s.top()); s.pop();
                s.push(to_string(a - b));
            }
            else if (token == "*") {
                int b = stoi(s.top()); s.pop();
                int a = stoi(s.top()); s.pop();
                s.push(to_string(a * b));
            }
            else if (token == "/") {
                int b = stoi(s.top()); s.pop();
                int a = stoi(s.top()); s.pop();
                s.push(to_string(a / b));
            }
            else s.push(token);
        }

        return stoi(s.top());
    }
};
