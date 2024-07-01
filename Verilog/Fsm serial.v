module top_module(
    input clk,
    input in,
    input reset,    // Synchronous reset
    output done
); 
    
    parameter S1 = 0, S2 = 1, S3 = 2, S4 = 3, E = 4;
    reg [2:0] state, next_state, counter;
    
    always @(posedge clk) begin
        if (reset) begin
            state <= S1;
            counter <= 7;
        end else
            state <= next_state;
        
        if ((state == S2) & (counter > 0))
            counter <= counter - 1;
        else
            counter <= 7;
    end
    
    always @(*) begin
        case (state)
            S1: next_state <= in ? S1 : S2;
            S2: next_state <= (counter == 0) ? S3 : S2;
            S3: next_state <= in ? S4 : E;
            S4: next_state <= in ? S1 : S2;
            E: next_state <= in ? S1 : E;
        endcase
    end
    
    assign done = (state == S4);

endmodule
