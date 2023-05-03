module top_module(
    input clk,
    input load,
    input [511:0] data,
    output [511:0] q
); 
    
    wire [511:0] ql, qr;
    
    assign ql = {1'b0, q[511:1]};
    assign qr = {q[510:0], 1'b0};
    
    always @(posedge clk) begin
        if (load)
            q <= data;
        else begin
            q <= (q & ~qr) | (~ql & qr) | (~q & qr);
        end
    end

endmodule
