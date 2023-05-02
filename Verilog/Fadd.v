// https://hdlbits.01xz.net/wiki/Fadd

module top_module( 
    input a, b, cin,
    output cout, sum );
    
    wire temp = a ^ b;
    
    assign sum = temp ^ cin;
    assign cout = (a & b) | (temp & cin);

endmodule
