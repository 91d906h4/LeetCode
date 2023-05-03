module top_module (
    input [3:0] SW,
    input [3:0] KEY,
    output [3:0] LEDR
); //
    
    MUXDFF instance_1(KEY[0], KEY[2], KEY[1], SW[3], KEY[3], LEDR[3]),
    	   instance_2(KEY[0], KEY[2], KEY[1], SW[2], LEDR[3], LEDR[2]),
    	   instance_3(KEY[0], KEY[2], KEY[1], SW[1], LEDR[2], LEDR[1]),
    	   instance_4(KEY[0], KEY[2], KEY[1], SW[0], LEDR[1], LEDR[0]);

endmodule

module MUXDFF (
	input clk, l, e,
    input i1, i2,
    output reg q
);
    
    always @(posedge clk) begin
        if (l)
            q <= i1;
        else if (e)
            q <= i2;
        else
            q <= q;
    end

endmodule
