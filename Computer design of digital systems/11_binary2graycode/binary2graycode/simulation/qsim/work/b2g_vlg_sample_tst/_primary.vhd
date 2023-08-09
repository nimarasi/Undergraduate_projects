library verilog;
use verilog.vl_types.all;
entity b2g_vlg_sample_tst is
    port(
        b               : in     vl_logic_vector(3 downto 0);
        sampler_tx      : out    vl_logic
    );
end b2g_vlg_sample_tst;
