library verilog;
use verilog.vl_types.all;
entity encoder is
    port(
        x               : in     vl_logic_vector(3 downto 0);
        y0              : out    vl_logic;
        y1              : out    vl_logic
    );
end encoder;
