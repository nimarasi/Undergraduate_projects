library ieee;
use ieee.std_logic_1164.all;

entity encoder is
port(x:in bit_vector(3 downto 0);
		y0,y1:out bit);
end encoder;

architecture data of encoder is
begin
	y0 <= (((not(x(0)) and not(x(1))) and x(2)) and not(x(3))) or (((not(x(0)) and not(x(1))) and not(x(2))) and x(3));
	y1 <= (((not(x(0)) and x(1)) and not(x(2))) and not(x(3))) or (((not(x(0)) and not(x(1))) and not(x(2))) and x(3));
end data;