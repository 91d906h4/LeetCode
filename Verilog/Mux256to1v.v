// https://hdlbits.01xz.net/wiki/Mux256to1v

module top_module( 
    input [1023:0] in,
    input [7:0] sel,
    output [3:0] out );
    
    assign out = in[sel * 4+:4];
    // in[sel * 4+:4] is as same as in[sel * 4 + 3:sel * 4]
    // and in[sel * 4 + 3:sel * 4] is not allowed because if
    // we want to select a range from a vector V[A:B], A and
    // B must be a constans.

endmodule
