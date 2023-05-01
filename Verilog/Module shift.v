// https://hdlbits.01xz.net/wiki/Module_shift

module top_module ( input clk, input d, output q );
    wire w1, w2;

    my_dff instance_1(clk, d, w1),
    	   instance_2(clk, w1, w2),
    	   instance_3(clk, w2, q);

endmodule
