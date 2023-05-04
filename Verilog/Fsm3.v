module top_module(
    input clk,
    input in,
    input areset,
    output out); //

    // State transition logic
    parameter A = 0, B = 1, C = 2, D = 3;
    wire [1:0] state, next_state;

    // State flip-flops with asynchronous reset
    always @(posedge clk or posedge areset) begin
        if (areset) 
            state <= A;
       	else begin
            case (state)
                A: next_state = in ? B : A;
                B: next_state = in ? B : C;
                C: next_state = in ? D : A;
                D: next_state = in ? B : C;
            endcase

            state <= next_state;
        end
    end

    // Output logic
    assign out = state == D;

endmodule
