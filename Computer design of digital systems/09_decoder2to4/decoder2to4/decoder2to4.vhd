library ieee;
use ieee.std_logic_1164.all;

entity decoder is
port(a,b:in bit;
		y0,y1,y2,y3:out bit);
end decoder;

architecture data of decoder is
begin
	y0 <= not(a) and not(b);
	y1 <= not(a) and b ;
	y2 <= a and not(b);
	y3 <= a and b;
end data;