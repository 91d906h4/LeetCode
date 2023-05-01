// https://hdlbits.01xz.net/wiki/Adder100i

module add_1(
	input a,
    input b,
    input cin,
    output cout,
    output sum
);

    assign sum = a ^ b ^ cin;
    assign cout = (a & b) | (b & cin) | (a & cin);

endmodule

module top_module( 
    input [99:0] a, b,
    input cin,
    output [99:0] cout,
    output [99:0] sum );
    
    genvar i;
    
    add_1 instance_1(a[0], b[0], cin, cout[0], sum[0]);
    
    generate
        for (i = 1; i < 100; i++) begin: gen_name
            add_1 instance_n(a[i], b[i], cout[i - 1], cout[i], sum[i]);
        end
    endgenerate

endmodule
