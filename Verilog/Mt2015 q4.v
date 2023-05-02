// https://hdlbits.01xz.net/wiki/Mt2015_q4

module top_module (input x, input y, output z);
    assign z = (x == 0 & y == 1) ? 0 : 1;
endmodule
