onerror {exit -code 1}
vlib work
vlog -work work binary2graycode.vo
vlog -work work Waveform.vwf.vt
vsim -novopt -c -t 1ps -L cycloneiv_ver -L altera_ver -L altera_mf_ver -L 220model_ver -L sgate work.b2g_vlg_vec_tst -voptargs="+acc"
vcd file -direction binary2graycode.msim.vcd
vcd add -internal b2g_vlg_vec_tst/*
vcd add -internal b2g_vlg_vec_tst/i1/*
run -all
quit -f
