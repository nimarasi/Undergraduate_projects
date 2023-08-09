library ieee;
use ieee.std_logic_1164.all;

entity ff is
port(a,b,c:in bit;
		o1,o2:inout bit;
		y1,y2:buffer bit);
end ff;

architecture data of ff is
begin
	o1 <= a and c;
	o2 <= b and c;
	y1 <= o1 nor y2;
	y2 <= o2 nor y1;
end data;