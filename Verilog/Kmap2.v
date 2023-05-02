module top_module(
    input a,
    input b,
    input c,
    input d,
    output out  ); 
    
    // SOP Reduction
    assign out = (~a & ~b & ~c) | (~a & ~c & ~d) | (a & ~b & ~c) | (a & c & d) | (b & c & d) | (~a & c & ~d);

endmodule
