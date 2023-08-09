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

-- DATE "11/11/2022 12:23:31"

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

ENTITY 	encoder IS
    PORT (
	x : IN STD.STANDARD.bit_vector(3 DOWNTO 0);
	y0 : OUT STD.STANDARD.bit;
	y1 : OUT STD.STANDARD.bit
	);
END encoder;

-- Design Ports Information
-- y0	=>  Location: PIN_A7,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- y1	=>  Location: PIN_N9,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- x[0]	=>  Location: PIN_M4,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- x[1]	=>  Location: PIN_M6,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- x[2]	=>  Location: PIN_N4,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- x[3]	=>  Location: PIN_L11,	 I/O Standard: 2.5 V,	 Current Strength: Default


ARCHITECTURE structure OF encoder IS
SIGNAL gnd : std_logic := '0';
SIGNAL vcc : std_logic := '1';
SIGNAL unknown : std_logic := 'X';
SIGNAL devoe : std_logic := '1';
SIGNAL devclrn : std_logic := '1';
SIGNAL devpor : std_logic := '1';
SIGNAL ww_devoe : std_logic;
SIGNAL ww_devclrn : std_logic;
SIGNAL ww_devpor : std_logic;
SIGNAL ww_x : std_logic_vector(3 DOWNTO 0);
SIGNAL ww_y0 : std_logic;
SIGNAL ww_y1 : std_logic;
SIGNAL \y0~output_o\ : std_logic;
SIGNAL \y1~output_o\ : std_logic;
SIGNAL \x[2]~input_o\ : std_logic;
SIGNAL \x[0]~input_o\ : std_logic;
SIGNAL \x[1]~input_o\ : std_logic;
SIGNAL \x[3]~input_o\ : std_logic;
SIGNAL \y0~0_combout\ : std_logic;
SIGNAL \y1~0_combout\ : std_logic;
SIGNAL \ALT_INV_y0~0_combout\ : std_logic;

BEGIN

ww_x <= IEEE.STD_LOGIC_1164.TO_STDLOGICVECTOR(x);
y0 <= IEEE.STD_LOGIC_1164.TO_BIT(ww_y0);
y1 <= IEEE.STD_LOGIC_1164.TO_BIT(ww_y1);
ww_devoe <= devoe;
ww_devclrn <= devclrn;
ww_devpor <= devpor;
\ALT_INV_y0~0_combout\ <= NOT \y0~0_combout\;

-- Location: IOOBUF_X12_Y31_N2
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

-- Location: IOOBUF_X20_Y0_N2
\y1~output\ : cycloneiv_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false")
-- pragma translate_on
PORT MAP (
	i => \y1~0_combout\,
	devoe => ww_devoe,
	o => \y1~output_o\);

-- Location: IOIBUF_X10_Y0_N8
\x[2]~input\ : cycloneiv_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_x(2),
	o => \x[2]~input_o\);

-- Location: IOIBUF_X8_Y0_N1
\x[0]~input\ : cycloneiv_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_x(0),
	o => \x[0]~input_o\);

-- Location: IOIBUF_X12_Y0_N8
\x[1]~input\ : cycloneiv_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_x(1),
	o => \x[1]~input_o\);

-- Location: IOIBUF_X31_Y0_N1
\x[3]~input\ : cycloneiv_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_x(3),
	o => \x[3]~input_o\);

-- Location: LCCOMB_X12_Y1_N24
\y0~0\ : cycloneiv_lcell_comb
-- Equation(s):
-- \y0~0_combout\ = (\x[0]~input_o\) # ((\x[1]~input_o\) # (\x[2]~input_o\ $ (!\x[3]~input_o\)))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "1111111011111101",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \x[2]~input_o\,
	datab => \x[0]~input_o\,
	datac => \x[1]~input_o\,
	datad => \x[3]~input_o\,
	combout => \y0~0_combout\);

-- Location: LCCOMB_X12_Y1_N26
\y1~0\ : cycloneiv_lcell_comb
-- Equation(s):
-- \y1~0_combout\ = (!\x[2]~input_o\ & (!\x[0]~input_o\ & (\x[1]~input_o\ $ (\x[3]~input_o\))))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "0000000100010000",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \x[2]~input_o\,
	datab => \x[0]~input_o\,
	datac => \x[1]~input_o\,
	datad => \x[3]~input_o\,
	combout => \y1~0_combout\);

ww_y0 <= \y0~output_o\;

ww_y1 <= \y1~output_o\;
END structure;


