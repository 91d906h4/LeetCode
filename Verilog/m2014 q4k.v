module top_module (
    input clk,
    input resetn,   // synchronous reset
    input in,
    output out);
    
    wire [3:0] q;
    
    always @(posedge clk) begin
        if (~resetn)
            q <= 0;
        else
            q <= {q[2:0], in};
    end
    
    assign out = q[3];

endmodule
