module top_module( 
    input [254:0] in,
    output [7:0] out );
    
    integer i;
    reg [7:0] counter;
    
    always @(*) begin
        counter = 0;
        for (i = 0; i < 255; i++) begin
            if (in[i] == 1'b1) counter = counter + 1'b1;
        end
    end
    
    assign out = counter;

endmodule
