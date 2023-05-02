module top_module(
    input [31:0] a,
    input [31:0] b,
    output [31:0] sum
);
    
    wire [15:0] cout1, cout2, cout3, temp1, temp2;
    
    add16 instance_1(a[15:0], b[15:0], 0, sum[15:0], cout1),
    	  instance_2(a[31:16], b[31:16], 0, temp1, cout2),
    	  instance_3(a[31:16], b[31:16], 1, temp2, cout3);
    
    always @(*) begin
        case(cout1)
            0: sum[31:16] = temp1;
            1: sum[31:16] = temp2;
        endcase
    end

endmodule
