// https://hdlbits.01xz.net/wiki/Adder3

module adder(
	input a, b, cin,
    output cout, sum
);
    
    wire t = a ^ b;
    
    assign sum = t ^ cin;
    assign cout = (a & b) | (t & cin);
    
endmodule

module top_module( 
    input [2:0] a, b,
    input cin,
    output [2:0] cout,
    output [2:0] sum );
    
    adder instance_1(a[0], b[0], cin, cout[0], sum[0]),
    	  instance_2(a[1], b[1], cout[0], cout[1], sum[1]),
    	  instance_3(a[2], b[2], cout[1], cout[2], sum[2]);

endmodule
