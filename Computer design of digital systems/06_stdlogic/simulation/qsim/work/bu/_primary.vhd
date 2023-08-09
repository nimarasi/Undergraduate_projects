library verilog;
use verilog.vl_types.all;
entity bu is
    port(
        a               : in     vl_logic;
        b               : in     vl_logic;
        oe              : in     vl_logic;
        y               : out    vl_logic
    );
end bu;
