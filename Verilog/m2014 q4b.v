// https://hdlbits.01xz.net/wiki/Exams/m2014_q4b

module top_module (
    input clk,
    input d, 
    input ar,   // asynchronous reset
    output q);
    
    always @(posedge clk or posedge ar) begin
        if (ar)
            q <= 0;
        else
            q <= d;
    end

endmodule
