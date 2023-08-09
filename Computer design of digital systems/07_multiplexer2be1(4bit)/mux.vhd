library ieee;
use ieee.std_logic_1164.all;

entity mux is 
port(a,b:in std_logic_vector(3 downto 0);
		s:in bit;
		o:out std_logic_vector(3 downto 0));
end mux;

architecture data of mux is
begin
	o <= a when s='0' else b;
end data;