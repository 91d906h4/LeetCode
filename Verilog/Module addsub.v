// https://hdlbits.01xz.net/wiki/Module_addsub

module top_module(
    input [31:0] a,
    input [31:0] b,
    input sub,
    output [31:0] sum
);
    wire [31:0] temp;
    wire cout;
    
    assign temp = b ^ {32{sub}};
    
    add16 instance_1(a[15:0], temp[15:0], sub, sum[15:0], cout),
    	  instance_2(a[31:16], temp[31:16], cout, sum[31:16]);

endmodule
