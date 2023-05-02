// https://hdlbits.01xz.net/wiki/Exams/m2014_q4a

module top_module (
    input d, 
    input ena,
    output q);
    
    always @(*) begin
        if (ena)
            q <= d;
        else
            q <= q;
    end

endmodule
