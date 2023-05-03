module counter(
	input clk, enable, reset,
    output [3:0] q
);
    
    always @(posedge clk) begin
        if (reset)
            q <= 0;
        else if (enable) begin
            if (q == 9)
                q <= 0;
            else
                q <= q + 1;
        end
    end
    
endmodule

module top_module (
    input clk,
    input reset,   // Synchronous active-high reset
    output [3:1] ena,
    output [15:0] q);
    
    assign ena[1] = q[3:0] == 9;
    assign ena[2] = (q[7:4] == 9) & (q[3:0] == 9);
    assign ena[3] = (q[11:8] == 9) & (q[7:4] == 9) & (q[3:0] == 9);

    counter instance_1(clk, 1, reset, q[3:0]),
    		instance_2(clk, ena[1], reset, q[7:4]),
    		instance_3(clk, ena[2], reset, q[11:8]),
    		instance_4(clk, ena[3], reset, q[15:12]);

endmodule
