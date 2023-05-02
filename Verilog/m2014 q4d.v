// https://hdlbits.01xz.net/wiki/Exams/m2014_q4d

module top_module (
    input clk,
    input in, 
    output out);
    
    always @(posedge clk) begin
    	out <= in ^ out;
    end

endmodule
