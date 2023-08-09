library ieee;
use ieee.std_logic_1164.all;

entity mux is 
port(a,b:in bit;
		s:in bit;
		o:out bit);
end mux;

architecture data of mux is 
signal o1,o2 :bit;
begin
	o1 <= not(s) and a;
	o2 <= s and b;
	o <= o1 or o2;
end data;