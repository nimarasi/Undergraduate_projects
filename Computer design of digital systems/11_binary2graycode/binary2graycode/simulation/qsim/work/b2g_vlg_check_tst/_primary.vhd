library verilog;
use verilog.vl_types.all;
entity b2g_vlg_check_tst is
    port(
        g               : in     vl_logic_vector(3 downto 0);
        sampler_rx      : in     vl_logic
    );
end b2g_vlg_check_tst;
