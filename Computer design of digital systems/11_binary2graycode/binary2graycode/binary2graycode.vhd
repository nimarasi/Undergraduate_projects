library ieee;
use ieee.std_logic_1164.all;

entity b2g is
port(b:in bit_vector(3 downto 0);
		g:out bit_vector(3 downto 0));
end b2g;

architecture data of b2g is
begin
	g(3) <= b(3);
	g(2) <= b(3) xor b(2);
	g(1) <= b(2) xor b(1);
	g(0) <= b(1) xor b(0);
end data;