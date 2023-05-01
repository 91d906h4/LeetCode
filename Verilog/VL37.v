// https://www.nowcoder.com/practice/49a7277c203a4ddd956fa385e687a72e

`timescale 1ns/1ns

module even_div
    (
    input     wire rst ,
    input     wire clk_in,
    output    wire clk_out2,
    output    wire clk_out4,
    output    wire clk_out8
    );
//*************code***********//

    reg [2:0] counter;

    always @(posedge clk_in or negedge rst)
        if (!rst)
            counter <= 3'b011;
        else
            counter <= counter + 1;
    
    assign clk_out2 = ~counter[0];
    assign clk_out4 = ~counter[1];
    assign clk_out8 = counter[2];

//*************code***********//
endmodule
