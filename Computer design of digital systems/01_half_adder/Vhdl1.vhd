library ieee;
use ieee.std_logic_1164.all;


entity halfadder is
port(a,b:in bit;
		co,s:out bit);
end halfadder;
		
architecture data of halfadder is
begin
	s <= a xor b;
	co <= a and b;
end data;
