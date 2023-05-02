// https://hdlbits.01xz.net/wiki/Thermostat

module top_module (
    input too_cold,
    input too_hot,
    input mode,
    input fan_on,
    output heater,
    output aircon,
    output fan
); 
    assign heater = mode == 1 & too_cold == 1;
    assign aircon = mode == 0 & too_hot == 1;
    assign fan = fan_on | heater | aircon;

endmodule
