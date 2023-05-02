module top_module (
    input clk,
    input reset,
    input [31:0] in,
    output [31:0] out
);
    
    reg [31:0] temp;
    wire [31:0] capture;
    
    always @(posedge clk)
    	temp <= in;
    
    assign capture = ~in & temp;
    
    always @(posedge clk) begin
        if (reset)
            out <= 32'b0;
        else begin
            for (int i = 0; i < 32; i++) begin
                if (capture[i] == 1'b1)
                    out[i] = 1'b1;
            end
        end
    end

endmodule
