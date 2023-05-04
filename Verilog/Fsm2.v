module top_module(
    input clk,
    input areset,    // Asynchronous reset to OFF
    input j,
    input k,
    output out); //  

    parameter OFF=0, ON=1; 
    reg state, next_state;

    always @(*) begin
        // State transition logic
        case (state)
        	OFF: next_state <= j ? ON : OFF;
            ON: next_state <= k ? OFF : ON;
        endcase
    end

    always @(posedge clk, posedge areset) begin
        if (areset)
            state <= OFF;
        else
            state <= next_state;
    end

    // Output logic
    assign out = (state == OFF) ? OFF : ON;

endmodule

/*
module top_module(
    input clk,
    input areset,    // Asynchronous reset to OFF
    input j,
    input k,
    output out); //  

    parameter OFF=0, ON=1; 
    reg state, next_state;

    always @(*) begin
        // State transition logic
        if (state == OFF) begin
            if (j)
                next_state <= ON;
            else
                next_state <= state;
        end
        else begin
            if (k)
                next_state <= OFF;
            else
                next_state <= state;
        end
    end

    always @(posedge clk, posedge areset) begin
        if (areset)
            state <= OFF;
        else
            state <= next_state;
    end

    // Output logic
    assign out = (state == OFF) ? OFF : ON;

endmodule
*/
