library ieee;
use ieee.std_logic_1164.all;

entity eq is
port(a,b:in bit_vector(3 downto 0);
		o :out bit);
end eq;

architecture data of eq is
begin
o <= (a(3) xnor b(3))
	and (a(2) xnor b(2))
	and (a(1) xnor b(1))
	and (a(0) xnor b(0));
end data;