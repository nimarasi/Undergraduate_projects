library ieee;
use ieee.std_logic_1164.all;

entity full is
port(a,b,cin :in bit;
		s,cout :out bit);
end full;

architecture data of full is
signal o1,o2,o3:bit;
begin
		o1 <= a xor b;
		o2 <= a and b;
		s <= o1 xor cin;
		o3 <= cin and o1;
		cout <= o3 or o2;
end data;