library ieee;
use ieee.std_logic_1164.all;

entity bu is
port(a,b:in std_logic;
		oe:in std_logic;
		y:out std_logic);
end bu;


architecture buf of bu is
	signal x :std_logic;
	
begin
	x <= a nand b;
	y <= x when oe='0' else 'Z';
end buf;