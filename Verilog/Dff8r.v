// https://hdlbits.01xz.net/wiki/Dff8r

module top_module (
    input clk,
    input reset,            // Synchronous reset
    input [7:0] d,
    output [7:0] q
);
    
    always @(posedge clk) begin
        if (reset)
            q <= 8'b00000000;
        else
        	q <= d;
    end

endmodule
