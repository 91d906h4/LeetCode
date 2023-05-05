module top_module(
    input clk,
    input areset,    // Freshly brainwashed Lemmings walk left.
    input bump_left,
    input bump_right,
    input ground,
    output walk_left,
    output walk_right,
    output aaah ); 
    
    parameter L = 0, R = 1, FL = 2, FR = 3;
    wire [1:0] state, next_state;
    
    always @(*) begin
        if (ground) begin
            case (state)
                L: next_state <= bump_left ? R : L;
                R: next_state <= bump_right ? L : R;
                FL: next_state <= L;
                FR: next_state <= R;
            endcase
        end
        else begin
            case (state)
            	L: next_state <= FL;
                R: next_state <= FR;
                FL: next_state <= FL;
                FR: next_state <= FR;
            endcase
        end
    end
    
    always @(posedge clk or posedge areset) begin
        if (areset)
            state <= L;
        else
            state <= next_state;
    end
    
    assign walk_left = state == L;
    assign walk_right = state == R;
    assign aaah = (state == FL) | (state == FR);

endmodule
