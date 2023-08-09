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

-- DATE "11/10/2022 18:24:17"

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

ENTITY 	bu IS
    PORT (
	a : IN std_logic;
	b : IN std_logic;
	oe : IN std_logic;
	y : OUT std_logic
	);
END bu;

-- Design Ports Information
-- y	=>  Location: PIN_B6,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- a	=>  Location: PIN_N4,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- b	=>  Location: PIN_C6,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- oe	=>  Location: PIN_L5,	 I/O Standard: 2.5 V,	 Current Strength: Default


ARCHITECTURE structure OF bu IS
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
SIGNAL ww_oe : std_logic;
SIGNAL ww_y : std_logic;
SIGNAL \y~output_o\ : std_logic;
SIGNAL \a~input_o\ : std_logic;
SIGNAL \b~input_o\ : std_logic;
SIGNAL \x~combout\ : std_logic;
SIGNAL \oe~input_o\ : std_logic;
SIGNAL \ALT_INV_oe~input_o\ : std_logic;

BEGIN

ww_a <= a;
ww_b <= b;
ww_oe <= oe;
y <= ww_y;
ww_devoe <= devoe;
ww_devclrn <= devclrn;
ww_devpor <= devpor;
\ALT_INV_oe~input_o\ <= NOT \oe~input_o\;

-- Location: IOOBUF_X14_Y31_N9
\y~output\ : cycloneiv_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false")
-- pragma translate_on
PORT MAP (
	i => \x~combout\,
	oe => \ALT_INV_oe~input_o\,
	devoe => ww_devoe,
	o => \y~output_o\);

-- Location: IOIBUF_X10_Y0_N8
\a~input\ : cycloneiv_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_a,
	o => \a~input_o\);

-- Location: IOIBUF_X14_Y31_N1
\b~input\ : cycloneiv_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_b,
	o => \b~input_o\);

-- Location: LCCOMB_X10_Y2_N0
x : cycloneiv_lcell_comb
-- Equation(s):
-- \x~combout\ = (!\b~input_o\) # (!\a~input_o\)

-- pragma translate_off
GENERIC MAP (
	lut_mask => "0000111111111111",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	datac => \a~input_o\,
	datad => \b~input_o\,
	combout => \x~combout\);

-- Location: IOIBUF_X14_Y0_N8
\oe~input\ : cycloneiv_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_oe,
	o => \oe~input_o\);

ww_y <= \y~output_o\;
END structure;


