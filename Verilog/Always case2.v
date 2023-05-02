// synthesis verilog_input_version verilog_2001
module top_module (
    input [3:0] in,
    output reg [1:0] pos  );

    always @(*) begin
        casez (in[3:0])
            4'bzzz1: pos = 0;
            4'bzz1z: pos = 1;
            4'bz1zz: pos = 2;
            4'b1zzz: pos = 3;
            default: pos = 0;
        endcase
    end
    
endmodule
