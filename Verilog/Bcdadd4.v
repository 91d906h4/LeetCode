// https://hdlbits.01xz.net/wiki/Bcdadd4

module top_module ( 
    input [15:0] a, b,
    input cin,
    output cout,
    output [15:0] sum );
    
    genvar i;
    
    wire [3:0] temp;
    
    bcd_fadd instance_1(a[3:0], b[3:0], cin, temp[0], sum[3:0]);
    
    generate
        for (i = 1; i < 4; i++) begin: name
            bcd_fadd instance_2(a[i * 4+:4], b[i * 4+:4], temp[i - 1], temp[i], sum[i * 4+:4]);
        end
    endgenerate
    
    assign cout = temp[3];

endmodule
