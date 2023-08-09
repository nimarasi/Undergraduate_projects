library verilog;
use verilog.vl_types.all;
entity ALU is
    port(
        a               : in     vl_logic_vector(2 downto 0);
        b               : in     vl_logic_vector(2 downto 0);
        c               : in     vl_logic;
        sel             : in     vl_logic_vector(1 downto 0);
        result          : out    vl_logic_vector(5 downto 0)
    );
end ALU;
