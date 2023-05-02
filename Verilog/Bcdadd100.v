// https://hdlbits.01xz.net/wiki/Bcdadd100

module top_module( 
    input [399:0] a, b,
    input cin,
    output cout,
    output [399:0] sum );
    
    wire [99:0] cout_t;
    genvar i;
    
    generate
        bcd_fadd instance_1(a[3:0], b[3:0], cin, cout_t[0], sum[3:0]);
        for (i = 4; i < 400; i = i + 4) begin: name
            bcd_fadd instance_2(a[i + 3:i], b[i + 3:i], cout_t[i / 4 - 1], cout_t[i / 4], sum[i + 3:i]);
        end
    endgenerate
    
    assign cout = cout_t[99];

endmodule
