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

-- DATE "11/10/2022 16:43:35"

-- 
-- Device: Altera EP4CGX15BF14C6 Package FBGA169
-- 

-- 
-- This VHDL file should be used for ModelSim-Altera (VHDL) only
-- 

LIBRARY CYCLONEIV;
LIBRARY IEEE;
LIBRARY STD;
USE CYCLONEIV.CYCLONEIV_COMPONENTS.ALL;
USE IEEE.STD_LOGIC_1164.ALL;
USE STD.STANDARD.ALL;

ENTITY 	ff IS
    PORT (
	a : IN std_logic;
	b : IN std_logic;
	c : IN std_logic;
	o1 : INOUT std_logic;
	o2 : INOUT std_logic;
	y1 : BUFFER STD.STANDARD.bit;
	y2 : BUFFER STD.STANDARD.bit
	);
END ff;

-- Design Ports Information
-- y1	=>  Location: PIN_L7,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- y2	=>  Location: PIN_N4,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- o1	=>  Location: PIN_M4,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- o2	=>  Location: PIN_L4,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- b	=>  Location: PIN_L5,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- c	=>  Location: PIN_M6,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- a	=>  Location: PIN_L11,	 I/O Standard: 2.5 V,	 Current Strength: Default


ARCHITECTURE structure OF ff IS
SIGNAL gnd : std_logic := '0';
SIGNAL vcc : std_logic := '1';
SIGNAL unknown : std_logic := 'X';
SIGNAL devoe : std_logic := '1';
SIGNAL devclrn : std_logic := '1';
SIGNAL devpor : std_logic := '1';
SIGNAL ww_devoe : std_logic;
SIGNAL ww_devclrn : std_logic;
SIGNAL ww_devpor : std_logic;
SIGNAL ww_a : std_logic;
SIGNAL ww_b : std_logic;
SIGNAL ww_c : std_logic;
SIGNAL ww_y1 : std_logic;
SIGNAL ww_y2 : std_logic;
SIGNAL \o1~input_o\ : std_logic;
SIGNAL \o2~input_o\ : std_logic;
SIGNAL \o1~output_o\ : std_logic;
SIGNAL \o2~output_o\ : std_logic;
SIGNAL \y1~output_o\ : std_logic;
SIGNAL \y2~output_o\ : std_logic;
SIGNAL \c~input_o\ : std_logic;
SIGNAL \a~input_o\ : std_logic;
SIGNAL \o1~2_combout\ : std_logic;
SIGNAL \b~input_o\ : std_logic;
SIGNAL \o2~2_combout\ : std_logic;
SIGNAL \y1~1_combout\ : std_logic;
SIGNAL \y2~0_combout\ : std_logic;
SIGNAL \ALT_INV_y1~1_combout\ : std_logic;
SIGNAL \ALT_INV_y2~0_combout\ : std_logic;

BEGIN

ww_a <= a;
ww_b <= b;
ww_c <= c;
y1 <= IEEE.STD_LOGIC_1164.TO_BIT(ww_y1);
y2 <= IEEE.STD_LOGIC_1164.TO_BIT(ww_y2);
ww_devoe <= devoe;
ww_devclrn <= devclrn;
ww_devpor <= devpor;
\ALT_INV_y1~1_combout\ <= NOT \y1~1_combout\;
\ALT_INV_y2~0_combout\ <= NOT \y2~0_combout\;

-- Location: IOOBUF_X8_Y0_N2
\o1~output\ : cycloneiv_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false")
-- pragma translate_on
PORT MAP (
	i => \o1~2_combout\,
	oe => VCC,
	devoe => ww_devoe,
	o => \o1~output_o\);

-- Location: IOOBUF_X8_Y0_N9
\o2~output\ : cycloneiv_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false")
-- pragma translate_on
PORT MAP (
	i => \o2~2_combout\,
	oe => VCC,
	devoe => ww_devoe,
	o => \o2~output_o\);

-- Location: IOOBUF_X14_Y0_N2
\y1~output\ : cycloneiv_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false")
-- pragma translate_on
PORT MAP (
	i => \ALT_INV_y1~1_combout\,
	devoe => ww_devoe,
	o => \y1~output_o\);

-- Location: IOOBUF_X10_Y0_N9
\y2~output\ : cycloneiv_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false")
-- pragma translate_on
PORT MAP (
	i => \ALT_INV_y2~0_combout\,
	devoe => ww_devoe,
	o => \y2~output_o\);

-- Location: IOIBUF_X12_Y0_N8
\c~input\ : cycloneiv_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_c,
	o => \c~input_o\);

-- Location: IOIBUF_X31_Y0_N1
\a~input\ : cycloneiv_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_a,
	o => \a~input_o\);

-- Location: LCCOMB_X12_Y1_N4
\o1~2\ : cycloneiv_lcell_comb
-- Equation(s):
-- \o1~2_combout\ = (\c~input_o\ & \a~input_o\)

-- pragma translate_off
GENERIC MAP (
	lut_mask => "1010101000000000",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \c~input_o\,
	datad => \a~input_o\,
	combout => \o1~2_combout\);

-- Location: IOIBUF_X14_Y0_N8
\b~input\ : cycloneiv_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_b,
	o => \b~input_o\);

-- Location: LCCOMB_X12_Y1_N22
\o2~2\ : cycloneiv_lcell_comb
-- Equation(s):
-- \o2~2_combout\ = (\c~input_o\ & \b~input_o\)

-- pragma translate_off
GENERIC MAP (
	lut_mask => "1010000010100000",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \c~input_o\,
	datac => \b~input_o\,
	combout => \o2~2_combout\);

-- Location: LCCOMB_X12_Y1_N2
\y1~1\ : cycloneiv_lcell_comb
-- Equation(s):
-- \y1~1_combout\ = (\c~input_o\ & ((\a~input_o\) # ((\y1~1_combout\ & !\b~input_o\)))) # (!\c~input_o\ & (\y1~1_combout\))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "1110111001001100",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \c~input_o\,
	datab => \y1~1_combout\,
	datac => \b~input_o\,
	datad => \a~input_o\,
	combout => \y1~1_combout\);

-- Location: LCCOMB_X12_Y1_N24
\y2~0\ : cycloneiv_lcell_comb
-- Equation(s):
-- \y2~0_combout\ = ((\c~input_o\ & \b~input_o\)) # (!\y1~1_combout\)

-- pragma translate_off
GENERIC MAP (
	lut_mask => "1011001110110011",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \c~input_o\,
	datab => \y1~1_combout\,
	datac => \b~input_o\,
	combout => \y2~0_combout\);

-- Location: IOIBUF_X8_Y0_N1
\o1~input\ : cycloneiv_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => o1,
	o => \o1~input_o\);

-- Location: IOIBUF_X8_Y0_N8
\o2~input\ : cycloneiv_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => o2,
	o => \o2~input_o\);

ww_y1 <= \y1~output_o\;

ww_y2 <= \y2~output_o\;

o1 <= \o1~output_o\;

o2 <= \o2~output_o\;
END structure;


