module top_module(
    input clk,
    input areset,    // Freshly brainwashed Lemmings walk left.
    input bump_left,
    input bump_right,
    output walk_left,
    output walk_right); //  

    parameter L = 0, R = 1;
    reg state, next_state;

    always @(posedge clk, posedge areset) begin
        if (areset)
            next_state <= L;
        else begin
            case (state)
            	L: next_state <= bump_left ? R : L;
                R: next_state <= bump_right ? L : R;
            endcase
        end
        
        state <= next_state;
    end

    assign walk_left = state == L;
    assign walk_right = state == R;

endmodule
