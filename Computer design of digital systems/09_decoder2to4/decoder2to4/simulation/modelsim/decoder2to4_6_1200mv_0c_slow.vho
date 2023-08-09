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

-- DATE "11/11/2022 11:53:33"

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

ENTITY 	decoder IS
    PORT (
	a : IN std_logic;
	b : IN std_logic;
	cin : IN std_logic;
	y0 : OUT STD.STANDARD.bit;
	y1 : OUT STD.STANDARD.bit;
	y2 : OUT STD.STANDARD.bit;
	y3 : OUT STD.STANDARD.bit
	);
END decoder;

-- Design Ports Information
-- y0	=>  Location: PIN_M4,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- y1	=>  Location: PIN_M6,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- y2	=>  Location: PIN_N4,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- y3	=>  Location: PIN_L7,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- a	=>  Location: PIN_L4,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- b	=>  Location: PIN_N6,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- cin	=>  Location: PIN_L11,	 I/O Standard: 2.5 V,	 Current Strength: Default


ARCHITECTURE structure OF decoder IS
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
SIGNAL ww_cin : std_logic;
SIGNAL ww_y0 : std_logic;
SIGNAL ww_y1 : std_logic;
SIGNAL ww_y2 : std_logic;
SIGNAL ww_y3 : std_logic;
SIGNAL \y0~output_o\ : std_logic;
SIGNAL \y1~output_o\ : std_logic;
SIGNAL \y2~output_o\ : std_logic;
SIGNAL \y3~output_o\ : std_logic;
SIGNAL \cin~input_o\ : std_logic;
SIGNAL \b~input_o\ : std_logic;
SIGNAL \a~input_o\ : std_logic;
SIGNAL \y0~0_combout\ : std_logic;
SIGNAL \y1~0_combout\ : std_logic;
SIGNAL \y2~0_combout\ : std_logic;
SIGNAL \y3~0_combout\ : std_logic;
SIGNAL \ALT_INV_y3~0_combout\ : std_logic;
SIGNAL \ALT_INV_y2~0_combout\ : std_logic;
SIGNAL \ALT_INV_y1~0_combout\ : std_logic;
SIGNAL \ALT_INV_y0~0_combout\ : std_logic;

BEGIN

ww_a <= a;
ww_b <= b;
ww_cin <= cin;
y0 <= IEEE.STD_LOGIC_1164.TO_BIT(ww_y0);
y1 <= IEEE.STD_LOGIC_1164.TO_BIT(ww_y1);
y2 <= IEEE.STD_LOGIC_1164.TO_BIT(ww_y2);
y3 <= IEEE.STD_LOGIC_1164.TO_BIT(ww_y3);
ww_devoe <= devoe;
ww_devclrn <= devclrn;
ww_devpor <= devpor;
\ALT_INV_y3~0_combout\ <= NOT \y3~0_combout\;
\ALT_INV_y2~0_combout\ <= NOT \y2~0_combout\;
\ALT_INV_y1~0_combout\ <= NOT \y1~0_combout\;
\ALT_INV_y0~0_combout\ <= NOT \y0~0_combout\;

-- Location: IOOBUF_X8_Y0_N2
\y0~output\ : cycloneiv_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false")
-- pragma translate_on
PORT MAP (
	i => \ALT_INV_y0~0_combout\,
	devoe => ww_devoe,
	o => \y0~output_o\);

-- Location: IOOBUF_X12_Y0_N9
\y1~output\ : cycloneiv_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false")
-- pragma translate_on
PORT MAP (
	i => \ALT_INV_y1~0_combout\,
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

-- Location: IOOBUF_X14_Y0_N2
\y3~output\ : cycloneiv_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false")
-- pragma translate_on
PORT MAP (
	i => \ALT_INV_y3~0_combout\,
	devoe => ww_devoe,
	o => \y3~output_o\);

-- Location: IOIBUF_X31_Y0_N1
\cin~input\ : cycloneiv_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_cin,
	o => \cin~input_o\);

-- Location: IOIBUF_X12_Y0_N1
\b~input\ : cycloneiv_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_b,
	o => \b~input_o\);

-- Location: IOIBUF_X8_Y0_N8
\a~input\ : cycloneiv_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_a,
	o => \a~input_o\);

-- Location: LCCOMB_X11_Y1_N8
\y0~0\ : cycloneiv_lcell_comb
-- Equation(s):
-- \y0~0_combout\ = ((\b~input_o\ & \a~input_o\)) # (!\cin~input_o\)

-- pragma translate_off
GENERIC MAP (
	lut_mask => "1101010111010101",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \cin~input_o\,
	datab => \b~input_o\,
	datac => \a~input_o\,
	combout => \y0~0_combout\);

-- Location: LCCOMB_X11_Y1_N2
\y1~0\ : cycloneiv_lcell_comb
-- Equation(s):
-- \y1~0_combout\ = ((!\b~input_o\ & \a~input_o\)) # (!\cin~input_o\)

-- pragma translate_off
GENERIC MAP (
	lut_mask => "0111010101110101",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \cin~input_o\,
	datab => \b~input_o\,
	datac => \a~input_o\,
	combout => \y1~0_combout\);

-- Location: LCCOMB_X11_Y1_N4
\y2~0\ : cycloneiv_lcell_comb
-- Equation(s):
-- \y2~0_combout\ = ((\b~input_o\ & !\a~input_o\)) # (!\cin~input_o\)

-- pragma translate_off
GENERIC MAP (
	lut_mask => "0101110101011101",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \cin~input_o\,
	datab => \b~input_o\,
	datac => \a~input_o\,
	combout => \y2~0_combout\);

-- Location: LCCOMB_X11_Y1_N22
\y3~0\ : cycloneiv_lcell_comb
-- Equation(s):
-- \y3~0_combout\ = ((!\b~input_o\ & !\a~input_o\)) # (!\cin~input_o\)

-- pragma translate_off
GENERIC MAP (
	lut_mask => "0101011101010111",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \cin~input_o\,
	datab => \b~input_o\,
	datac => \a~input_o\,
	combout => \y3~0_combout\);

ww_y0 <= \y0~output_o\;

ww_y1 <= \y1~output_o\;

ww_y2 <= \y2~output_o\;

ww_y3 <= \y3~output_o\;
END structure;


