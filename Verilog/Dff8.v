// https://hdlbits.01xz.net/wiki/Dff8

module top_module (
    input clk,
    input [7:0] d,
    output [7:0] q
);
    always @(posedge clk) begin
    	q <= d;
    end

endmodule
