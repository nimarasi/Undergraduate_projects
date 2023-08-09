library verilog;
use verilog.vl_types.all;
entity encoder_vlg_sample_tst is
    port(
        x               : in     vl_logic_vector(3 downto 0);
        sampler_tx      : out    vl_logic
    );
end encoder_vlg_sample_tst;
