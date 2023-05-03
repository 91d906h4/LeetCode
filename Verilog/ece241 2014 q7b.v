module top_module (
    input clk,
    input reset,
    output OneHertz,
    output [2:0] c_enable
); //
    
    wire [3:0] q0, q1, q2;
    
    assign c_enable = {q1 == 9 & q0 == 9, q0 == 9, 1'b1};
    assign OneHertz = (q0 == 9) & (q1 == 9) & (q2 == 9);

    bcdcount counter0 (clk, reset, c_enable[0], q0),
             counter1 (clk, reset, c_enable[1], q1),
             counter2 (clk, reset, c_enable[2], q2);

endmodule
