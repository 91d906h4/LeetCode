module adder(
	input a, b, cin,
    output cout, sum
);
    
    wire t = a ^ b;
    
    assign sum = t ^ cin;
    assign cout = (a & b) | (t & cin);
    
endmodule

module top_module (
    input [3:0] x,
    input [3:0] y, 
    output [4:0] sum);
    
    wire [4:0] cout;
    
    adder instance_1(x[0], y[0], 0, cout[0], sum[0]),
    	  instance_2(x[1], y[1], cout[0], cout[1], sum[1]),
    	  instance_3(x[2], y[2], cout[1], cout[2], sum[2]),
    	  instance_4(x[3], y[3], cout[2], cout[3], sum[3]);

    assign sum[4] = cout[3];

endmodule
