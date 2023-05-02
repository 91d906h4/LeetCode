module top_module( 
    input [2:0] in,
    output [1:0] out );
    
    always @(*) begin
        casez(in)
            3'b111: out = 2'b11;
            3'b11z: out = 2'b10;
            3'b1z1: out = 2'b10;
            3'bz11: out = 2'b10;
            3'b1zz: out = 2'b01;
            3'bz1z: out = 2'b01;
            3'bzz1: out = 2'b01;
            default: out = 2'b00;
        endcase
    end

endmodule
