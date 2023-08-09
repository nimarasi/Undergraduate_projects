-- Copyright (C) 1991-2013 Altera Corporation
-- Your use of Altera Corporation's design tools, logic functions 
-- and other software and tools, and its AMPP partner logic 
-- functions, and any output files from any of the foregoing 
-- (including device programming or simulation files), and any 
-- associated documentation or information are expressly subject 
-- to the terms and conditions of the Altera Program License 
-- Subscription Agreement, Altera MegaCore Function License 
-- Agreement, or other applicable license agreement, including, 
-- without limitation, that your use is for the sole purpose of 
-- programming logic devices manufactured by Altera and sold by 
-- Altera or its authorized distributors.  Please refer to the 
-- applicable agreement for further details.

-- VENDOR "Altera"
-- PROGRAM "Quartus II 64-Bit"
-- VERSION "Version 13.1.0 Build 162 10/23/2013 SJ Web Edition"

-- DATE "12/31/2022 22:49:19"

-- 
-- Device: Altera EP4CGX15BF14C6 Package FBGA169
-- 

-- 
-- This VHDL file should be used for ModelSim-Altera (VHDL) only
-- 

LIBRARY CYCLONEIV;
LIBRARY IEEE;
USE CYCLONEIV.CYCLONEIV_COMPONENTS.ALL;
USE IEEE.STD_LOGIC_1164.ALL;

ENTITY 	ALU IS
    PORT (
	a : IN std_logic_vector(2 DOWNTO 0);
	b : IN std_logic_vector(2 DOWNTO 0);
	c : IN std_logic;
	sel : IN std_logic_vector(1 DOWNTO 0);
	result : OUT std_logic_vector(5 DOWNTO 0)
	);
END ALU;

-- Design Ports Information
-- result[0]	=>  Location: PIN_L7,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- result[1]	=>  Location: PIN_K12,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- result[2]	=>  Location: PIN_A8,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- result[3]	=>  Location: PIN_M4,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- result[4]	=>  Location: PIN_F11,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- result[5]	=>  Location: PIN_L13,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- a[0]	=>  Location: PIN_B6,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- b[0]	=>  Location: PIN_M9,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- c	=>  Location: PIN_K8,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- sel[1]	=>  Location: PIN_N4,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- sel[0]	=>  Location: PIN_A6,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- a[1]	=>  Location: PIN_M6,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- b[1]	=>  Location: PIN_L4,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- b[2]	=>  Location: PIN_J13,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- a[2]	=>  Location: PIN_F10,	 I/O Standard: 2.5 V,	 Current Strength: Default


ARCHITECTURE structure OF ALU IS
SIGNAL gnd : std_logic := '0';
SIGNAL vcc : std_logic := '1';
SIGNAL unknown : std_logic := 'X';
SIGNAL devoe : std_logic := '1';
SIGNAL devclrn : std_logic := '1';
SIGNAL devpor : std_logic := '1';
SIGNAL ww_devoe : std_logic;
SIGNAL ww_devclrn : std_logic;
SIGNAL ww_devpor : std_logic;
SIGNAL ww_a : std_logic_vector(2 DOWNTO 0);
SIGNAL ww_b : std_logic_vector(2 DOWNTO 0);
SIGNAL ww_c : std_logic;
SIGNAL ww_sel : std_logic_vector(1 DOWNTO 0);
SIGNAL ww_result : std_logic_vector(5 DOWNTO 0);
SIGNAL \result[0]~output_o\ : std_logic;
SIGNAL \result[1]~output_o\ : std_logic;
SIGNAL \result[2]~output_o\ : std_logic;
SIGNAL \result[3]~output_o\ : std_logic;
SIGNAL \result[4]~output_o\ : std_logic;
SIGNAL \result[5]~output_o\ : std_logic;
SIGNAL \sel[1]~input_o\ : std_logic;
SIGNAL \sel[0]~input_o\ : std_logic;
SIGNAL \Mux4~0_combout\ : std_logic;
SIGNAL \c~input_o\ : std_logic;
SIGNAL \b[0]~input_o\ : std_logic;
SIGNAL \a[0]~input_o\ : std_logic;
SIGNAL \Mux5~0_combout\ : std_logic;
SIGNAL \Mux5~1_combout\ : std_logic;
SIGNAL \alu2|fs1|bout~0_combout\ : std_logic;
SIGNAL \b[1]~input_o\ : std_logic;
SIGNAL \a[1]~input_o\ : std_logic;
SIGNAL \alu1|fa2|ha2|s~0_combout\ : std_logic;
SIGNAL \Mux4~2_combout\ : std_logic;
SIGNAL \alu3|ha1|s~combout\ : std_logic;
SIGNAL \alu1|fa1|cout~0_combout\ : std_logic;
SIGNAL \Mux4~1_combout\ : std_logic;
SIGNAL \Mux4~3_combout\ : std_logic;
SIGNAL \a[2]~input_o\ : std_logic;
SIGNAL \alu2|fs2|bout~0_combout\ : std_logic;
SIGNAL \b[2]~input_o\ : std_logic;
SIGNAL \alu2|fs3|diff~combout\ : std_logic;
SIGNAL \alu3|ha1|cout~combout\ : std_logic;
SIGNAL \alu3|f3~combout\ : std_logic;
SIGNAL \alu3|fa1|ha2|s~combout\ : std_logic;
SIGNAL \Mux3~0_combout\ : std_logic;
SIGNAL \Mux3~1_combout\ : std_logic;
SIGNAL \Mux2~2_combout\ : std_logic;
SIGNAL \alu3|ha3|cout~combout\ : std_logic;
SIGNAL \alu3|fa1|cout~0_combout\ : std_logic;
SIGNAL \alu3|ha2|s~combout\ : std_logic;
SIGNAL \Mux2~3_combout\ : std_logic;
SIGNAL \Mux2~4_combout\ : std_logic;
SIGNAL \alu1|fa4|cout~0_combout\ : std_logic;
SIGNAL \alu3|fa2|cout~0_combout\ : std_logic;
SIGNAL \alu3|ha2|cout~combout\ : std_logic;
SIGNAL \Mux1~0_combout\ : std_logic;
SIGNAL \alu3|fa3|cout~0_combout\ : std_logic;
SIGNAL \Mux0~2_combout\ : std_logic;

BEGIN

ww_a <= a;
ww_b <= b;
ww_c <= c;
ww_sel <= sel;
result <= ww_result;
ww_devoe <= devoe;
ww_devclrn <= devclrn;
ww_devpor <= devpor;

-- Location: IOOBUF_X14_Y0_N2
\result[0]~output\ : cycloneiv_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false")
-- pragma translate_on
PORT MAP (
	i => \Mux5~1_combout\,
	devoe => ww_devoe,
	o => \result[0]~output_o\);

-- Location: IOOBUF_X33_Y11_N9
\result[1]~output\ : cycloneiv_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false")
-- pragma translate_on
PORT MAP (
	i => \Mux4~3_combout\,
	devoe => ww_devoe,
	o => \result[1]~output_o\);

-- Location: IOOBUF_X12_Y31_N9
\result[2]~output\ : cycloneiv_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false")
-- pragma translate_on
PORT MAP (
	i => \Mux3~1_combout\,
	devoe => ww_devoe,
	o => \result[2]~output_o\);

-- Location: IOOBUF_X8_Y0_N2
\result[3]~output\ : cycloneiv_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false")
-- pragma translate_on
PORT MAP (
	i => \Mux2~4_combout\,
	devoe => ww_devoe,
	o => \result[3]~output_o\);

-- Location: IOOBUF_X33_Y24_N9
\result[4]~output\ : cycloneiv_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false")
-- pragma translate_on
PORT MAP (
	i => \Mux1~0_combout\,
	devoe => ww_devoe,
	o => \result[4]~output_o\);

-- Location: IOOBUF_X33_Y12_N9
\result[5]~output\ : cycloneiv_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false")
-- pragma translate_on
PORT MAP (
	i => \Mux0~2_combout\,
	devoe => ww_devoe,
	o => \result[5]~output_o\);

-- Location: IOIBUF_X10_Y0_N8
\sel[1]~input\ : cycloneiv_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_sel(1),
	o => \sel[1]~input_o\);

-- Location: IOIBUF_X10_Y31_N1
\sel[0]~input\ : cycloneiv_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_sel(0),
	o => \sel[0]~input_o\);

-- Location: LCCOMB_X5_Y1_N26
\Mux4~0\ : cycloneiv_lcell_comb
-- Equation(s):
-- \Mux4~0_combout\ = (\sel[1]~input_o\ & !\sel[0]~input_o\)

-- pragma translate_off
GENERIC MAP (
	lut_mask => "0000000011110000",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	datac => \sel[1]~input_o\,
	datad => \sel[0]~input_o\,
	combout => \Mux4~0_combout\);

-- Location: IOIBUF_X22_Y0_N8
\c~input\ : cycloneiv_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_c,
	o => \c~input_o\);

-- Location: IOIBUF_X24_Y0_N1
\b[0]~input\ : cycloneiv_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_b(0),
	o => \b[0]~input_o\);

-- Location: IOIBUF_X14_Y31_N8
\a[0]~input\ : cycloneiv_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_a(0),
	o => \a[0]~input_o\);

-- Location: LCCOMB_X5_Y1_N16
\Mux5~0\ : cycloneiv_lcell_comb
-- Equation(s):
-- \Mux5~0_combout\ = (!\sel[1]~input_o\ & (\c~input_o\ $ (\b[0]~input_o\ $ (\a[0]~input_o\))))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "0010000100010010",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \c~input_o\,
	datab => \sel[1]~input_o\,
	datac => \b[0]~input_o\,
	datad => \a[0]~input_o\,
	combout => \Mux5~0_combout\);

-- Location: LCCOMB_X5_Y1_N4
\Mux5~1\ : cycloneiv_lcell_comb
-- Equation(s):
-- \Mux5~1_combout\ = (\Mux5~0_combout\) # ((\Mux4~0_combout\ & (\b[0]~input_o\ & \a[0]~input_o\)))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "1110110011001100",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \Mux4~0_combout\,
	datab => \Mux5~0_combout\,
	datac => \b[0]~input_o\,
	datad => \a[0]~input_o\,
	combout => \Mux5~1_combout\);

-- Location: LCCOMB_X5_Y1_N28
\alu2|fs1|bout~0\ : cycloneiv_lcell_comb
-- Equation(s):
-- \alu2|fs1|bout~0_combout\ = (\c~input_o\ & ((\b[0]~input_o\) # (!\a[0]~input_o\))) # (!\c~input_o\ & (\b[0]~input_o\ & !\a[0]~input_o\))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "1010000011111010",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \c~input_o\,
	datac => \b[0]~input_o\,
	datad => \a[0]~input_o\,
	combout => \alu2|fs1|bout~0_combout\);

-- Location: IOIBUF_X8_Y0_N8
\b[1]~input\ : cycloneiv_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_b(1),
	o => \b[1]~input_o\);

-- Location: IOIBUF_X12_Y0_N8
\a[1]~input\ : cycloneiv_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_a(1),
	o => \a[1]~input_o\);

-- Location: LCCOMB_X5_Y1_N8
\alu1|fa2|ha2|s~0\ : cycloneiv_lcell_comb
-- Equation(s):
-- \alu1|fa2|ha2|s~0_combout\ = \b[1]~input_o\ $ (\a[1]~input_o\)

-- pragma translate_off
GENERIC MAP (
	lut_mask => "0011110000111100",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	datab => \b[1]~input_o\,
	datac => \a[1]~input_o\,
	combout => \alu1|fa2|ha2|s~0_combout\);

-- Location: LCCOMB_X5_Y1_N22
\Mux4~2\ : cycloneiv_lcell_comb
-- Equation(s):
-- \Mux4~2_combout\ = (!\sel[1]~input_o\ & (\sel[0]~input_o\ & (\alu2|fs1|bout~0_combout\ $ (\alu1|fa2|ha2|s~0_combout\))))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "0000011000000000",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \alu2|fs1|bout~0_combout\,
	datab => \alu1|fa2|ha2|s~0_combout\,
	datac => \sel[1]~input_o\,
	datad => \sel[0]~input_o\,
	combout => \Mux4~2_combout\);

-- Location: LCCOMB_X5_Y1_N0
\alu3|ha1|s\ : cycloneiv_lcell_comb
-- Equation(s):
-- \alu3|ha1|s~combout\ = (\b[1]~input_o\ & (\a[0]~input_o\ $ (((\a[1]~input_o\ & \b[0]~input_o\))))) # (!\b[1]~input_o\ & (\a[1]~input_o\ & (\b[0]~input_o\)))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "0110101011000000",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \b[1]~input_o\,
	datab => \a[1]~input_o\,
	datac => \b[0]~input_o\,
	datad => \a[0]~input_o\,
	combout => \alu3|ha1|s~combout\);

-- Location: LCCOMB_X5_Y1_N6
\alu1|fa1|cout~0\ : cycloneiv_lcell_comb
-- Equation(s):
-- \alu1|fa1|cout~0_combout\ = (\c~input_o\ & ((\b[0]~input_o\) # (\a[0]~input_o\))) # (!\c~input_o\ & (\b[0]~input_o\ & \a[0]~input_o\))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "1111101010100000",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \c~input_o\,
	datac => \b[0]~input_o\,
	datad => \a[0]~input_o\,
	combout => \alu1|fa1|cout~0_combout\);

-- Location: LCCOMB_X5_Y1_N10
\Mux4~1\ : cycloneiv_lcell_comb
-- Equation(s):
-- \Mux4~1_combout\ = (!\sel[1]~input_o\ & (!\sel[0]~input_o\ & (\alu1|fa1|cout~0_combout\ $ (\alu1|fa2|ha2|s~0_combout\))))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "0000000000000110",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \alu1|fa1|cout~0_combout\,
	datab => \alu1|fa2|ha2|s~0_combout\,
	datac => \sel[1]~input_o\,
	datad => \sel[0]~input_o\,
	combout => \Mux4~1_combout\);

-- Location: LCCOMB_X5_Y1_N2
\Mux4~3\ : cycloneiv_lcell_comb
-- Equation(s):
-- \Mux4~3_combout\ = (\Mux4~2_combout\) # ((\Mux4~1_combout\) # ((\alu3|ha1|s~combout\ & \Mux4~0_combout\)))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "1111111111101010",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \Mux4~2_combout\,
	datab => \alu3|ha1|s~combout\,
	datac => \Mux4~0_combout\,
	datad => \Mux4~1_combout\,
	combout => \Mux4~3_combout\);

-- Location: IOIBUF_X33_Y24_N1
\a[2]~input\ : cycloneiv_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_a(2),
	o => \a[2]~input_o\);

-- Location: LCCOMB_X5_Y1_N18
\alu2|fs2|bout~0\ : cycloneiv_lcell_comb
-- Equation(s):
-- \alu2|fs2|bout~0_combout\ = (\alu2|fs1|bout~0_combout\ & ((\b[1]~input_o\) # (!\a[1]~input_o\))) # (!\alu2|fs1|bout~0_combout\ & (!\a[1]~input_o\ & \b[1]~input_o\))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "1100111100001100",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	datab => \alu2|fs1|bout~0_combout\,
	datac => \a[1]~input_o\,
	datad => \b[1]~input_o\,
	combout => \alu2|fs2|bout~0_combout\);

-- Location: IOIBUF_X33_Y15_N8
\b[2]~input\ : cycloneiv_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_b(2),
	o => \b[2]~input_o\);

-- Location: LCCOMB_X1_Y8_N26
\alu2|fs3|diff\ : cycloneiv_lcell_comb
-- Equation(s):
-- \alu2|fs3|diff~combout\ = \a[2]~input_o\ $ (\alu2|fs2|bout~0_combout\ $ (\b[2]~input_o\))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "1001100101100110",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \a[2]~input_o\,
	datab => \alu2|fs2|bout~0_combout\,
	datad => \b[2]~input_o\,
	combout => \alu2|fs3|diff~combout\);

-- Location: LCCOMB_X5_Y1_N30
\alu3|ha1|cout\ : cycloneiv_lcell_comb
-- Equation(s):
-- \alu3|ha1|cout~combout\ = (\b[1]~input_o\ & (\a[1]~input_o\ & (\b[0]~input_o\ & \a[0]~input_o\)))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "1000000000000000",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \b[1]~input_o\,
	datab => \a[1]~input_o\,
	datac => \b[0]~input_o\,
	datad => \a[0]~input_o\,
	combout => \alu3|ha1|cout~combout\);

-- Location: LCCOMB_X5_Y1_N12
\alu3|f3\ : cycloneiv_lcell_comb
-- Equation(s):
-- \alu3|f3~combout\ = (\a[0]~input_o\ & \b[2]~input_o\)

-- pragma translate_off
GENERIC MAP (
	lut_mask => "1100000011000000",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	datab => \a[0]~input_o\,
	datac => \b[2]~input_o\,
	combout => \alu3|f3~combout\);

-- Location: LCCOMB_X5_Y1_N24
\alu3|fa1|ha2|s\ : cycloneiv_lcell_comb
-- Equation(s):
-- \alu3|fa1|ha2|s~combout\ = \alu3|ha1|cout~combout\ $ (\alu3|f3~combout\ $ (((\b[1]~input_o\ & \a[1]~input_o\))))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "1001010101101010",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \alu3|ha1|cout~combout\,
	datab => \b[1]~input_o\,
	datac => \a[1]~input_o\,
	datad => \alu3|f3~combout\,
	combout => \alu3|fa1|ha2|s~combout\);

-- Location: LCCOMB_X1_Y8_N0
\Mux3~0\ : cycloneiv_lcell_comb
-- Equation(s):
-- \Mux3~0_combout\ = (!\sel[0]~input_o\ & (\alu3|fa1|ha2|s~combout\ $ (((\b[0]~input_o\ & \a[2]~input_o\)))))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "0001001000110000",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \b[0]~input_o\,
	datab => \sel[0]~input_o\,
	datac => \alu3|fa1|ha2|s~combout\,
	datad => \a[2]~input_o\,
	combout => \Mux3~0_combout\);

-- Location: LCCOMB_X1_Y8_N28
\Mux3~1\ : cycloneiv_lcell_comb
-- Equation(s):
-- \Mux3~1_combout\ = (\Mux3~0_combout\) # ((\alu2|fs3|diff~combout\ & (!\sel[1]~input_o\ & \sel[0]~input_o\)))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "1100111011001100",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \alu2|fs3|diff~combout\,
	datab => \Mux3~0_combout\,
	datac => \sel[1]~input_o\,
	datad => \sel[0]~input_o\,
	combout => \Mux3~1_combout\);

-- Location: LCCOMB_X1_Y8_N22
\Mux2~2\ : cycloneiv_lcell_comb
-- Equation(s):
-- \Mux2~2_combout\ = (\a[2]~input_o\ & (\b[2]~input_o\ & ((\alu2|fs2|bout~0_combout\) # (!\sel[0]~input_o\)))) # (!\a[2]~input_o\ & (\sel[0]~input_o\ & ((\b[2]~input_o\) # (\alu2|fs2|bout~0_combout\))))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "1101010010001000",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \a[2]~input_o\,
	datab => \b[2]~input_o\,
	datac => \alu2|fs2|bout~0_combout\,
	datad => \sel[0]~input_o\,
	combout => \Mux2~2_combout\);

-- Location: LCCOMB_X1_Y8_N10
\alu3|ha3|cout\ : cycloneiv_lcell_comb
-- Equation(s):
-- \alu3|ha3|cout~combout\ = (\b[0]~input_o\ & (\alu3|fa1|ha2|s~combout\ & \a[2]~input_o\))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "1000100000000000",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \b[0]~input_o\,
	datab => \alu3|fa1|ha2|s~combout\,
	datad => \a[2]~input_o\,
	combout => \alu3|ha3|cout~combout\);

-- Location: LCCOMB_X5_Y1_N20
\alu3|fa1|cout~0\ : cycloneiv_lcell_comb
-- Equation(s):
-- \alu3|fa1|cout~0_combout\ = (\alu3|ha1|cout~combout\ & ((\alu3|f3~combout\) # ((\b[1]~input_o\ & \a[1]~input_o\)))) # (!\alu3|ha1|cout~combout\ & (\b[1]~input_o\ & (\a[1]~input_o\ & \alu3|f3~combout\)))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "1110101010000000",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \alu3|ha1|cout~combout\,
	datab => \b[1]~input_o\,
	datac => \a[1]~input_o\,
	datad => \alu3|f3~combout\,
	combout => \alu3|fa1|cout~0_combout\);

-- Location: LCCOMB_X1_Y8_N16
\alu3|ha2|s\ : cycloneiv_lcell_comb
-- Equation(s):
-- \alu3|ha2|s~combout\ = \alu3|fa1|cout~0_combout\ $ (((\a[1]~input_o\ & \b[2]~input_o\)))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "0110011010101010",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \alu3|fa1|cout~0_combout\,
	datab => \a[1]~input_o\,
	datad => \b[2]~input_o\,
	combout => \alu3|ha2|s~combout\);

-- Location: LCCOMB_X1_Y8_N12
\Mux2~3\ : cycloneiv_lcell_comb
-- Equation(s):
-- \Mux2~3_combout\ = \alu3|ha3|cout~combout\ $ (\alu3|ha2|s~combout\ $ (((\b[1]~input_o\ & \a[2]~input_o\))))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "1001011001100110",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \alu3|ha3|cout~combout\,
	datab => \alu3|ha2|s~combout\,
	datac => \b[1]~input_o\,
	datad => \a[2]~input_o\,
	combout => \Mux2~3_combout\);

-- Location: LCCOMB_X1_Y8_N8
\Mux2~4\ : cycloneiv_lcell_comb
-- Equation(s):
-- \Mux2~4_combout\ = (\sel[1]~input_o\ & (((!\sel[0]~input_o\ & \Mux2~3_combout\)))) # (!\sel[1]~input_o\ & (\Mux2~2_combout\))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "0011101000001010",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \Mux2~2_combout\,
	datab => \sel[0]~input_o\,
	datac => \sel[1]~input_o\,
	datad => \Mux2~3_combout\,
	combout => \Mux2~4_combout\);

-- Location: LCCOMB_X1_Y8_N30
\alu1|fa4|cout~0\ : cycloneiv_lcell_comb
-- Equation(s):
-- \alu1|fa4|cout~0_combout\ = (\b[2]~input_o\ & \a[2]~input_o\)

-- pragma translate_off
GENERIC MAP (
	lut_mask => "1100110000000000",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	datab => \b[2]~input_o\,
	datad => \a[2]~input_o\,
	combout => \alu1|fa4|cout~0_combout\);

-- Location: LCCOMB_X1_Y8_N24
\alu3|fa2|cout~0\ : cycloneiv_lcell_comb
-- Equation(s):
-- \alu3|fa2|cout~0_combout\ = (\alu3|ha3|cout~combout\ & ((\alu3|ha2|s~combout\) # ((\b[1]~input_o\ & \a[2]~input_o\)))) # (!\alu3|ha3|cout~combout\ & (\alu3|ha2|s~combout\ & (\b[1]~input_o\ & \a[2]~input_o\)))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "1110100010001000",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \alu3|ha3|cout~combout\,
	datab => \alu3|ha2|s~combout\,
	datac => \b[1]~input_o\,
	datad => \a[2]~input_o\,
	combout => \alu3|fa2|cout~0_combout\);

-- Location: LCCOMB_X1_Y8_N2
\alu3|ha2|cout\ : cycloneiv_lcell_comb
-- Equation(s):
-- \alu3|ha2|cout~combout\ = (\alu3|fa1|cout~0_combout\ & (\a[1]~input_o\ & \b[2]~input_o\))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "1000100000000000",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \alu3|fa1|cout~0_combout\,
	datab => \a[1]~input_o\,
	datad => \b[2]~input_o\,
	combout => \alu3|ha2|cout~combout\);

-- Location: LCCOMB_X1_Y8_N20
\Mux1~0\ : cycloneiv_lcell_comb
-- Equation(s):
-- \Mux1~0_combout\ = (\Mux4~0_combout\ & (\alu1|fa4|cout~0_combout\ $ (\alu3|fa2|cout~0_combout\ $ (\alu3|ha2|cout~combout\))))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "1001000001100000",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \alu1|fa4|cout~0_combout\,
	datab => \alu3|fa2|cout~0_combout\,
	datac => \Mux4~0_combout\,
	datad => \alu3|ha2|cout~combout\,
	combout => \Mux1~0_combout\);

-- Location: LCCOMB_X1_Y8_N6
\alu3|fa3|cout~0\ : cycloneiv_lcell_comb
-- Equation(s):
-- \alu3|fa3|cout~0_combout\ = (\alu3|ha2|cout~combout\ & ((\alu3|fa2|cout~0_combout\) # ((\a[2]~input_o\ & \b[2]~input_o\)))) # (!\alu3|ha2|cout~combout\ & (\a[2]~input_o\ & (\b[2]~input_o\ & \alu3|fa2|cout~0_combout\)))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "1111100010000000",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \a[2]~input_o\,
	datab => \b[2]~input_o\,
	datac => \alu3|ha2|cout~combout\,
	datad => \alu3|fa2|cout~0_combout\,
	combout => \alu3|fa3|cout~0_combout\);

-- Location: LCCOMB_X1_Y8_N18
\Mux0~2\ : cycloneiv_lcell_comb
-- Equation(s):
-- \Mux0~2_combout\ = (\alu3|fa3|cout~0_combout\ & (\sel[1]~input_o\ & !\sel[0]~input_o\))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "0000000010100000",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \alu3|fa3|cout~0_combout\,
	datac => \sel[1]~input_o\,
	datad => \sel[0]~input_o\,
	combout => \Mux0~2_combout\);

ww_result(0) <= \result[0]~output_o\;

ww_result(1) <= \result[1]~output_o\;

ww_result(2) <= \result[2]~output_o\;

ww_result(3) <= \result[3]~output_o\;

ww_result(4) <= \result[4]~output_o\;

ww_result(5) <= \result[5]~output_o\;
END structure;


