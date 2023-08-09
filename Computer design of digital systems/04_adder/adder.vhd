library ieee;
use ieee.std_logic_1164.all;

entity adder is 
port( a,b : in integer range 0 to 7;
		c : out integer range 0 to 15);
end adder;

architecture data of adder is 
begin 
	c<=a+b;
end data;
	