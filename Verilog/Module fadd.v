module top_module (
    input [31:0] a,
    input [31:0] b,
    output [31:0] sum
);//
    wire [31:0] w1;
    
    add16 instance_1(a[15:0], b[15:0], 0, sum[15:0], w1[15:0]),
    instance_2(a[31:16], b[31:16], w1[15:0], sum[31:16], w1[31:16]);

endmodule

module add1 ( input a, input b, input cin,   output sum, output cout );

// Full adder module here
    assign sum = a ^ b ^ cin;
    assign cout = (a & b) | (b & cin) | (a & cin);

endmodule
